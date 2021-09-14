import pygame

WHITE = (255,255,255)
BLACK = (0, 0, 0)
WIDTH = 600
HEIGHT = 400

def scale_image(name, scale):
    return pygame.transform.scale(name, (int(name.get_width()*scale), int(name.get_height()*scale)))
def load_image(name):
    return pygame.image.load("Imgs/"+name+".png")
def load_images(name, nbrImgs):
    lst = []
    for i in range(nbrImgs):
        img = pygame.image.load("Imgs/"+name+str(i)+".png")
        lst.append(img)
    return lst
def scale_list_images(list_images, scale):
    lst = []
    for item in list_images:
        for i in range(scale):
            lst.append(item)
    return lst
def text_to_screen(screen, text, x, y, size = 40, color = BLACK, font_type = 'Early GameBoy.ttf'):
    text = str(text)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
def load_sound(name):
    return pygame.mixer.Sound("Sounds/"+name+".wav")
def play_sound(sound):
    pygame.mixer.Sound.play(sound)

