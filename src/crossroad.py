"""
Mini Crossy Road
================
Um joguinho inspirado no Crossy Road, desenvolvido em Python com Pygame.
O jogador deve atravessar a rua desviando dos carros.

Controles: WASD para movimentação, R para reiniciar após Game Over.
"""

import pygame
from pygame.locals import *
from sys import exit
import random
import os

# --- Configuração de caminhos de assets ---
diretorio = os.path.join(os.path.dirname(__file__), '..', 'assets')
diretorio = os.path.abspath(diretorio)

arquivos = {}
for arquivo in os.listdir(diretorio):
    caminho_imagem = os.path.join(diretorio, arquivo)
    arquivos[arquivo] = caminho_imagem

# --- Inicialização do Pygame ---
pygame.init()
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mini Crossy Road")

# --- Áudio ---
# Música de fundo em loop infinito
musica = pygame.mixer.music.load(arquivos['musica.mp3'])
pygame.mixer.music.play(-1)

# Efeitos sonoros
batida = pygame.mixer.Sound(arquivos['batida.wav'])  # Som ao colidir com carro
buzina1 = pygame.mixer.Sound(arquivos['buzina_grave.mp3'])
buzina2 = pygame.mixer.Sound(arquivos['buzina.mp3'])
buzinas = [buzina1, buzina2]

# --- Grupos de sprites e relógio ---
todas_sprites = pygame.sprite.Group()
relogio = pygame.time.Clock()

# --- Variáveis do jogador ---
x_jogador = 240
y_jogador = 450
borda_livre_cima = True
borda_livre_baixo = True
borda_livre_esquerda = True
borda_livre_direita = True

# --- Variáveis dos carros ---
y_carros = 400
x_carros = 10
xi_carros = 630

# Posições iniciais possíveis para os carros (lado esquerdo e direito)
posicoesx_carros = [20, 15, 10, 16, 589, 585, 590, 595]

# --- Variáveis de controle ---
cores = []              # Cores geradas aleatoriamente para cada carro
carros_lista = []       # Lista de retângulos dos carros na tela
lista_Xcarros = []      # Posições X atuais dos carros
lista_Xcarros_inicio = []  # Posições X iniciais dos carros
pontos = 0              # Score do jogador
velocidade = 10         # Velocidade de movimentação do jogador
primeira_vez = 1        # Flag para primeira geração de carros
morreu = False          # Estado de Game Over

fonte = pygame.font.SysFont("arial", 20, True, False)


def carros(q):
    """
    Gera ou atualiza os carros na tela.

    Se q > 0 (primeira vez ou reinício), gera 8 carros com posições
    e cores aleatórias. Caso contrário, move os carros existentes.

    Args:
        q: Se > 0, gera novos carros. Se == 0, atualiza posições.
    """
    global carros_lista, primeira_vez

    if q > 0:
        # Gerar novos carros com cores e posições aleatórias
        for i in range(8):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            cores.append((r, g, b))
            x_carros = random.choice(posicoesx_carros)
            carro = pygame.draw.rect(tela, (r, g, b), (x_carros, y_carros - 60 * i, 30, 20))
            carros_lista.append(carro)
            primeira_vez = 0
            lista_Xcarros.append(x_carros)
            lista_Xcarros_inicio.append(x_carros)
    else:
        # Mover carros existentes conforme sua direção original
        for i in range(8):
            x_carros = lista_Xcarros[i]
            carro = pygame.draw.rect(tela, (cores[i]), (x_carros, y_carros - 60 * i, 30, 20))
            carros_lista.append(carro)

            # Carros da esquerda vão para a direita, da direita vão para a esquerda
            if 30 > lista_Xcarros_inicio[i] > 0:
                lista_Xcarros[i] += 4 * pontos  # Velocidade aumenta com a pontuação
            if 600 > lista_Xcarros_inicio[i] > 100:
                lista_Xcarros[i] -= 4 * pontos

            # wrap-around: carro que sai da tela volta pelo outro lado
            if lista_Xcarros[i] <= 0:
                lista_Xcarros[i] = 639
            elif lista_Xcarros[i] > 640:
                lista_Xcarros[i] = 1

            # Toca buzina quando o carro passa pela posição X do jogador
            if x_jogador == lista_Xcarros[i]:
                buzina2.play()


def reiniciar_jogo():
    """Reinicia todas as variáveis do jogo para o estado inicial."""
    global y_jogador, x_jogador, lista_Xcarros, lista_Xcarros_inicio
    global x_carros, y_carros, pontos, primeira_vez, cores, carros_lista
    x_jogador = 240
    y_jogador = 450
    primeira_vez = 1
    cores = []
    lista_Xcarros = []
    lista_Xcarros_inicio = []
    carros_lista = []


# --- Loop principal do jogo ---
while True and not morreu:
    carros_lista = []
    relogio.tick(30)  # 30 FPS
    tela.fill("white")

    # Renderizar texto de pontuação
    mensagame = f'Pontos: {pontos}'
    texto_completo = fonte.render(mensagame, False, 'black')

    # Processar eventos (fechar janela)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Verificar limites da tela para restringir movimento
    if y_jogador <= 10:
        borda_livre_cima = False
    if y_jogador >= 465:
        borda_livre_baixo = False
    if x_jogador >= 630:
        borda_livre_direita = False
    if x_jogador <= 10:
        borda_livre_esquerda = False

    # Movimentação do jogador com WASD
    if pygame.key.get_pressed()[K_w] and borda_livre_cima:
        y_jogador -= velocidade
        borda_livre_baixo = True
    if pygame.key.get_pressed()[K_a] and borda_livre_esquerda:
        x_jogador -= velocidade
        borda_livre_direita = True
    if pygame.key.get_pressed()[K_s] and borda_livre_baixo:
        y_jogador += velocidade
        borda_livre_cima = True
    if pygame.key.get_pressed()[K_d] and borda_livre_direita:
        x_jogador += velocidade
        borda_livre_esquerda = True

    # Jogador chegou ao topo: ganha ponto e reinicia posição
    if y_jogador <= 10:
        y_jogador = 481
        pontos += 1
        reiniciar_jogo()

    # Desenhar jogador (quadrado preto)
    jogador = pygame.draw.rect(tela, ('black'), (x_jogador, y_jogador, 10, 10))

    # Gerar/atualizar carros
    carros(primeira_vez)

    # Verificar colisão do jogador com carros
    for carro in carros_lista:
        if jogador.colliderect(carro):
            morreu = True
            pontos = 0
            batida.play()
            pygame.mixer.music.stop()
            fonte2 = pygame.font.SysFont("arial", 20, True, False)
            mensagame = "Game Over, Pressione a tecla R para jogar novamente"
            texto_completo = fonte2.render(mensagame, True, 'black')

    # Tela de Game Over: aguarda tecla R para reiniciar
    while morreu:
        tela.fill('white')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciar_jogo()
                    morreu = False
                    primeira_vez = 1
                    pygame.display.update()
                    pygame.mixer.music.play(-1)

        tela.blit(texto_completo, (50, 250))
        pygame.display.update()

    # Atualizar tela
    pygame.display.update()
    tela.blit(texto_completo, (300, 50))
    pygame.display.flip()
