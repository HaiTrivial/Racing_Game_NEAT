import pygame
import math
race_track1 = pygame.image.load("Race_Track2.jpg")
car_img =pygame.transform.rotate(pygame.transform.scale( pygame.image.load("wagen.png"), (50,50)), 90)
startpunkt_x = 75
startpunkt_y = 35

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.min_speed = 0.2
        self.max_speed = 10
        self.speed = self.min_speed
        self.direction_vector = [1,0]
    def draw(self, screen):
        screen.blit(car_img, (self.x, self.y))


    def movement(self, events):
        #if events[pygame.K_UP] and self.speed < self.max_speed:
        #    self.speed += 0.2
        #if events[pygame.K_DOWN] and self.speed > self.min_speed:
        #    self.speed -= 0.2
        if events[pygame.K_LEFT]:
            if self.direction_vector[0] > 0  and self.direction_vector[1] >= 0:
                self.direction_vector[0] += 0.002
                self.direction_vector[1] -= 0.002
            elif self.direction_vector[0] > 0 and self.direction_vector[1] < 0:
                self.direction_vector[0] -= 0.002
                self.direction_vector[1] -= 0.002
            elif self.direction_vector[0] < 0 and self.direction_vector[1] > 0:
                self.direction_vector[0] += 0.002
                self.direction_vector[1] += 0.002
            else:
                self.direction_vector[0] -= 0.002
                self.direction_vector[1] += 0.002
        if events[pygame.K_RIGHT]:
            if self.direction_vector[0] > 0  and self.direction_vector[1] >= 0:
                self.direction_vector[0] -= 0.002
                self.direction_vector[1] += 0.002
            elif self.direction_vector[0] > 0 and self.direction_vector[1] < 0:
                self.direction_vector[0] += 0.002
                self.direction_vector[1] += 0.002
            elif self.direction_vector[0] < 0 and self.direction_vector[1] > 0:
                self.direction_vector[0] -= 0.002
                self.direction_vector[1] -= 0.002
            else:
                self.direction_vector[0] += 0.002
                self.direction_vector[1] -= 0.002
        self.x += self.direction_vector[0] * self.speed
        self.y += self.direction_vector[1] * self.speed
        print(self.direction_vector[0])
        print(self.direction_vector[1])

    def resetCar(self):
        self.speed = self.min_speed
        self.direction_vector[0] = 1
        self.direction_vector[1] = 0
        self.x = startpunkt_x
        self.y = startpunkt_y
    def check_for_Track(self):
        print(race_track1.get_at((int ( math.floor(self.x)),int ( math.floor(self.y)))))
        print(race_track1.get_at((int(math.floor(self.x+50)), int(math.floor(self.y)+50))))
        #or (0, 0, 0, 255) != race_track1.get_at((int(math.floor(self.x + 15)), int(math.floor(self.y + 15)))):
        if (0,0,0,255) != race_track1.get_at((int ( math.floor(self.x)),int ( math.floor(self.y+10)))):
            self.resetCar()


def fill_window(screen, car, events):
    #drawTrack
    screen.blit(race_track1, (0,0))
    car.draw(screen)
    car.movement(events)
    car.check_for_Track()
    pygame.display.update()

clock = pygame.time.Clock()
def run_game():

    pygame.init()

    clock = pygame.time.Clock()
    clock.tick(60)
    screen = pygame.display.set_mode((1024, 768))
    car1 = Car(startpunkt_x,startpunkt_y)
    run = True

    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        events = pygame.key.get_pressed()
        fill_window(screen, car1, events)
    pygame.quit()
    quit()
run_game()












