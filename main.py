class player():
	"""docstring for player"""
	def __init__(self, image, x, y,tileBoxes):
		self.image = image
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.rect = pygame.Rect(self.x, self.y, 40, 40)
		self.tileBoxes = tileBoxes
	def draw(self, surface):
		player = surface.blit(self.image, (self.x,self.y))
		
		return self.rect

	def move(self):
		next_level = False
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
			next_level = True

		for wall in self.tileBoxes[0]:
			if self.rect.colliderect(wall):
				if self.dx > 0:
					# self.rect.right = wall.left
					print("careful, you could poke an eye out!left")
					self.x = wall[0]-50
				elif self.dx < 0:
					# self.rect.left = wall.right
					print("careful, you could poke an eye out!r")
					self.x = wall[0]+50
				elif self.dy > 0:
					# self.rect.bottom = wall.top
					print("careful, you could poke an eye out!t")
					self.y = wall[1]-50
				elif self.dy < 0:
					# self.rect.top = wall.bottom
					print("careful, you could poke an eye out!b")
					self.y = wall[1]+50
					

		# elif playerRect.colliderect(otherRect) == True:
		# 	print("eargsthd")
		return(self.x, self.y, next_level)



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


class present(): #stuff in the chest and when you open it, you get this and it will show in a bar
	"""docstring for present"""
	def __init__(self, my_id, size):#id is number and if certain id, x and y set. SIZE is boolean if it is full screen or just icon
		super(present, self).__init__() # SIZE if fullscreen, press space to make gone...
		self.my_id = my_id
		self.size = size
		self.x = x
		self. y = y
	def function():
		pass

		

		

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
				elif item == 4:
					hi=self.draw(self.tileX, self.tileY, tile[4],True)
					tileRect_list.append(hi)
					
				
				# print(hi)
				self.tileX+=50

			self.tileX = 0
			self.tileY+=50
			# print("good")
			
		return tileRect_list ,endTile



"""This is where my program starts """
import pygame
import os
pygame.init()
screen = pygame.display.set_mode((800, 600))



#level
"""
default =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
"""
one =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,4,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,1,1,1,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,3,1,0,0,0,3,0,0,0,0,0,3],
		[1,0,0,0,0,0,0,0,0,0,3,3,0,0,3,3],
		[1,0,0,0,0,0,0,0,0,0,3,0,3,0,3,2],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3]]

two =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,3,0,0,0,4,0,0,1,1,0,0,0,1,1,1],
		[1,0,0,0,0,0,3,3,3,3,3,0,0,1,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1,1,1,3,1],
		[1,1,1,0,0,1,1,1,1,1,1,1,3,3,0,1],
		[1,0,1,0,0,0,0,0,0,0,0,0,3,2,0,1],
		[1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
		[1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
		[1,0,0,0,0,0,3,3,3,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

thr =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,3,0,0,1,3,0,0,0,1],
		[1,0,0,3,0,0,3,4,3,0,1,3,0,0,0,1],
		[1,0,0,0,0,0,0,3,0,0,1,3,0,2,0,1],
		[1,0,0,0,0,0,0,0,0,0,1,3,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

fou =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,1,0,3,0,0,3,0,0,0,3,0,1],
		[1,0,0,0,1,0,0,0,0,0,0,0,0,3,0,1],
		[1,0,0,0,1,0,3,0,0,3,0,0,0,3,0,1],
		[1,0,0,0,1,0,0,0,0,0,0,0,0,3,0,1],
		[1,0,0,0,1,0,3,0,0,3,0,0,0,3,0,1],
		[1,0,0,0,1,0,0,0,0,0,0,1,0,3,0,1],
		[1,0,0,0,1,0,3,0,0,3,0,1,0,3,0,1],
		[1,0,0,0,1,0,0,0,0,0,0,1,0,3,0,1],
		[1,0,0,0,1,0,3,4,0,3,0,1,0,2,0,1],
		[1,0,0,0,1,0,0,0,0,0,0,1,0,3,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

fiv =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
		[1,0,4,0,0,0,0,0,0,1,1,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1],
		[1,0,0,0,0,0,1,1,1,0,0,0,0,0,3,1],
		[1,0,0,0,0,0,1,0,0,0,0,0,0,3,3,1],
		[1,0,0,0,0,0,3,0,0,0,0,0,3,3,0,1],
		[1,0,0,0,0,0,3,0,0,0,0,3,3,0,0,1],
		[1,0,0,0,0,0,1,1,1,3,3,3,0,0,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
		[1,0,0,0,0,0,0,0,0,0,2,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

six =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,3,0,0,3,0,0,0,0,0,1],
		[1,0,0,0,0,3,0,2,2,0,3,0,0,0,0,1],
		[1,0,0,0,0,3,0,2,2,0,3,0,0,0,0,1],
		[1,0,0,0,0,0,3,0,0,3,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


#image

def getPath(path):
	the_path = os.path.abspath(path)
	return the_path

#player, tile
myimage = pygame.image.load(getPath("assets/b-ball.png"))
door_tile = pygame.image.load(getPath("assets/tile.png")) #door
tile_tile =pygame.image.load(getPath("assets/tile1.png")) #tile
wall_tile =pygame.image.load(getPath("assets/tile2.png")) #wall	
light_tile =pygame.image.load(getPath("assets/tile3.png")) #light	
baller_tile =pygame.image.load(getPath("assets/tile4.png")) #light	
#presents
present1 = pygame.image.load(getPath("assets/present1.png")) # old b-ball poster
present2 = pygame.image.load(getPath("assets/present2.png")) # b-ball rookie
present3 = pygame.image.load(getPath("assets/present3.png")) # b-ball bone
present4 = pygame.image.load(getPath("assets/present4.png")) # slam dunk REDO?
present5 = pygame.image.load(getPath("assets/present5.png")) # JOIN THE PACK
present6 = pygame.image.load(getPath("assets/present6.png")) #summon
tiles = (tile_tile, wall_tile, door_tile, light_tile, baller_tile)


def game(level_matrix, x, y):
	done = False
	#level
	level_one = level(level_matrix, tiles,0,0) #level



	x_collide = False
	y_collide = False
	tileBox = level_one.render_level(tiles)
	bob=player(myimage,x,y,tileBox) #player
	bob.draw(screen)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		tileBox = level_one.render_level(tiles)

		temp_coor = bob.move()
		playerBox = bob.draw(screen)
		
		tile_temp_coor = level_one.render_level(tiles)

		bob=player(myimage,temp_coor[0],temp_coor[1],tileBox)
		bob.draw(screen)

		if temp_coor[2] == True:
			return True
			done = True
		pygame.display.flip()	

	










while True:
	if game(one,50,50) == True:
		if game(two,50,50) == True:
			if game(thr,150,250) == True:
				if game(fou,350,100) == True:
					if game(fiv,650,100) == True:
						if game(six,550,450) == True:
							continue