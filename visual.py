import pygame
import sys
import generator as tg
import threading
import random

# ---------------- START SIMULATION THREADS ----------------
threading.Thread(target=tg.light_changer, daemon=True).start()
threading.Thread(target=tg.generator, daemon=True).start()
threading.Thread(target=tg.traversal, daemon=True).start()

# ---------------- PYGAME INIT ----------------
pygame.init()
WIDTH, HEIGHT = 1280, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulation")

clock = pygame.time.Clock()
FPS = 60

# ---------------- LOAD ASSETS ----------------
road = pygame.image.load("road.png")

car_imgs = [
    pygame.transform.scale(pygame.image.load("Car1.png"), (40, 70)),
    pygame.transform.scale(pygame.image.load("Car2.png"), (40, 70))
]

# ---------------- LANE COORDINATES ----------------
# Approximate positions based on your diagram
LANE_POSITIONS = {
    "AL3": (620, 0),
    "AL2": (650, 0),

    "BL3": (580, 680),
    "BL2": (610, 680),

    "CL3": (1280, 340),
    "CL2": (1280, 370),

    "DL3": (0, 300),
    "DL2": (0, 330),
}

# ---------------- DRAW TRAFFIC LIGHTS ----------------
def draw_lights():
    colors = {
        "GREEN": (0, 255, 0),
        "RED": (255, 0, 0)
    }

    pygame.draw.circle(screen, colors[tg.LaneA_light], (640, 160), 10)
    pygame.draw.circle(screen, colors[tg.LaneB_light], (640, 560), 10)
    pygame.draw.circle(screen, colors[tg.LaneC_light], (900, 360), 10)
    pygame.draw.circle(screen, colors[tg.LaneD_light], (380, 360), 10)

# ---------------- DRAW CARS ----------------
def draw_cars():
    for lane, queue in tg.lane.items():
        if lane in LANE_POSITIONS:
            x, y = LANE_POSITIONS[lane]
            for i, _ in enumerate(list(queue)[:5]):
                car = random.choice(car_imgs)
                screen.blit(car, (x, y + i * 45))

# ---------------- MAIN LOOP ----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(road, (0, 0))
    draw_lights()
    draw_cars()

    pygame.display.update()
    clock.tick(FPS)


if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        tg.paused = not tg.paused
        print("Paused" if tg.paused else "Resumed")

