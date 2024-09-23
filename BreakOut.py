# import pygame
# import random
# from random import randint
# import random as r  # r points at random
# from random import randint # imports randint directly, its a function in our file now
# pygame.init()
#
# screen = pygame.display.set_mode((1280,720))
#
# clock = pygame.time.Clock()
#
# class Player(pygame.Rect):
#
#     def __init__(self, x, y):
#         super().__init__(x, y, 100, 25)   # arbitrary values TODO tweak
#         self.vx = 0
#
#     def draw(self):
#         pygame.draw.rect(screen, 'orange', self, 0) # fill
#         pygame.draw.rect(screen, 'black', self, 1)   # outline
#
#     def update(self):
#         self.x += self.vx
#         if self.x < 0:
#             self.x = 0
#         elif self.x + self.width > screen.get_width():
#             self.x = screen.get_width() - self.width
#
# class Ball(pygame.Rect):
#
#     def __init__(self, x, y, diameter):
#         super().__init__(x, y, diameter, diameter)
#         self.vx = random.randint(3, 6) * random.choice([1, -1])
#         self.vy = random.randint(3, 4) # TODO tweak?
#
#     def draw(self):
#         pygame.draw.ellipse(screen, 'white', self, 0)
#
#
#     def update(self):
#         self.x += self.vx
#         self.y += self.vy
#         if (self.right >= screen.get_width() and self.vx > 0) or (self.left <= 0 and self.vx <= 0):
#             self.vx = -self.vx
#         if self.bottom <= 0 and self.vy < 0:
#             self.vy = - self.vy
#         if (self.top >= screen.get_height() and self.vy > 0 ):
#             self.vy = - self.vy
#
#
#
#
#     def colliderect(self, rect):
#         # if ball land in the player
#         if pygame.Rect.colliderect(self.ball.rect, self.playerA.rect):
#             self.ball.direction = "right"
#         if pygame.Rect.colliderect(self.ball.rect, self.playerB.rect):
#             self.ball.direction = "left"
#         player.update()
#         ball.update()
#         if ball.colliderect(player):
#             ball.vy = -1
#             ball.y = player.y - ball.width
#         if pygame.Rect.colliderect(self.ball.rect, self.bricks.rect):
#             self.ball.direction = "right"
#         if pygame.Rect.colliderect(self.ball.rect, self.bricks.rect):
#             self.ball.direction = "left"
#         if ball.colliderect(bricks):
#             ball.vy = -ball.vy
#             ball.vx = -ball.vx
#             ball.y = player.y - ball.width
#
#
#
# class bricks(pygame.Rect):
#
#
#     # def __init__(self,  x, y, diameter):
#     #     self.randRed = random.randint(1,255)
#     #     self.randGreen = random.randint(1, 255)
#     #     self.randBlue = random.randint(1, 255)
#     #
#     #
#     # def draw(self):
#     #     pygame.draw.rect(screen, (self.randRed,self.randGreen,self.randBlue), self, 0)  # fill
#     #     pygame.draw.rect(screen, (self.randRed,self.randGreen,self.randBlue), self, 1)  # outline
#     WIDTH = 80
#     HEIGHT = 20
#
#     def __init__(self, x, y):
#         super().__init__(x, y, self.WIDTH, self.HEIGHT)
#         self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
#     def draw(self):
#         pygame.draw.rect(screen, self.color, self, 0)
#
#
#
#
#
#
#
# player = Player(screen.get_width()/2 - 50, screen.get_height() - 50)
# ball = Ball(screen.get_width()/2 - 10, screen.get_height()/2 +20, 20)
#
# while True:
#     # Process player inputs.
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_a:
#                 player.vx += -6
#             elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#                 player.vx += 6
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_a:
#                 player.vx += 6
#             elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#                 player.vx += -6
#
#     # Do logical updates here.
#     player.update()
#     ball.update()
#     #ball player intersection
#     if player.colliderect(ball):
#         ball.vy *= -1
#
#     screen.fill('grey')  # Fill the display with a solid color
#     # Render the graphics here.
#     brickList = []
#     n =0
#     while(n<5):
#         brick = bricks(n*140, 40)
#         brickList.append(brick)
#         n+= 1
#
#     player.draw()
#     ball.draw()
#     for b in brickList:
#         b.draw()
#
#     pygame.display.flip()  # Refresh on-screen display
#     clock.tick(60)         # wait until next frame (at 60 FPS)
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
class Player(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 400, 25)   # arbitrary values
        self.vx = 0
        bear_image = pygame.image.load('bear.png')



    def draw(self):
        pygame.draw.rect(screen, 'orange', self, 0)  # fill
        pygame.draw.rect(screen, 'black', self, 1)   # outline

    def update(self):
        self.x += self.vx
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > screen.get_width():
            self.x = screen.get_width() - self.width


class Ball(pygame.Rect):
    def __init__(self, x, y, diameter):
        super().__init__(x, y, diameter, diameter)
        self.vx = random.randint(3, 6) * random.choice([1, -1])
        self.vy = random.randint(3, 4)

    def draw(self):
        pygame.draw.rect(screen, 'white', self, 0)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # Bounce off walls
        if self.right >= screen.get_width() or self.left <= 0:
            self.vx = -self.vx
        if self.top <= 0:
            self.vy = -self.vy

    def handle_collision(self, rect):
        if self.colliderect(rect):
            self.vy *= -1  # reverse vertical direction


class Brick(pygame.Rect):
    WIDTH = 80
    HEIGHT = 20

    def __init__(self, x, y):
        super().__init__(x, y, self.WIDTH, self.HEIGHT)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.rect(screen, self.color, self, 0)


# Initialize objects
player = Player(screen.get_width() / 2 - 50, screen.get_height() - 50)
ball = Ball(screen.get_width() / 2 - 10, screen.get_height() / 2 + 20, 20)

# Create brick layout (done once outside the game loop)
brick_list = []
for row in range(5):
    for col in range(10):
        brick = Brick(col * (Brick.WIDTH + 10) + 10, row * (Brick.HEIGHT + 10) + 40)
        brick_list.append(brick)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                player.vx = -6
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                player.vx = 6
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d]:
                player.vx = 0

    # Update objects
    player.update()
    ball.update()

    # Ball and player collision
    ball.handle_collision(player)

    # Ball and brick collision
    for brick in brick_list[:]:
        if ball.colliderect(brick):
            ball.handle_collision(brick)
            brick_list.remove(brick)  # Remove the brick when hit

    # Draw everything
    screen.fill('grey')
    player.draw()
    ball.draw()

    for brick in brick_list:
        brick.draw()

    pygame.display.flip()
    clock.tick(60)

