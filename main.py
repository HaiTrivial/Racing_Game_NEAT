import pygame
import math

from pygame.examples.go_over_there import screen

#TODO: click wehere to start -> while loop mit while startpunkt x/y none -> wenn click dann setze
#TODO: fix borders of car -> again -> make a bigger hit circle
# TODO make the impoting of a picture variable via drag and drop
#TODO fix Bug with out of picture collision
# Sensoren vom Auto die Daten an die AI liefern

'''
Setting Standard values for the Screen width and height 
'''

Screen_width = 1024
Screen_height = 768

'''importing pictures for racetrack and car'''

race_track1 = pygame.image.load("Race_Track2.jpg")
car_img =pygame.transform.rotate(pygame.transform.scale( pygame.image.load("wagen.png"), (50,50)), 90)
startpunkt_x = 75
startpunkt_y = 35

'''
Car class that manages all the car logic
@draw draws the current picture of the car onto the screen
@movement manages all the movement of the car -> like the tilt and speed 
'''

class Car:
    def __init__(self, x, y):
        self.x = x # x position of car
        self.y = y # y position of car
        self.min_speed = 0.2 # min speed car is able to drive
        self.max_speed = 0.4 # max speed car is able to drive
        self.speed = self.min_speed # current speed car is driving
        self.direction_vector = [1,0] # the ration the car is tilted in the direction of an aces. Ex : 1,0 is 100% oriented along the x-aces and 0% along the y-aces. So the driving direction is to the right
        self.original_car_image = car_img # the origninal car_img
        self.rotated_car_img =self.original_car_image # rotated car image
        self.current_rotation_car_pic = 0 # the rotation the car picture is tilted
        self.current_rotation_angle = 0 # the direction angle of the car
        self.car_rect = self.original_car_image.get_rect(center=(self.x, self.y)) #rect of the car image

    def draw(self, screen):
        screen.blit(self.rotated_car_img, self.car_rect.topleft) #(self.x, self.y)


    def movement(self, events):


        '''if events[pygame.K_LEFT]:
            self.current_rotation = self.current_rotation + 0.18

            #0.002
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
            self.current_rotation = self.current_rotation -0.18

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
                self.direction_vector[1] -= 0.002'''

        if events[pygame.K_UP] and self.speed < self.max_speed: # increase the speed until the max has been reached
            self.speed += 0.001
        if events[pygame.K_DOWN] and self.speed > self.min_speed: # decrease the speed until the min has been reached
            self.speed -= 0.001

        #another way to change the direction
        if events[pygame.K_LEFT]:
            self.current_rotation_angle = self.current_rotation_angle - 0.18
        if events[pygame.K_RIGHT]:
            self.current_rotation_angle = self.current_rotation_angle + 0.18

        #calculate new angle x with cos and y with sin
        self.direction_vector[0] = 1 * math.cos(math.radians(self.current_rotation_angle))
        self.direction_vector[1] = 1 * math.sin(math.radians(self.current_rotation_angle))

        self.x += self.direction_vector[0] * self.speed
        self.y += self.direction_vector[1] * self.speed
        self.rotate_image()

    def resetCar(self):
        self.speed = self.min_speed
        self.direction_vector[0] = 1
        self.direction_vector[1] = 0
        self.x = startpunkt_x
        self.y = startpunkt_y
        self.rotated_car_img = car_img
        self.car_rect  = self.original_car_image.get_rect(center=(self.x, self.y))
        self.current_rotation_angle = 0

    def inside_borders(self):
        if Screen_width <= self.car_rect.right -3:
            self.x = Screen_width - self.car_rect.width /2  - 3
            self.car_rect = self.original_car_image.get_rect(center=(self.x, self.y))
        if  0  >= self.car_rect.top +3:
            self.y = Screen_height - self.car_rect.height /2 + 3
            self.car_rect = self.original_car_image.get_rect(center=(self.x, self.y))
        if Screen_height <= self.car_rect.bottom -3:
            self.y = Screen_height - self.car_rect.height /2 - 3
            self.car_rect = self.original_car_image.get_rect(center=(self.x, self.y))



            #self.x = Screen_width -20

    def check_for_Track(self):
        self.inside_borders()
        #mache die hitbox quadratisch damit der tilt des Bildes nicht die relative Position des Hitbox ausrivhtung verändert
        print("Track")
        if (0,0,0,255) != race_track1.get_at((int ( math.floor(self.x)+(self.car_rect.width/2)),int ( math.floor(self.y)+(self.car_rect.width/2)))): #or (0, 0, 0, 255) != race_track1.get_at((int(math.floor(self.x + 20)), int(math.floor(self.y + 35)))):
            self.resetCar()

    def rotate_image(self):
        self.rotated_car_img = pygame.transform.rotate(self.original_car_image, - self.current_rotation_angle)
        self.original_car_image = car_img
        self.car_rect = self.rotated_car_img.get_rect(center=(self.x + 25, self.y +25))


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
    screen = pygame.display.set_mode((Screen_width, Screen_height))
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

# 0.002 * x = 1  <=> x = 500.0
# 0.18 gard pro move



#input for neat algorithm ...
#3 sensors one in driving direction and the other two in opposite 45 grad angels
#outputs 3 do nothing , move left , move left
#Avctivation function TanH
#pop size 50
#fitness Function -> distance traveled (what about loop? ) -> create finishline thetn maybe time to get to the finish line ?or multiple checkpoints .
#Idee für Fitness fkt vllt alle 5 sek ursprungsetzen und dann abstand nach 5 sek zu diesem Punkt messen ?
# vltt check point ? -> müssen auch gestezt werden ? path find algo ?
#max gen 50






