import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Flappy Bird')

# Cores
branco = (255, 255, 255)
azul = (0, 0, 255)

# Personagem
personagem_x = 50
personagem_y = 300
personagem_velocidade = 5
personagem_altura = 30
personagem_largura = 30

# Obstáculos
obstaculo_x = largura_tela
obstaculo_y = [random.randint(100, 400), random.randint(100, 400)]
obstaculo_largura = 50
obstaculo_velocidade = 5
espaco_obstaculos = 150

# Pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

def desenhar_personagem(x, y):
    pygame.draw.rect(tela, azul, (x, y, personagem_largura, personagem_altura))

def desenhar_obstaculos(x, y1, y2):
    pygame.draw.rect(tela, branco, (x, 0, obstaculo_largura, y1))
    pygame.draw.rect(tela, branco, (x, y2 + espaco_obstaculos, obstaculo_largura, altura_tela - y2 - espaco_obstaculos))

def main():
    global obstaculo_x, obstaculo_y, pontuacao

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personagem_y -= 50

        personagem_y += personagem_velocidade

        tela.fill((0, 0, 0))

        desenhar_personagem(personagem_x, personagem_y)

        for i in range(len(obstaculo_x)):
            obstaculo_x[i] -= obstaculo_velocidade
            desenhar_obstaculos(obstaculo_x[i], obstaculo_y[i][0], obstaculo_y[i][1])

            if obstaculo_x[i] < -obstaculo_largura:
                obstaculo_x[i] = largura_tela
                obstaculo_y[i] = [random.randint(100, 400), random.randint(100, 400)]
                pontuacao += 1

            # Checa colisão com obstáculos
            if personagem_x < obstaculo_x[i] + obstaculo_largura and personagem_x + personagem_largura > obstaculo_x[i]:
                if personagem_y < obstaculo_y[i][0] or personagem_y + personagem_altura > obstaculo_y[i][1] + espaco_obstaculos:
                    pygame.quit()
                    sys.exit()

        # Checa colisão com as bordas da tela
        if personagem_y < 0 or personagem_y + personagem_altura > altura_tela:
            pygame.quit()
            sys.exit()

        # Exibe pontuação na tela
        texto = fonte.render(f'Pontuação: {pontuacao}', True, branco)
        tela.blit(texto, (10, 10))

        pygame.display.update()

if _name_ == "_main_":
    main()