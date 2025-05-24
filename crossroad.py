import pygame
from pygame.locals import*
from sys import exit
import random
#from pygame.sprite import AbstractGroup
import os

diretorio = os.path.dirname(__file__)
arquivos = {}

for arquivo in os.listdir(diretorio):
    caminho_imagem = os.path.join(diretorio, arquivo)
    arquivos[arquivo] = caminho_imagem

pygame.init()
largura = 640
altura = 480
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Animação")


musica = pygame.mixer.music.load(arquivos['musica.mp3'])
pygame.mixer.music.play(-1)#esse -1 server pra criar um loop



batida = pygame.mixer.Sound(arquivos['batida.wav'])
buzina1 = pygame.mixer.Sound(arquivos['buzina_grave.mp3'])
buzina2 = pygame.mixer.Sound(arquivos['buzina.mp3'])
buzinas = [buzina1,buzina2]

todas_sprites = pygame.sprite.Group()

relogio = pygame.time.Clock()

x_jogador = 240
y_jogador = 450
borda_livre_cima = True
borda_livre_baixo = True
borda_livre_esquerda = True
borda_livre_direita = True

y_carros = 400
x_carros = 10
xi_carros = 630

cores = []
def carros(q):
    global carros_lista
    global primeira_vez

    if q > 0:
        for i in range(8):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            cores.append((r,g,b))
            x_carros = random.choice(posiçoesx_carros)
            carro = pygame.draw.rect(tela,(r,g,b),(x_carros,y_carros-60*i,30,20))
            carros_lista.append(carro)
            primeira_vez  = 0
            lista_Xcarros.append(x_carros)
            lista_Xcarros_inicio.append(x_carros)
           
    else:
        for i in range(8):
            x_carros = lista_Xcarros[i]
            carro = pygame.draw.rect(tela,(cores[i]),(x_carros,y_carros-60*i,30,20))
            carros_lista.append(carro)
            if 30>lista_Xcarros_inicio[i]>0:
                lista_Xcarros[i] += 4*pontos  
            if 600>lista_Xcarros_inicio[i]>100:
                lista_Xcarros[i] -= 4*pontos

            if lista_Xcarros[i] <= 0:
                    lista_Xcarros[i] = 639

            elif lista_Xcarros[i] > 640:
                    lista_Xcarros[i] = 1

            if x_jogador == lista_Xcarros[i]:
             buzina2.play()   
                        
def reiniciar_jogo():
    global y_jogador,x_jogador,lista_Xcarros,lista_Xcarros_inicio,x_carros,y_carros,pontos,primeira_vez,cores,carros_lista
    x_jogador = 240
    y_jogador = 450
    primeira_vez = 1
    cores = []
    lista_Xcarros = []
    lista_Xcarros_inicio = []
    carros_lista = []



#velho = pygame.image.load(arquivos['velho.png'])
#sprite = pygame.sprite.Sprite()
#sprite.image = velho
#velho_n = pygame.transform.scale(velho,(64,64))
#sprite.image  = velho_n

morreu = False
primeira_vez = 1

velocidade = 10
carros_lista = []
lista_Xcarros = []
lista_Xcarros_inicio = []
pontos = 0

posiçoesx_carros =[20,15,10,16,589,585,590,595]
fonte = pygame.font.SysFont("arial",20,True,False)

while True and not morreu:
    carros_lista = []
    relogio.tick(30)
    tela.fill("white")
    mensagame = f'Pontos: {pontos}'
    texto_completo = fonte.render(mensagame,False,'black')


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit

    #todas_sprites.draw(tela)
    #todas_sprites.update()


    if y_jogador <= 10: 
         borda_livre_cima = False
    if y_jogador >= 465:
         borda_livre_baixo = False

    if x_jogador >= 630:
         borda_livre_direita = False
    if x_jogador <= 10:
         borda_livre_esquerda = False



    if pygame.key.get_pressed()[K_w] and borda_livre_cima:
        y_jogador-=velocidade
        borda_livre_baixo = True


    if pygame.key.get_pressed()[K_a] and borda_livre_esquerda:
        x_jogador-=velocidade
        borda_livre_direita = True

    if pygame.key.get_pressed()[K_s] and borda_livre_baixo:
        y_jogador+=velocidade
        borda_livre_cima = True

    if pygame.key.get_pressed()[K_d] and borda_livre_direita:
        x_jogador+=velocidade
        borda_livre_esquerda = True

    if y_jogador<=10:
            y_jogador = 481
            pontos +=1
            reiniciar_jogo()


    
    
    jogador =pygame.draw.rect(tela,('black'),(x_jogador,y_jogador,10,10))
    

    carros(primeira_vez)
    

    for carro in carros_lista:
        if jogador.colliderect(carro):
            morreu = True
            pontos = 0
            batida.play()
            pygame.mixer.music.stop()
            fonte2 = pygame.font.SysFont("arial",20,True,False)
            mensagame = "Game Over, Pressione a tecla R para jogar novamente"
            texto_completo = fonte2.render(mensagame,True,'black')


    while morreu:
            tela.fill('white')
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                        morreu = False
                        print("ae")
                        primeira_vez = 1
                        pygame.display.update()
                        pygame.mixer.music.play(-1)

            tela.blit(texto_completo, (50,250)) 
            pygame.display.update()
                       
    pygame.display.update()
    tela.blit(texto_completo, (300,50))
    #tela.blit(jogador, (x_jogador-25,y_jogador-29))
    pygame.display.flip()