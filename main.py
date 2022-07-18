import pygame
import math
import random
import shop
import rect

pygame.init()

#normal computer screen
#width = 1800
#height = 900
width = 800
height = 600

states = {
  "main": 0,
  "shop": 1
}

screen = pygame.display.set_mode([width, height])
posx = 200
posy = 200
pos = pygame.mouse.get_pos()
r = 100
pizzanum = 2000
state = states["main"] 
font = pygame.font.Font('freesansbold.ttf', 32)
small_font = pygame.font.Font('freesansbold.ttf', 18)
fever = 1
running = True
shopcoords = ((700, 0), (800, 100)) 
fevertime_coords = ((150,100),(250,200))
chefs_kiss_coords = ((350,100),(450,200))
ovenbroven_coords = ((550,100),(650,200))
drovenovengonewrongcoords = ((250,300),(350,400))
animewaifucoords = ((450,300),(550,400))
getTicksLastFrame = 0
feverTimer = 0
kiss = 1
pizza = pygame.image.load('pizza.png')
pizza = pygame.transform.scale(pizza, (2*r,2*r))
    
while running == True:
  t = pygame.time.get_ticks()
  deltaTime = (t - getTicksLastFrame) / 1000.0
  getTicksLastFrame = t
  feverTimer = feverTimer - deltaTime
  if feverTimer <= 0:
    fever = 1
  if state == states["main"]:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
  
      if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
        pos = pygame.mouse.get_pos()
        a = pos[0] - posx
        b = pos[1] - posy
        dist = math.sqrt(a**2 + b**2)
        if dist < r: #pizza
          pizzanum += (fever * kiss)
        if (rect.inside_rect(pos, shopcoords)) == True: #shop button 
          state = states["shop"]

    text = font.render('Pizza: '+str(pizzanum), False, (0,0,0))
    fever_text = font.render('Fever: '+str(fever), False, (0,0,0))
    timer_text = font.render('Time: '+str(round(feverTimer)), False, (0,0,0))
    menu_text = small_font.render('Shop', False, (0,0,0))    
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (194, 175, 138), pygame.Rect(shopcoords[0][0], shopcoords[0][1], shopcoords[1][0]-shopcoords[0][0], shopcoords[1][1]-shopcoords[0][1]))
    screen.blit(pizza,(posx-r,posy-r))
    screen.blit(text, (0,0))
    screen.blit(menu_text, (725, 35))
    if fever > 1:
      screen.blit(fever_text, (200,0))
    if feverTimer > 0:
      screen.blit(timer_text, (400,0))
    pygame.display.flip()

  if state == states["shop"]: 
    screen.blit(fever_text, (725, 35))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
        state = states["main"]  
      if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        pos = pygame.mouse.get_pos()
        (fever, feverTimer, kiss) = shop.shop(pos, fevertime_coords, chefs_kiss_coords, ovenbroven_coords, drovenovengonewrongcoords, pizzanum, fever, feverTimer, kiss)

    screen.fill((194, 175, 138))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(fevertime_coords[0][0], fevertime_coords[0][1], fevertime_coords[1][0]-fevertime_coords[0][0], fevertime_coords[1][1]-fevertime_coords[0][1]))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(chefs_kiss_coords[0][0], chefs_kiss_coords[0][1], chefs_kiss_coords[1][0]-chefs_kiss_coords[0][0], chefs_kiss_coords[1][1]-chefs_kiss_coords[0][1]))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(ovenbroven_coords[0][0], ovenbroven_coords[0][1], ovenbroven_coords[1][0]-ovenbroven_coords[0][0], ovenbroven_coords[1][1]-ovenbroven_coords[0][1]))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(drovenovengonewrongcoords[0][0], drovenovengonewrongcoords[0][1], drovenovengonewrongcoords[1][0]-drovenovengonewrongcoords[0][0], drovenovengonewrongcoords[1][1]-drovenovengonewrongcoords[0][1]))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(animewaifucoords[0][0], animewaifucoords[0][1], animewaifucoords[1][0]-animewaifucoords[0][0], animewaifucoords[1][1]-animewaifucoords[0][1]))

    shopfevertext = small_font.render('Fever', False, (0,0,0))
    screen.blit(shopfevertext, (175,120))

    shopfevertwotext = small_font.render('Boost', False, (0,0,0))
    screen.blit(shopfevertwotext,(175,140))
    
    shopfevercosttext = small_font.render('Cost: 200', False, (0,0,0))
    screen.blit(shopfevercosttext, (160,160))

    shopchefskisstext = small_font.render("Chef's Kiss", False, (0,0,0))
    screen.blit(shopchefskisstext, (350,130))
    
    shopchefskisscosttext = small_font.render('Cost: 400', False, (0,0,0))
    screen.blit(shopchefskisscosttext, (360,150))

    shopovenbroventext = small_font.render('Oven', False, (0,0,0))
    screen.blit(shopovenbroventext, (580,120))

    shopovenbroventexttwo = small_font.render('Broven', False, (0,0,0))
    screen.blit(shopovenbroventexttwo, (570,140))

    shopovenbrovencosttext = small_font.render('Cost: 600', False, (0,0,0))
    screen.blit(shopovenbrovencosttext, (560,160))

    shopdogwtext = small_font.render('DOGW', False, (0,0,0))
    screen.blit(shopdogwtext, (270,330))

    shopdogwcosttext = small_font.render('Cost: 800', False, (0,0,0))
    screen.blit(shopdogwcosttext, (260,350))

    shopanimewaifutext = small_font.render('Anime', False,(0,0,0))
    screen.blit(shopanimewaifutext, (470,320))

    shopanimewaifutwotext = small_font.render('Waifu', False, (0,0,0))
    screen.blit(shopanimewaifutwotext, (470,340))

    shopanimewaifucosttext = small_font.render('Cost: 1000', False, (0,0,0))
    screen.blit(shopanimewaifucosttext, (455,360))
    
    pygame.display.flip()

pygame.quit()


#item ideas
#1.fever boost; just combo boost(done)
#for fever boost Click button and subtract pizzas from the pizza you already have
#When we are in frenzy, clicking on the pizza gives you more pizza than original amount (at a certain/fixed rate)
#After 15 secs, the fever wil end
#2.chef's kiss; hires the chef born and raised in italy(done)
#3.oven broven; 50% chance for 20% more pizzas and 50% chance to lose all of the pizza (spelled broven but pronounced bruh-ven)(done)
#4.droven oven gone wrong (cops called at 1am) (help me) (totally not clickbait); 1% chance to win the game by getting 50000000000 times more pizzas and 99% chance to lose all of the pizza
#5.anime waifu; your favorite waifu to help you buy stocks!

# HW for this week

# future ideas
# 1. Add a stocks system
# - Jaeyoon has an idea on how to do stock prices
# - 
# 2. Maybe add more menus?