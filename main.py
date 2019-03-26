class player():
	"""docstring for player"""
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, (self.x,self.y))

	def move(self):
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_LEFT]:
			self.x -=10
			# print("left"+str(self.x))
			self.draw(screen)
		elif pressed[pygame.K_RIGHT]:
			self.x+=10	
			# print("right"+str(self.x))
			self.draw(screen)
		elif pressed[pygame.K_UP]:
			self.y-=10	
			# print("up"+str(self.y))
			self.draw(screen)
		elif pressed[pygame.K_DOWN]:
			self.y+=10	
			# print("down"+str(self.y))
			self.draw(screen)

		return(self.x, self.y)

# class tile():
# 	"""docstring for tile"""
# 	def __init__(self, tile):
# 		self.tile = tile
# 	def draw(surface, x, y):
# 		surface.blit(self.tile, (self.x,self.y))
# 	#include tile properties


class level():
	"""docstring for level"""
	def __init__(self, level_matrix, tile, tileX, tileY):
		self.level_matrix = level_matrix
		self.tile = tile
		self.tileX = tileX
		self.tileY = tileY

	def draw(self, tileX, tileY):
		screen.blit(self.tile, (tileX,tileY))
	#include tile properties

	def render_level(self):
		tileX = 0
		tileY = 0

		for row in self.level_matrix:
			for item in row:
				# print (item)
				self.draw(tileX, tileY)
				tileX+=50
			tileX = 0
			tileY+=50


"""This is where my program starts """
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False



one =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]



myimage = pygame.image.load("myimage.png")
mytile = pygame.image.load("tile.png")
		


bob=player(myimage,30,9) #player
bob.draw(screen)




level_one = level(one, mytile,0,0) #level




while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	level_one.render_level()

	#screen.fill((0,0,255))
	temp_coor = bob.move()
	bob=player(myimage,temp_coor[0],temp_coor[1])
	bob.draw(screen)


	pygame.display.flip()