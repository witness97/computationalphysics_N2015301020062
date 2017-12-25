#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:32:30 2017

@author: wangshiru
"""

import pygame, random, sys
from pygame.locals import *
pygame.init()
size = 640, 400
screen = pygame.display.set_mode(size)
bg = (0,0,0)
font = pygame.font.Font(None,20)

class Snake:
    position = [(16,10),(17,10),(18,10),(19,10),(20,10)]
    speed = (-1,0)
    score = 0
    color = 255,248,220
    def move(self):
        head = self.position[0][0] + self.speed[0], self.position[0][1] + self.speed[1]
        self.position.insert(0,head)
        self.position.pop()
    def eat(self):
        head = self.position[0][0] + self.speed[0], self.position[0][1] + self.speed[1]
        self.position.insert(0, head)
        self.score += 1
    def panduan_die(self):
        head = self.position[0]
        if (head in self.position[1:]) or (not 1<= head[0] <= 32) or (not 1<= head[1] <= 20):
            sys.exit()
    def turn(self,m):
        if m == K_LEFT:
            self.speed = (-1,0)
        if m == K_RIGHT:
            self.speed = (1, 0)
        if m == K_UP:
            self.speed = (0,-1)
        if m == K_DOWN:
            self.speed = (0,1)

class Food:
    pp = [(i,j) for i in range(1,33) for j in range(1,21)]
    def __init__(self,position):
        pp = self.pp[:]
        for each in position:
            pp.remove(each)
        self.wei = random.choice(pp)


snake = Snake()
food = Food(snake.position)
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            snake.turn(event.key)
    if (snake.position[0][0]+snake.speed[0],snake.position[0][1]+snake.speed[1])\
            == food.wei:
        snake.eat()
        food = Food(snake.position)
    else:
        snake.move()
        snake.panduan_die()
    screen.fill(bg)
    for each in snake.position:
        position = (each[0]-1)*20 , (each[1]-1)*20
        rect = pygame.Rect(position[0],position[1],20,20)
        screen.fill(snake.color,rect)
    position = (food.wei[0]-1)*20, (food.wei[1]-1)*20
    rect  = pygame.Rect(position[0],position[1],20,20)
    screen.fill((0,255,0),rect)
    screen.blit(font.render('score:'+str(snake.score),True,(255,255,255)),(400,0))
    pygame.display.flip()
    pygame.time.delay(200)