import pygame
caminho = input('\033[1;32mCola o caminho da musica:\n')
pygame.mixer.init()
pygame.mixer.music.load(caminho.replace('"',''))
pygame.mixer.music.play()
input("Pressione Enter para parar a música...\033[m")
pygame.mixer.music.stop()