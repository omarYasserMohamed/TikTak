import pygame , sys
pygame.init()

win = pygame.display.set_mode((700 , 700))
pygame.display.set_caption("TIK TAK")
hitSound = pygame.mixer.Sound('hit.wav')


win.fill((205 , 255 , 10))

class Player:
	def __init__(self, x , y):
		self.x = x
		self.y = y
		self.velocity = 0.7
		self.score = 0
	def draw(self):
		pygame.draw.rect(win,(0,0,0),(self.x,self.y,15,60))
	def moveUp(self):
		if(self.y > 0):
			self.y = self.y - self.velocity
		pygame.draw.rect(win,(0,0,0),(self.x,self.y,15,60))
	def moveDown(self):
		if(self.y < 540 ):
			self.y = self.y + self.velocity
		pygame.draw.rect(win,(0,0,0),(self.x,self.y,15,60))



class Ball:
	def __init__(self):
		self.x = 70
		self.y = 70
		self.center = (self.x , self.y)
		self.directionInX = 1
		self.directionInY = 1
		self.velocity = 0.6
		self.vector = 0.8
	def draw(self):
		pygame.draw.circle(win , (250,0,0) , self.center , 8)
	def move(self):
		if(self.y < 0 or self.y > 600):
			if(gameFinished == False):
				hitSound.play()
			self.directionInY = self.directionInY * -1
			self.x = self.x + (self.velocity * self.vector * self.directionInX)
			self.y = self.y + (self.velocity * (1 - self.vector) * self.directionInY)
			self.center = (int(self.x) , int(self.y))
			pygame.draw.circle(win , (250,0,0) , self.center , 8)
			return 0
		elif(self.x < 0):

			self.x = 170
			self.y = 70
			self.center = (self.x , self.y)
			self.directionInX = 1
			self.directionInY = 1
			self.velocity = self.velocity * 1.01
			self.vector = 0.7
			pygame.draw.circle(win , (250,0,0) , self.center , 8)
			return 2
		elif(self.x > 700):

			self.x = 570
			self.y = 70
			self.center = (self.x , self.y)
			self.directionInX = -1
			self.directionInY = 1
			self.velocity = self.velocity * 1.01
			self.vector = 0.6
			pygame.draw.circle(win , (250,0,0) , self.center , 8)
			return 1

		else:
			self.x = self.x + (self.velocity * self.vector * self.directionInX)
			self.y = self.y + (self.velocity * (1 - self.vector) * self.directionInY)
			self.center = (int(self.x) , int(self.y))
			pygame.draw.circle(win , (250,0,0) , self.center , 8)
			return 0

	def hitPlayer(self):

		self.directionInX = -1 * self.directionInX
		self.directionInY = -1 * self.directionInY
		self.vector = self.vector  * 0.9
		self.x = self.x + (self.directionInX * self.velocity * self.vector)
		self.y = self.y + (self.velocity * (1 - self.vector) * self.directionInY)
		self.center = (int(self.x) , int(self.y))
		self.move()




playerOne = Player(670 , 10)
playerOne.draw()
playerTwo = Player(10 , 10)
playerTwo.draw()
ball = Ball()
ball.draw()

font = pygame.font.SysFont('comicsans' , 30, True)
endFont = pygame.font.SysFont('comicsans' , 40, True)
gameFinished = False
gameStarted = False
winner = ''


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	keys = pygame.key.get_pressed()
	if(gameStarted):
		if keys[pygame.K_UP]:
			win.fill((205 , 255 , 10))
			playerTwo.draw()
			ball.move()
			playerOne.moveUp()
		if keys[pygame.K_DOWN]:
			win.fill((205 , 255 , 10))
			playerTwo.draw()
			ball.move()
			playerOne.moveDown()
		if keys[pygame.K_w]:
			win.fill((205 , 255 , 10))
			playerOne.draw()
			ball.move()
			playerTwo.moveUp()
		if keys[pygame.K_s]:
			win.fill((205 , 255 , 10))
			ball.move()
			playerOne.draw()
			playerTwo.moveDown()
		win.fill((205 , 255 , 10))
		playerOne.draw()
		playerTwo.draw()
		if(int(playerOne.x) == int(ball.x) and playerOne.y <= ball.y <=  playerOne.y +60):
			if(gameFinished == False):
				hitSound.play()
			ball.hitPlayer()
		elif(int(playerTwo.x)+15 == int(ball.x) and playerTwo.y <= ball.y <=  playerTwo.y +60):
			if(gameFinished == False):
				hitSound.play()
			ball.hitPlayer()
		else:
			result = ball.move()
			if(result != 0):
				playerOne.velocity = playerOne.velocity *1.05
				playerTwo.velocity = playerTwo.velocity * 1.05

				if(result == 1):

					playerOne.score+= 1
					if(playerOne.score == 10):
						gameFinished = True
						if(len(winner) == 0):
							winner = winner + 'player1'

				else:
					playerTwo.score+= 1
					if(playerTwo.score == 10):
						gameFinished = True
						if(len(winner) == 0):
							winner = winner + 'player2'



			#print(ball.x , playerOne.x)
		pygame.draw.rect(win,(0,0,0),(0,600,700,5))
		text1 = font.render('player1 score: ' + str(playerOne.score) , 1 , (0,0,0))
		text2 = font.render('player2 score: ' + str(playerTwo.score) , 1 , (0,0,0))
		win.blit(text1 , (20, 650))
		win.blit(text2 , (490, 650))

		if(gameFinished):
			win.fill((205 , 255 , 10))
			gameOverText = endFont.render('GAME OVER', 1 , (0,0,0))
			win.blit(gameOverText , (290, 100))
			winnerText = endFont.render(winner + ' won', 1 , (0,0,0))
			win.blit(winnerText , (290, 300))
			seeYouText = endFont.render('see you', 1 , (0,0,0))
			win.blit(seeYouText , (310, 500))

	else:
		if keys[pygame.K_SPACE]:
			gameStarted = True
		win.fill((205 , 255 , 10))
		startText1 = endFont.render('use the W and S keys to move player1', 1 , (0,0,0))
		win.blit(startText1 , (10, 100))
		startText1 = endFont.render('use the UP and DOWN keys to move player2', 1 , (0,0,0))
		win.blit(startText1 , (10, 300))
		startText1 = endFont.render('press SPACE to start the game', 1 , (0,0,0))
		win.blit(startText1 , (10, 500))

	pygame.display.update()





pygame.quit()
