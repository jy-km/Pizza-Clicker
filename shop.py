import random
import rect

def shop(pos, fevertime_coords, chefs_kiss_coords, ovenbroven_coords, drovenovengonewrongcoords, pizzanum, fever, feverTimer, kiss):
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
    print('asdf')
  return (fever, feverTimer, kiss)
            
