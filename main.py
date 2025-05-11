import pygame
race_track1 = pygame.image.load("Race_Track2.jpg")
car_img =pygame.transform.rotate(pygame.transform.scale( pygame.image.load("wagen.png"), (50,50)), 90)

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
    def draw(self, screen):
        screen.blit(car_img, (self.x, self.y))


    def movement(self):
        pass # hier weiter machen


def fill_window(screen, car):
    #drawTrack
    screen.blit(race_track1, (0,0))
    car.draw(screen)
    pygame.display.update()


def run_game():

    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    car1 = Car(0,0)
    run = True

    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        fill_window(screen, car1)
    pygame.quit()
    quit()
run_game()


















