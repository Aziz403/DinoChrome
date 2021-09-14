from Tools import *
from random import randint
from pygame.locals import *

class Dino():
    Down = False
    FirstJump = False
    def __init__(self, posX, posY, Screen):
        self.posX = posX
        self.posY = posY
        self.Images = load_images("dinossaur", 3)
        self.Images = scale_list_images(self.Images, 5)
        self.ImageId = 0
        self.Image = scale_image(self.Images[self.ImageId], 2)
        self.Screen = Screen
        self.JumpSound = load_sound("jump_sound")
        self.IsJump = False

    def Draw(self):
        self.Screen.blit(self.Image, [self.posX, self.posY])
    def Update(self):
        if self.ImageId == 3*5:
            self.ImageId = 0
        self.Image = scale_image(self.Images[self.ImageId], 2)
        self.ImageId += 1
        if self.IsJump:
            self.Jump()

    def Jump(self):
        if Dino.FirstJump:
            play_sound(self.JumpSound)
            Dino.FirstJump = False
        if (291 > self.posY > 170) and not Dino.Down:
            self.posY -= 2.5
        if self.posY < 171:
            Dino.Down = True
        if Dino.Down:
            self.posY += 2.5
        if self.posY > 290:
            self.posY = 290
            self.IsJump = False
            Dino.Down = False


class Cloud():
    def __init__(self, posX, Screen):
        self.posX = posX
        self.posY = randint(20, 190)
        self.Image = load_image("cloud")
        self.Screen = Screen
        self.Spped = randint(5, 20)/10
    def Draw(self):
        self.Screen.blit(self.Image, [self.posX, self.posY])
    def Update(self):
        self.posX -= self.Spped
        if self.posX < -40:
            self.posX = 600
            self.posY = randint(20, 190)


class Obstacle():
    DipartScoure = 10
    def __init__(self, Speed, posX, Screen):
        self.Image = load_image("obstacle")
        scale = randint(10, 20) / 10
        self.Image = scale_image(self.Image, scale)
        self.posX = posX + randint(5, 50)
        self.posY = 345 - self.Image.get_height()
        self.Screen = Screen
        self.Speed = Speed
    def Draw(self):
        self.Screen.blit(self.Image, [self.posX, self.posY])
    def Update(self):
        self.posX -= self.Speed
        if self.posX < -60:
            self.Image = load_image("obstacle")
            scale = randint(10, 20) / 10
            self.Image = scale_image(self.Image, scale)
            self.posY = 345 - self.Image.get_height()
            self.posX = randint(600, 1000)


class Bird():
    DipartScoure = 200
    def __init__(self, posX, Screen):
        self.posX = posX
        self.posY = randint(200, 270)
        self.Images = load_images("fly_dino", 2)
        self.Images = scale_list_images(self.Images, 7)
        self.ImageId = 0
        self.Image = scale_image(self.Images[self.ImageId], 2)
        self.Screen = Screen
        self.Speed = randint(15, 30)/10
    def Draw(self):
        self.Screen.blit(self.Image, [self.posX, self.posY])
    def Update(self):
        self.posX -= self.Speed
        if self.posX < -40:
            self.posX = randint(600, 1000)
            self.posY = randint(200, 290)
        if self.ImageId == 2 * 7:
            self.ImageId = 0
        self.Image = scale_image(self.Images[self.ImageId], 2)
        self.ImageId += 1


class Earth():
    def __init__(self, Screen ,Speed):
        self.Move = 0
        self.Image = load_image("floor")
        self.Image = scale_image(self.Image, 2)
        self.Screen = Screen
        self.Speed = Speed
    def Draw(self):
        for x in range(0, 64):
            self.Screen.blit(self.Image, [self.Move + (x * 64), 300])
    def Update(self):
        if self.Move < -1200:
            self.Move = 0
        self.Move -= self.Speed


class Game():
    FirstTimeGameOver = False
    def __init__(self, Width, Height):

        self.Width = Width
        self.Height = Height
        self.Clock = pygame.time.Clock()
        self.Screen = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption("T-Rex Chrome")
        self.Score = 0
        self.Speed = 2

        self.DeathSound = load_sound("death_sound")
        self.ScoreUpSound = load_sound("score_sound")

        self.Earth = Earth(self.Screen, self.Speed)

        self.Dino = Dino(50, 290, self.Screen)

        self.Clouds = []
        self.Clouds.append(Cloud(400, self.Screen))
        self.Clouds.append(Cloud(800, self.Screen))
        self.Clouds.append(Cloud(1500, self.Screen))

        self.Bird = Bird(700, self.Screen)

        self.Obstacles = []
        self.Obstacles.append(Obstacle(self.Speed, 600, self.Screen))
        self.Obstacles.append(Obstacle(self.Speed, 900, self.Screen))
        self.Obstacles.append(Obstacle(self.Speed, 920, self.Screen))

        self.Start = False
        self.Pause = False
        self.Over = False

    def Draw(self):
        self.Screen.fill(WHITE)

        self.Earth.Draw()

        self.Dino.Draw()

        for cloud in self.Clouds:
            cloud.Draw()

        if self.Score > Bird.DipartScoure:
            self.Bird.Draw()

        if self.Score > Obstacle.DipartScoure:
            for obstacle in self.Obstacles:
                obstacle.Draw()

    def Update(self):
        if self.Start:
            self.Clock.tick(60)

            self.Earth.Update()

            self.Dino.Update()

            for cloud in self.Clouds:
                cloud.Update()

            if self.Score > Bird.DipartScoure:
                self.Bird.Update()

            if self.Score > Obstacle.DipartScoure:
                for obstacle in self.Obstacles:
                    obstacle.Update()

            if (self.Score % 100)==1:
                play_sound(self.ScoreUpSound)

            self.Score += 0.2
            self.Start = not self.IsClash()
            self.Over = not self.Start
            if self.Over:
                Game.FirstTimeGameOver = self.Over
            text_to_screen(self.Screen, "Score : "+str(int(self.Score)), 10, 30, 15, BLACK)
            text_to_screen(self.Screen, "Entre 'R' To Restart Game", 10, 50, 11, BLACK)
            text_to_screen(self.Screen, "Entre 'P' To Pause Game", 10, 65, 11, BLACK)


        elif self.Over:
            text_to_screen(self.Screen, "Game Over", 200, 155, 22, BLACK)
            text_to_screen(self.Screen, "Entre 'R' To Reset Game", 155, 190, 12, BLACK)
            if Game.FirstTimeGameOver:
                play_sound(self.DeathSound)
                Game.FirstTimeGameOver = False

        elif not self.Start and not self.Pause:
            text_to_screen(self.Screen, "Entre 'Space' To Play The Game", 90, 150, 15, BLACK)

        elif self.Pause:
            text_to_screen(self.Screen, "Entre 'Space' To Contine Your Game", 60, 150, 15, BLACK)

    def IsClash(self):
        for item in self.Obstacles:
            if (self.Dino.posY < item.posY < (self.Dino.posY + self.Dino.Image.get_height())) and (
                    self.Dino.posX < item.posX < self.Dino.Image.get_width()):
                return True
        if (self.Dino.posY < self.Bird.posY < (self.Dino.posY + self.Dino.Image.get_height())) and (
                self.Dino.posX < self.Bird.posX < self.Dino.Image.get_width()):
            return True
        return False






