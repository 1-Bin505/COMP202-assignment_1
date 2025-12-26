import pygame
import sys
import threading
import random
import generator as tg
from collections import deque

threading.Thread(target=tg.light_changer, daemon=True).start()
threading.Thread(target=tg.generator, daemon=True).start()
threading.Thread(target=tg.traversal, daemon=True).start()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Traffic Simulation")
clock = pygame.time.Clock()

road_img = pygame.image.load("Road.png").convert()
car_imgs = [
    pygame.transform.scale(pygame.image.load("Car1.png"), (30, 60)),
    pygame.transform.scale(pygame.image.load("Car3.png"), (30, 60))
]


class VisualCar:
    def __init__(self, image, path, road):
        self.image = image
        self.path = path
        self.road = road
        self.x, self.y = path[0]
        self.index = 0
        self.speed = 3
        self.done = False

    def update(self):
        if self.index >= len(self.path) - 1:
            self.done = True
            return True

      
        if self.index == 1:
            light = getattr(tg, f"Lane{self.road}_light")
            if light == "RED":
                return False

        tx, ty = self.path[self.index + 1]
        dx, dy = tx - self.x, ty - self.y
        dist = (dx**2 + dy**2)**0.5

        if dist > self.speed:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
        else:
            self.x, self.y = tx, ty
            self.index += 1
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))


PATHS = {
    ("AL3", "CL1"): [(640, -60), (640, 280), (640, 360), (640, 720)],
    ("AL2", "BL1"): [(680, -60), (680, 280), (640, 360), (360, 360), (-80, 360)],
    ("BL3", "DL1"): [(640, 780), (640, 430), (640, 360), (640, -80)],
    ("BL2", "AL1"): [(600, 780), (600, 430), (640, 360), (920, 360), (1340, 360)],
    ("CL3", "BL1"): [(-60, 360), (280, 360), (360, 360), (640, 360)],
    ("CL2", "DL1"): [(-60, 400), (280, 400), (360, 360), (640, 360), (640, -80)],
    ("DL3", "AL1"): [(1280 + 60, 360), (1000, 360), (920, 360), (640, 360)],
    ("DL2", "CL1"): [(1280 + 60, 320), (1000, 320), (920, 360), (640, 360), (640, 720)],

}

active_cars = []


LIGHT_POS = {
    "A": (600, 300),
    "B": (660, 430),
    "C": (680, 360),
    "D": (580, 360),
}

def draw_lights():
    for road, pos in LIGHT_POS.items():
        color = (0, 255, 0) if getattr(tg, f"Lane{road}_light") == "GREEN" else (255, 0, 0)
        pygame.draw.circle(screen, color, pos, 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            tg.paused = not tg.paused

    screen.blit(road_img, (0, 0))

   
    while tg.move_events:
        src, dst = tg.move_events.popleft()
        if (src, dst) in PATHS:
            path = PATHS[(src, dst)]
            img = random.choice(car_imgs)
            road = src[0]  # A/B/C/D
            active_cars.append(VisualCar(img, path, road))


    for car in active_cars[:]:
        if car.update():
            active_cars.remove(car)
        car.draw(screen)

  
    draw_lights()

    pygame.display.update()
    clock.tick(60)
