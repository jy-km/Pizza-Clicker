import random
import rect

def shop(pos, fevertime_coords, chefs_kiss_coords, ovenbroven_coords, drovenovengonewrongcoords, animewaifucoords, pizzanum, fever, feverTimer, kiss, asdf):
  if (rect.inside_rect(pos, fevertime_coords)) == True: #fevertime
    if pizzanum - 200 >= 0:
      pizzanum = pizzanum - 200
      fever = random.randint(2,10)
      feverTimer = 15
      
  if (rect.inside_rect(pos, chefs_kiss_coords)) == True: #chef's kiss
    if pizzanum - 400 >= 0:
      pizzanum -= 400
      kiss = kiss + 1

  if (rect.inside_rect(pos, ovenbroven_coords)) == True: 
    if pizzanum - 600 >= 0:
      pizzanum -= 600
      randintrandom = random.randint(1,100)
      if randintrandom == 69:
        kiss = kiss + 100
        print("you succeeded")
      else:
        print("EPIC FAIL")
  if (rect.inside_rect(pos, drovenovengonewrongcoords)) == True:
    if pizzanum - 800 >= 0:
      pizzanum -= 800
      randintrandom = random.randint(1,100000)
      if randintrandom == 50000:
        pizzanum = pizzanum + 1000000000
        print("you succeeded :)")
      else:
        pizzanum = 0
        print("PITIFUL FAIL")
  if (rect.inside_rect(pos, animewaifucoords)) == True:
    if pizzanum - 1000 >= 0:
      pizzanum -= 1000

      randintrandomrare = random.randint(1,asdf)
      if randintrandomrare == 1:
        pizzanum = pizzanum + 1000000
        asdf = asdf ** 2
        print(asdf)
        print("You have got your waifu's love and her blessings have given you loads of pizzas.")
      else:
        print("Your heart is broken because your waifu didn't like you. Sad.")
  return (fever, feverTimer, kiss, pizzanum, asdf)
  