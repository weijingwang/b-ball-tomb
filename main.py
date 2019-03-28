class player():
	"""docstring for player"""
	def __init__(self, image, x, y,tileBoxes,chestBoxes,next_level,gotChest):
		self.image = image
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.rect = pygame.Rect(self.x, self.y, 50, 50)
		self.tileBoxes = tileBoxes
		self.chestBoxes = chestBoxes
		self.next_level = next_level
		self.gotChest = gotChest

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
			self.next_level = True #----------------------------------------------------------------------------------

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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if self.rect.colliderect(self.chestBoxes[2]):
						print("look out a chest omg! press space to open!")
						self.gotChest = True #----------------------------------------------------------------------------------

	
		return(self.x, self.y, self.next_level, self.gotChest)



class present(): #stuff in the chest and when you open it, you get this and it will show in a bar
	"""docstring for present"""
	def __init__(self, full_size, small_size,size_is_normal,my_id,x,y):#id is number and if certain id, x and y set. SIZE is boolean if it is full screen or just icon
# SIZE if fullscreen, press enter to make gone...
		self.full_size = full_size
		self.small_size = small_size
		self.size_is_normal = size_is_normal
		self.my_id = my_id
		self.x = x
		self. y = y
		

	def show(self):
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.size_is_normal = False
			if self.size_is_normal == True:
				screen.blit(self.full_size[self.my_id], (self.x,self.y))
			else:
				screen.blit(self.small_size[self.my_id], (self.x,self.y))


		

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
		chestRect_list = []
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
					hi=self.draw(self.tileX, self.tileY, tile[4],False)
					chest =self.draw(self.tileX, self.tileY, tile[4],False)
					# tileRect_list.append(hi)
					chestRect_list.append(chest)
					
				# print(hi)
				self.tileX+=50

			self.tileX = 0
			self.tileY+=50
			# print("good")
			
		return tileRect_list ,endTile, chest



"""This is where my program starts """
import pygame
import os
pygame.init()
screen = pygame.display.set_mode((800, 600))

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
present1_s = pygame.transform.scale(present1, (50,50))
present2 = pygame.image.load(getPath("assets/present2.png")) # b-ball rookie
present2_s = pygame.transform.scale(present2, (50,50))
present3 = pygame.image.load(getPath("assets/present3.png")) # b-ball bone
present3_s = pygame.transform.scale(present3, (50,50))
present4 = pygame.image.load(getPath("assets/present4.png")) # slam dunk REDO?
present4_s = pygame.transform.scale(present4, (50,50))
present5 = pygame.image.load(getPath("assets/present5.png")) # JOIN THE PACK
present5_s = pygame.transform.scale(present5, (50,50))
present6 = pygame.image.load(getPath("assets/present6.png")) #summon
present6_s = pygame.transform.scale(present6, (50,50))

title = pygame.image.load(getPath("assets/title.png"))

tiles = (tile_tile, wall_tile, door_tile, light_tile, baller_tile)
presents = (present1,present2,present3,present4,present5,present6)
presents_s = (present1_s,present2_s,present3_s,present4_s,present5_s,present6_s)


def title_screen():
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN: #PRESS R IF STUCK OUT SIDE OR IN WALLS
				if event.key == pygame.K_SPACE:
					done = True

		screen.blit(title, (0,0))

		pygame.display.flip()	



def game(level_matrix, x, y):
	done = False

	#level
	level_one = level(level_matrix, tiles,0,0) #level



	x_collide = False
	y_collide = False
	tileBox = level_one.render_level(tiles)

	bob=player(myimage,x,y,tileBox,tileBox, False, False) #player
	bob.draw(screen)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: #PRESS R IF STUCK OUT SIDE OR IN WALLS
				if event.key == pygame.K_r:
					bob.x = 50
					bob.y = 50

		tileBox = level_one.render_level(tiles)

		temp_coor = bob.move()
		playerBox = bob.draw(screen)
		next_level = bob.next_level
		gotChest = bob.gotChest
		


		tile_temp_coor = level_one.render_level(tiles)

		bob=player(myimage,temp_coor[0],temp_coor[1],tileBox,tileBox, next_level,gotChest)
		bob.draw(screen)

		if temp_coor[2] == True:
			return (True,temp_coor[3]) #next level and if you got chest or not
			done = True
		pygame.display.flip()	

	




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

my_present = present(presents, presents_s,True,0,0,0)
title_screen()
while True:

#do all seperate screens no if statement as much???
	if game(one,50,50)[0] == True:
		if game(two,50,50)[0] == True:
			if game(thr,150,250)[0] == True:
				if game(fou,350,100)[0] == True:
					if game(fiv,650,100)[0] == True:
						if game(six,550,450)[0] == True:
							continue
	if game(one,50,50)[1] == True:
		print("yes")
		if game(two,50,50)[1] == True:
			if game(thr,150,250)[1] == True:
				if game(fou,350,100)[1] == True:
					if game(fiv,650,100)[1] == True:
						if game(six,550,450)[1] == True:
							quit()