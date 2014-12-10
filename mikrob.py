__author__ = 'c.A.t'

import pygame

import sys

from random import *

from pygame.locals import *

pygame.init()

size = width, height = 1020, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('mIcrob v.2')



WHITE = 255, 255, 220
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
bakteria_color = Color(255, 0, 0, 255)

clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

screen.fill(WHITE)

class Mikrob:

    def __init__(self, pos=(width/2, height/2), body_lenght=10, genom='URDL'):
        self.x, self.y = __x, __y = pos
        self.body_lenght = self.initial_body = body_lenght
        self.body = [(__x, __y)]
        self.genom = genom
        self.energy = self.body_lenght * 10
        self.__body_builder()

    def update(self):
        self.energy -= 1
        self.__body_builder()
        if len(self.body) >= self.initial_body * 2:
            return self.division()



    def __body_builder(self):
        body_lenght = self.body_lenght

        if len(self.body) >= body_lenght:
            self.body.pop()


        while len(self.body) != body_lenght:
            __x, __y = self.body[0]
            print self.energy
            rand = randint(0, len(self.genom)-1)
            gen = self.genom[rand]
            if gen == 'U':
                __y -= 1
            elif gen == 'R':
                __x += 1
            elif gen == 'D':
                __y += 1
            elif gen == 'L':
                __x -= 1

            __pos = (__x, __y)

            if __pos not in self.body:
                self.body = [(__x, __y)] + self.body
            else:
                pass

        self.body_lenght = len(self.body)

    def eat(self, scr, bakterias):
        for i in range(len(self.body)):
            if scr.get_at(self.body[i]) == bakteria_color:
                for bakteria in bakterias:
                    __x,__y = self.body[i]
                    if bakteria.x == __x and bakteria.y == __y:
                        bakterias.remove(bakteria)
                        self.body_lenght += 1
                        self.energy += 10
                        print str(self.body_lenght) + " " + str(len(self.body))

    def display(self, scr, pixCol):
        for i in range(len(self.body)):
             scr.set_at(self.body[i], pixCol)

    def division(self):
        self.body_lenght /= 2
        new_body = self.body[len(self.body)/2:]
        self.body = self.body[:len(self.body)/2]
        new_mirkrob = Mikrob(new_body[0], len(new_body), self.genom)
        return new_mirkrob


class Bacteria:
    def __init__(self, x=width/2, y=height/2):
        self.x = x
        self.y = y

    def step(self):
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)

    def display(self, scr, pixCol):
        scr.set_at((self.x, self.y), pixCol)




bakterias = []
mikrobs = [Mikrob((width/2, height/2), 2, 'LUDR')]

for i in range(3000):
    bak = Bacteria(randint(0, width), randint(0, height))
    bakterias += [bak]


while  True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    screen.blit(background, (0, 0))

    for bakteria  in bakterias:
        bakteria.step()
        bakteria.display(screen, RED)

    for mikrob in mikrobs:

        mikrob.eat(screen, bakterias)
        new = mikrob.update()
        mikrob.display(screen, BLACK)
        if new:
            mikrobs.append(new)

    pygame.display.update()
    #clock.tick(1)


