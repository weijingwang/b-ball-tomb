class player():
	"""docstring for player"""
	def __init__(self, image, x, y,tileBoxes):
		self.image = image
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.rect = pygame.Rect(self.x, self.y, 49, 49)
		self.tileBoxes = tileBoxes
	def draw(self, surface):
		player = surface.blit(self.image, (self.x,self.y))
		
		return self.rect

	def move(self):
		pressed = pygame.key.get_pressed()
		self.draw(screen)
		if pressed[pygame.K_LEFT]:
			self.dx = -10
			self.x +=self.dx
			# print("left"+str(self.x))
			self.draw(screen)
		elif pressed[pygame.K_RIGHT]:
			self.dx = 10
			self.x +=self.dx	
			# print("right"+str(self.x))
			self.draw(screen)
		elif pressed[pygame.K_UP]:
			self.dy = -10
			self.y +=self.dy
			# print("up"+str(self.y))
			self.draw(screen)
		elif pressed[pygame.K_DOWN]:
			self.dy = 10
			self.y +=self.dy
			# print("down"+str(self.y))
			self.draw(screen)

		if self.rect.colliderect(self.tileBoxes[1]):
			print("out")
			return "done"

		for wall in self.tileBoxes[0]:
			if self.rect.colliderect(wall):
				if self.dx > 0:
					self.rect.right = wall.left
					print("left")
					self.x = wall[0]+100
				elif self.dx < 0:
					self.rect.left = wall.right
					print("r")
					self.x = wall[0]+50
				elif self.dy > 0:
					self.rect.bottom = wall.top
					print("t")
					self.y = wall[1]-50
				elif self.dy < 0:
					self.rect.top = wall.bottom
					print("b")
					self.y = wall[1]+50
					

		# elif playerRect.colliderect(otherRect) == True:
		# 	print("eargsthd")
		return(self.x, self.y)



# class tile():
# 	"""docstring for tile"""
# 	def __init__(self, tile):
# 		self.tile = tile
# 	def draw(surface, x, y):
# 		surface.blit(self.tile, (self.x,self.y))
# 	#include tile properties

# class tile():
# 	"""docstring for tile"""
# 	def __init__(self, type):
# 		self.type = type
# 	def draw(type):
# 		if type == 0:

		

class level():
	"""docstring for level"""
	def __init__(self, level_matrix, tile, tileX, tileY):
		self.level_matrix = level_matrix
		self.tile = tile
		self.tileX = tileX
		self.tileY = tileY

	def draw(self, tileX, tileY, tile, wall):

		screen.blit(tile, (tileX,tileY))
	#include tile properties
		tileRect = pygame.Rect(tileX, tileY, 50, 50)
		if wall == True:
			tileRect = pygame.Rect(tileX, tileY, 50, 50)
		else:
			pass
		return tileRect

	def render_level(self,tile):
		self.tileX = 0
		self.tileY = 0

		tileRect_list = []

		for row in self.level_matrix:
			for item in row:
				# print (item)`
				if item == 0:
					hi=self.draw(self.tileX, self.tileY, tile[0],False)
					
				elif item == 1:
					hi=self.draw(self.tileX, self.tileY, tile[1],True)
					tileRect_list.append(hi)
				elif item == 2:
					hi=self.draw(self.tileX, self.tileY, tile[2],False)
					endTile = self.draw(self.tileX, self.tileY, tile[2],False)
				elif item == 3:
					hi=self.draw(self.tileX, self.tileY, tile[3],False)
					

				
				# print(hi)
				self.tileX+=50

			self.tileX = 0
			self.tileY+=50
			# print("good")
			
		return tileRect_list ,endTile


"""This is where my program starts """
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False


#one = [[0,1],[2,3]]

one =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,3,0,0,0,0,0,3],
		[1,0,0,0,0,0,0,0,0,0,3,3,0,0,3,3],
		[1,0,0,0,0,0,0,0,0,0,3,0,3,0,3,2],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3]]



myimage = pygame.image.load("b-ball.png")
door_tile = pygame.image.load("tile.png") #door
tile_tile =pygame.image.load("tile1.png") #tile
wall_tile =pygame.image.load("tile2.png") #wall	
light_tile =pygame.image.load("tile3.png") #light	



tiles = (tile_tile, wall_tile, door_tile, light_tile)


level_one = level(one, tiles,0,0) #level



x_collide = False
y_collide = False
tileBox = level_one.render_level(tiles)
bob=player(myimage,50,50,tileBox) #player
bob.draw(screen)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	tileBox = level_one.render_level(tiles)


	# level_one.render_level(tiles)

	#screen.fill((0,0,255))
	temp_coor = bob.move()
	playerBox = bob.draw(screen)
	





	tile_temp_coor = level_one.render_level(tiles)

	bob=player(myimage,temp_coor[0],temp_coor[1],tileBox)
	bob.draw(screen)


	pygame.display.flip()