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
	def __init__(self, is_full_size, small_size,size_is_normal,my_id,x,y):#id is number and if certain id, x and y set. SIZE is boolean if it is full screen or just icon
	# SIZE if fullscreen, press enter to make gone...
		self.is_full_size = is_full_size
		self.small_size = small_size
		self.size_is_normal = size_is_normal
		self.my_id = my_id
		self.x = x
		self. y = y
		

	def show(self):
		myEffect = pygame.mixer.Sound(getPath("assets/C.ogg"))
		if self.is_full_size == True:
			screen.blit(self.size_is_normal[self.my_id], (0,0))
			myEffect.play()
		else:
			pass
			# screen.blit(self.small_size[self.my_id], (self.x,self.y))
		return(self.small_size[self.my_id],self.x,self.y)

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

class game_class():
	"""docstring for game_class"""
	def __init__(self, level_matrix, player_location, number, chest_checklist):
		self.level_matrix = level_matrix
		self.x = player_location[0]
		self.y = player_location[1]
		self.number = number
		self.present_list = presents_s
		#-----------------------------------------------------------------
		#-----------------------------------------------------------------
		self.chest_checklist = chest_checklist
		#-----------------------------------------------------------------
		#-----------------------------------------------------------------
	def game(self):
		done = False
		presents_small = (present1_s,present2_s,present3_s,present4_s,present5_s,present6_s)
		#level
		level_one = level(self.level_matrix, tiles,0,0) #level



		x_collide = False
		y_collide = False
		tileBox = level_one.render_level(tiles)

		bob=player(myimage,self.x,self.y,tileBox,tileBox, False, False) #player
		bob.draw(screen)

		my_present = present(True, presents_s,presents,int(self.number)-1,(int(self.number)-1)*50,0)

		john = bar(presents_small,self.number,False,self.chest_checklist)


		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				elif event.type == pygame.KEYDOWN: #PRESS R IF STUCK OUT SIDE OR IN WALLS
					if event.key == pygame.K_r:
						bob.x = self.x
						bob.y = self.y
					elif event.key == pygame.K_RETURN and temp_coor[3] == True:
						print("asgdfsghrete")
						my_present.is_full_size = False

			temp_chest_check = self.chest_checklist
			tileBox = level_one.render_level(tiles)
			
			temp_coor = bob.move()
			playerBox = bob.draw(screen)
			next_level = bob.next_level
			gotChest = bob.gotChest
			# print (temp_coor[3])
			john = bar(presents_small,self.number,False,self.chest_checklist)
	#my_present.is_full_size


			bob=player(myimage,temp_coor[0],temp_coor[1],tileBox,tileBox, next_level,gotChest)
			bob.draw(screen)

			if temp_coor[3] == True:
				self.image = my_present.show()[0]
				self.chest_checklist[self.number-1] = True
				print('Chest opened!!!!!!!!! number is {}'.format(self.number))
				# return (False,chest_get_checklist)
				#level in which present was got
				if temp_coor[2] == True:
					return (True,temp_chest_check) #next level and if you got chest or not
					done = True
			elif temp_coor[2] == True:
				return (True,temp_chest_check) #next level and if you got chest or not
				done = True
			


			#bar "code" hahahahahahahahaha-----------------------

			john.draw()

			print(temp_chest_check)

			pygame.display.flip()

class bar():
	"""docstring for bar"""
	def __init__(self,presentList,maxi,new_gotChest,alreadyGot):
		self.presentList = presentList
		self.maxi = maxi
		self.new_gotChest = new_gotChest
		self.alreadyGot = alreadyGot
	def draw(self):
		count = 0
		for x in self.presentList[:self.maxi]:
			for status in self.alreadyGot:
				if status == True:
					screen.blit(x, ((self.alreadyGot.index(status)*50)+250,0))
				else:
					if self.new_gotChest == True:
						screen.blit(x, (count+250,0))
					else:
						pass
					count+=50

def getPath(path):
	the_path = os.path.abspath(path)
	return the_path

def title_screen(image):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: #PRESS R IF STUCK OUT SIDE OR IN WALLS
				if event.key == pygame.K_SPACE:
					done = True
		# myPresentBar = bar(1,presentList,0,0)
		# myPresentBar.show()
		screen.blit(image, (0,0))
		# count = 0
		# for x in presentList:
		# 	screen.blit(x, (count,0))
		# 	count+=50

		pygame.display.flip()

def final_boss_game(boss_image,level):
	bossX = 0
	bossY = 0
	done = False
	count6 = 0
	print(count6)

	#clock here--------------------------
	clock = pygame.time.Clock()
	counter, text = 66, '66'.rjust(3)
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	#------------------------------------

	while not done:
		bossX = randrange(-1,1)
		bossY = randrange(-1,1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_6:
					count6+=1
					print(count6)
				elif event.key == pygame.K_RETURN:
					count6+=11
					print(count6)
			elif event.type == pygame.USEREVENT:
				counter -= 1
				text = str(counter).rjust(3) if counter > 0 else 'boom!'


		#timer

		screen.blit(boss_image, (bossX,bossY))
		messageText(str(counter),20,40,30,screen,255,255,255)
		messageText("b baller man has {} lives left".format(str(int(7-level))),500,40,30,screen,255,255,255)
		messageText("6 pressed {} times...".format(str(count6)),550,500,30,screen,255,255,255)
		messageText("press ENTER for powerup...",300,550,30,screen,255,255,255)
		# count = 0
		# for x in presentList:
		# 	screen.blit(x, (count,0))
		# 	count+=50
		if count6 >= 66:
			print("you win")
			done = True
		pygame.display.flip()
		clock.tick(60)



"""This is where my program starts """
import pygame
from fadetoWhite import *
import os
from random import randrange
from displayText import *
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
		[1,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1],
		[1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,3,0,0,3,0,0,0,0,0,1],
		[1,0,0,0,0,3,0,2,2,0,3,0,0,0,0,1],
		[1,0,0,0,0,3,0,2,2,0,3,0,0,0,0,1],
		[1,0,0,0,0,0,3,0,0,3,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



pygame.display.set_caption("B-Baller Tomb (Pyweek27) ...")

#image

#player, tile
myimage = pygame.image.load(getPath("assets/b-ball.png"))
door_tile = pygame.image.load(getPath("assets/tile.png")) #door
tile_tile =pygame.image.load(getPath("assets/tile1.png")) #tile
wall_tile =pygame.image.load(getPath("assets/tile2.png")) #wall	
light_tile =pygame.image.load(getPath("assets/tile3.png")) #light	
baller_tile =pygame.image.load(getPath("assets/tile4.png")) #light
boss = pygame.image.load(getPath("assets/boss.png"))

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

#scene
title = pygame.image.load(getPath("assets/title.png"))
scene1 = pygame.image.load(getPath("assets/scene1.png"))
scene2 = pygame.image.load(getPath("assets/scene2.png"))
scene3 = pygame.image.load(getPath("assets/scene3.png"))
scene4 = pygame.image.load(getPath("assets/scene4.png"))
scene5 = pygame.image.load(getPath("assets/scene5.png"))
scene6 = pygame.image.load(getPath("assets/scene6.png"))


tiles = (tile_tile, wall_tile, door_tile, light_tile, baller_tile)
presents = (present1,present2,present3,present4,present5,present6)
presents_s = (present1_s,present2_s,present3_s,present4_s,present5_s,present6_s)


	





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def main_loop():
	pygame.mixer.music.load(getPath("assets/bb.mp3")) 
	chest_checklist = [False,False,False,False,False,False]
	player_location = ((50,50),(50,50),(150,250),(350,100),(650,100),(550,450))
	level_list = (one, two, thr, fou, fiv, six)

	# game1 = game_class(one,50,50,1)
	# game2 = game_class(two,50,50,2)
	# game3 = game_class(thr,150,250,3)
	# game4 = game_class(fou,350,100,4)
	# game5 = game_class(fiv,650,100,5)
	# game6 = game_class(six,550,450,6)

	chest_item_list=[]
	#level_list = [game1,game2,game3,game4,game5,game6]
	title_screen(title)
	title_screen(scene1)
	while True:
		i = 0
		for level in level_list:
			game = game_class(level, player_location[i], i+1, chest_checklist)
			chest_checklist = game.chest_checklist
			i += 1
			print('new chest_checklist {}'.format(chest_checklist))
			game.game()
		if chest_checklist == [True,True,True,True,True,True]:
			pygame.mixer.music.play(-1,0.0)
			title_screen(scene2)
			title_screen(scene3)
			title_screen(scene4)
			title_screen(scene5)
			fadetoWhite(screen)
			final_boss_game(boss,1)
			final_boss_game(boss,2)
			final_boss_game(boss,3)
			final_boss_game(boss,4)
			final_boss_game(boss,5)
			final_boss_game(boss,6)
			title_screen(scene6)
			quit()



main_loop()

