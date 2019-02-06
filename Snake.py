import pygame, sys, random, time

pygame.init()

class Snake():

    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'right'
        self.changeDirectionTo = self.direction

    def changeDirect(self, direct):
        if direct == 'right' and self.direction is not 'left':
            self.direction = 'right'
        if direct == 'left' and self.direction is not 'right':
            self.direction = 'left'
        if direct == 'up' and self.direction is not 'down':
            self.direction = 'up'
        if direct == 'down' and self.direction is not 'up':
            self.direction = 'down'

    def move(self, foodPosiotion):
        if self.direction == 'right':
            self.position[0] += 10
        if self.direction == 'left':
            self.position[0] -= 10
        if self.direction == 'down':
            self.position[1] += 10
        if self.direction == 'up':
            self.position[1] -= 10
        self.body.insert(0, self.position[:])

        if self.position == foodPosiotion:
            return 1
        else:
            self.body.pop()
            return 0

    def checkColision(self):
        if self.position[0] > 500 or self.position[0] < 0:
            return 1
        elif self.position[1] > 500 or self.position[1] < 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0

class FoodGenerator():

    def __init__(self):
        self.position = [random.randrange(1,50) * 10, random.randrange(1,50) * 10]
        self.isFoodOnScreen = True

    def generateFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50) * 10, random.randrange(1,50) * 10]
            self.isFoodOnScreen = True
        return self.position

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()
score = 0

snake = Snake()
foodGenerator = FoodGenerator()
fontObj = pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 64)

def gameOver():
    text_render = fontObj.render("Score: " + str(score), True, (0, 0, 250))
    window.blit(text_render, (130, 150))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.changeDirect('down')
            if event.key == pygame.K_UP:
                snake.changeDirect('up')
            if event.key == pygame.K_LEFT:
                snake.changeDirect('left')
            if event.key == pygame.K_RIGHT:
                snake.changeDirect('right')

    foodPosition = foodGenerator.generateFood()

    if snake.move(foodPosition) == 1:
        score += 1
        foodGenerator.isFoodOnScreen = False

    window.fill((0, 0, 0))
    for posiotion in snake.body:
        pygame.draw.rect(window, pygame.Color(255, 0, 0), pygame.Rect(posiotion[0], posiotion[1], 10, 10))
    pygame.draw.rect(window, pygame.Color(0, 170, 0), pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

    if snake.checkColision() == 1:
        gameOver()

    pygame.display.set_caption("Game snake")
    pygame.display.flip()
    fps.tick(5 + score // 2)

