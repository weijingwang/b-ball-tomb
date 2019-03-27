class player():
	"""docstring for player"""
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y

	def draw(self, surface):
		player = surface.blit(self.image, (self.x,self.y))
		playerRect = pygame.Rect(self.x, self.y, 49, 49)

	def move(self):
		pressed = pygame.key.get_pressed()
		self.draw(screen)
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

	def draw(self, tileX, tileY, tile):

		screen.blit(tile, (tileX,tileY))
	#include tile properties
		tileRect = pygame.Rect(self.tileX, self.tileY, 50, 50)

	def render_level(self,tile):
		tileX = 0
		tileY = 0

		tile_coordsX = []
		tile_coordsY = []

		for row in self.level_matrix:
			for item in row:
				# print (item)
				if item == 0:
					self.draw(tileX, tileY, tile[0])
				elif item == 1:
					self.draw(tileX, tileY, tile[1])
				elif item == 2:
					self.draw(tileX, tileY, tile[2])
				elif item == 3:
					self.draw(tileX, tileY, tile[3])

				tile_coordsX.append(tileX)

				tileX+=50
			tileX = 0
			tile_coordsY.append(tileY)
			tileY+=50


"""This is where my program starts """
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False



one =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



myimage = pygame.image.load("myimage.png")
door_tile = pygame.image.load("tile.png") #door
tile_tile =pygame.image.load("tile1.png") #tile
wall_tile =pygame.image.load("tile2.png") #wall	
light_tile =pygame.image.load("tile3.png") #light	


bob=player(myimage,30,9) #player
bob.draw(screen)


tiles = (tile_tile, wall_tile, door_tile, light_tile)

level_one = level(one, tiles,0,0) #level



x_collide = False
y_collide = False


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	level_one.render_level(tiles)

	#screen.fill((0,0,255))
	temp_coor = bob.move()
	# tile_temp_coor = level_one.render_level(tiles)

	bob=player(myimage,temp_coor[0],temp_coor[1])
	bob.draw(screen)

	# for x in tile_temp_coor[0]:
	# 	if temp_coor[0] == tile_temp_coor[0]:
	# 		x_collide = True
	# 		print("x")
	# 	else:
	# 		x_collide = False
	# for y in tile_temp_coor[1]:
	# 	if temp_coor[1] == tile_temp_coor[1]:
	# 		y_collide = True
	# 		print("y")
	# 	else:
	# 		y_collide = False
	# if x_collide == True and y_collide == True:
	# 	print("collision")

	pygame.display.flip()