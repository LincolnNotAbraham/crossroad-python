# 🚗 Mini Crossy Road

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Um joguinho simples inspirado no **Crossy Road**, desenvolvido em Python com a biblioteca Pygame. O objetivo é atravessar a rua desviando dos obstáculos (carros) o máximo que puder!

## 🎮 Funcionalidades

- Movimentação do personagem (WASD)
- Geração randômica de carros com cores aleatórias
- Detecção de colisão com obstáculos
- Contagem de score
- Sons de buzina e batida
- Música de fundo em loop
- Tela de Game Over com reinício (tecla R)

## 📦 Tecnologias Utilizadas

- **Python 3**
- **Pygame** — biblioteca para criação de jogos 2D

## 🚀 Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/LincolnNotAbraham/crossroad-python.git
cd crossroad-python
```

2. Instale as dependências:

```bash
pip install -r requirementes.txt
```

3. Execute o jogo:

```bash
python src/crossroad.py
```

## 🕹️ Controles

| Tecla | Ação |
|-------|------|
| `W` | Mover para cima |
| `S` | Mover para baixo |
| `A` | Mover para a esquerda |
| `D` | Mover para a direita |
| `R` | Reiniciar (após Game Over) |

## 📁 Estrutura do Projeto

```
crossroad-python/
├── src/
│   └── crossroad.py      # Código principal do jogo
├── assets/
│   ├── musica.mp3         # Música de fundo
│   ├── buzina.mp3         # Som de buzina
│   ├── buzina_grave.mp3   # Som de buzina grave
│   ├── batida.wav         # Som de colisão
│   └── velho.png          # Sprite do personagem (em uso)
├── requirementes.txt      # Dependências do projeto
└── README.md
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

## 👤 Autor

**Lincoln** — [GitHub](https://github.com/LincolnNotAbraham)
