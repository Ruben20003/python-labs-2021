import numpy as np
import pygame
import random
import math

class Ball:
    def __init__(self, sides, r=8, color=(128, 128, 128), score=None, koldunov_orz=0):
        """
        sides - array of size 2, containing lengths of the sides of the display in pixels.
        r(int or float or tuple/list/np.array (a, b))=10 -
            if int/float is passed, then the ball is drawn with radius r
            if list/np.array/tuple (a, b) is passed, then the ball is drawn with random radius
            from interval a to b.
        color - tuple (R,G,B) containing color of the ball
        score - int/float/None
            if int/float is passed, then it contains the bounty of the ball.
            if None is passed, then the score is calculated by the formula score=round(100/r).
        koldunov_orz - int, containing 1 if self should render as Koldunov, containing 0 else.
        """
        self.coords = np.random.randint(0, sides, size=(2)).astype(float)
        self.velocity = (0, 0)
        while self.velocity[0] * self.velocity[0] + self.velocity[1] + self.velocity[1] < 10. * 10.:
            self.velocity = np.random.randint(-50, 50, size=(2)).astype(float)

        self.color = color

        if type(r) in (tuple, list, np.array):
            self.r = random.uniform(r[0], r[1])

        if score is None:
            self.score = np.round(30 / self.r)
        else:
            self.score = score

        self.koldunov_orz = koldunov_orz
        if self.koldunov_orz == 1:
            self.orientation = 0

        self.is_alive = True

    def move(self, dt=1):
        """
        Ball.move(dt=1)
        returns - None

        Updates balls coordinates by time dt
        dt(int or float) - value of variable of evolution
        """
        self.coords += self.velocity * dt

    def collision(self, sides):
        """
        Ball.collision(sides)
        returns - None
        Calculates the collision of the ball with sides
        sides(np.array of shape (2,) and type float or int) - the sides of the display.
        """
        for i in (0, 1):
            if np.abs(self.coords[i] - sides[i] / 2) >= sides[i] / 2 - self.r:
                self.coords[i] = self.r if self.coords[i] <= self.r else sides[i] - self.r
                self.velocity[i] *= -1

    def click(self, mouse_coords):
        """
        Ball.click(mouse_coords)
        returns - int
        Checks if ball is clicked
        mouse_coords(np.array of shape (2,) and type float or int) - x, y coordinates of mouse
        returns the amount of score recieved for the click (determinend by Ball.score variable)
        """
        if self.is_alive and np.linalg.norm(self.coords - mouse_coords) <= self.r:
            self.is_alive = False
            return self.score

        return 0

    def render(self, surface):
        """
        Ball.render(surface)
        returns - None
        Renders ball on the surface.
        surface(pygame.Surface) - surface to be rendered on
        """
        if self.is_alive:
            if self.koldunov_orz == 0:
                pygame.draw.circle(surface, self.color, self.coords, self.r)
            else:
                koldunov = pygame.image.load('koldunov.jpg')
                koldunov.set_colorkey((0,0,0))
                koldunov = koldunov.convert_alpha()
                correct_scale = 2 * self.r
                correct_scale *= (abs(math.sin(self.orientation)) +
                                  abs(math.cos(self.orientation)))
                correct_scale = math.ceil(2 * self.r / correct_scale)
                correct_scale = math.ceil(self.r)
                koldunov = pygame.transform.scale(koldunov, (correct_scale, correct_scale));
                self.orientation += 2
                koldunov = pygame.transform.rotate(koldunov, self.orientation);
                display.blit(koldunov, self.coords - (self.r, self.r))
                #pygame.draw.circle(surface, (199,36,177), self.coords, 20)

COLORS = [(156, 152, 47), (116, 193, 232), (232, 227, 93), (2, 2, 2), (158, 11, 26), (8, 56, 8), (14, 158, 93)]
COLORS_N = len(COLORS)

esh = 'eshutyun_gyotutyun_eshutyun'
def update_leaderboard(score):
    print(f'Finished. Final score {score}.')
    name = input('Enter your name to save in leaderboard: ')
    with open(esh, 'a') as file:
        file.write(f"{name:<20}: {score}\n")

pygame.init()

FPS = 30
SIDES = [1690, 690]

display = pygame.display.set_mode(SIDES)

pygame.display.update()
clock = pygame.time.Clock()
gameover = False

BALL_COUNT = 8
pool = [Ball(SIDES, r=(20, 50), color=random.choice(COLORS))
        for _ in range(BALL_COUNT)]
pool.append(Ball(SIDES, r=(20, 30), color=random.choice(COLORS), score=69, koldunov_orz=1));
pool.append(Ball(SIDES, r=(40, 70), color=random.choice(COLORS), score=69, koldunov_orz=1));

score = 0
penalty = 3
balls_left = BALL_COUNT

frames = 0
while frames <= 25 * FPS and not gameover:
    frames += 1
    clock.tick(FPS)
    for ball in pool:
        ball.render(display)
        ball.move(4. / FPS)
        ball.collision(SIDES)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, ball in enumerate(pool):
                d_score = ball.click(np.array([x, y]))
                if d_score > 0:
                    score += d_score
                    ball.render(display)
                    pygame.display.update()

                    balls_left -= 1
                    print(f'Կպար, քունած բուլզայ!  score: {score}')
                    pool.pop(i)
                    break
            else:
                score -= penalty
                print(f'Ծուռ էշի մեկը, դու գյոթ ես, միավորներդ նախույ եմ անում! score: {score}')

    if event.type == pygame.QUIT:
        gameover = True
    pygame.display.update()
    display.fill((232, 70, 86))

    if balls_left == 0:
        pygame.quit()
        gameover = True
        update_leaderboard(score)
pygame.quit()
