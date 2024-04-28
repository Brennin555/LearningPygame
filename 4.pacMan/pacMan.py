#Aula 25 - pacMan

import pygame
import constsPacMan as consts
import sprites as sp
import os

class Game:
    def __init__(self):
        #criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((consts.LARGURA, consts.ALTURA))
        pygame.display.set_caption(consts.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.estaRodando = True
        self.fonte = pygame.font.match_font(consts.FONTE, 36)
        self.carregar_arquivos()
        
    def novoJogo(self):
        #instancia as classes das sprites do jogo
        self.todas_sprites = pygame.sprite.Group()
        self.rodar()
        
    def rodar(self):
        self.jogando = True
        while self.jogando: 
            self.relogio.tick(consts.FPS)
            self.eventos()
            self.atualiza_sprites()
            self.desenha_sprites()

    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.estaRodando = False
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.jogando = False
                    self.estaRodando = False
                    
    def atualiza_sprites(self):
        self.todas_sprites.update()
        
    def desenha_sprites(self):
        self.tela.fill(consts.PRETO)
        self.todas_sprites.draw(self.tela)
        pygame.display.flip()
        
    def carregar_arquivos(self):
        diretorioImagens = os.path.join(os.path.join(os.getcwd()), '4.pacMan\images')
        self.diretorioSons = os.path.join(os.path.join(os.getcwd()), '4.pacMan\sounds')
        self.spritesheet = os.path.join(diretorioImagens, consts.SPRITESHEET)
        self.pacmanLogo = os.path.join(diretorioImagens, consts.LOGO)
        self.pacmanLogo = pygame.image.load(self.pacmanLogo).convert()
        
    def mostrarTexto(self, texto, tamanho, cor, x, y):
        #exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def mostrarLogo(self, x, y):
        #exibe o logo do jogo
        start_logo_rect = self.pacmanLogo.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.pacmanLogo, start_logo_rect)
    
    def mostrar_tela_inicial(self):
        pygame.mixer.music.load(os.path.join(os.path.join(self.diretorioSons, consts.MUSICA_START)))
        pygame.mixer.music.play()
        
        self.mostrarLogo(consts.LARGURA/2, 20)
        self.mostrarTexto("Pressione uma tecla para jogar", 
                          32, 
                          consts.AMARELO, 
                          consts.LARGURA/2, 
                          consts.ALTURA/2)
        pygame.display.flip()
        self.mostrarTexto("Feito por Brennin",
                            16,
                            consts.BRANCO,
                            consts.LARGURA/2,
                            570)
        
        pygame.display.flip()
        self.esperar_tecla()
        
    def esperar_tecla(self):
        #espera o jogador pressionar uma tecla para começar o jogo
        esperando = True
        while esperando:
            self.relogio.tick(consts.FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    esperando = False
                    self.estaRodando = False
                    pygame.quit()
                if evento.type == pygame.KEYUP:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorioSons, consts.TECLA_START)).play()
                    esperando = False  
    
    def mostrar_tela_final(self):
        pass
    
g = Game()
g.mostrar_tela_inicial()

while g.estaRodando:
    g.novoJogo()
    g.mostrar_tela_final()
    
#Vídeos incompletos na playlist do Joao Tinti #VoltaJoaoTinti