import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

path = []

for x in range(0,50, 1):
	y=1*x**2-20*x-10
	if y >= 0:
	# 	y=y
	# else:
		path.append((x,y))

print (path)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	lol = pygame.draw.lines(screen, (255,0,0), True, path, 1)

	pygame.display.flip()