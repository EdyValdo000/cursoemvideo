import pygame
caminho = input('Cola o caminho da musica:\n')
pygame.mixer.init()
pygame.mixer.music.load(caminho.replace('"',''))
pygame.mixer.music.play()
input("Pressione Enter para parar a música...")
pygame.mixer.music.stop()