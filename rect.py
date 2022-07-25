
def inside_rect(mousepos, rectbounds): # IMPORTANT!
  if rectbounds[0][0] < mousepos[0] and mousepos[0] < rectbounds[1][0] and rectbounds[0][1] < mousepos[1] and mousepos[1] < rectbounds[1][1]:
    return True
  else:
    return False

# f(x) = x
# y = x

# return takes you out of the function back to where you called the function and it brings whatever comes after "return" with it

# coords = (1, 1)

# def add(x, y, z):
#   return x + y + z

# add(1, 2, 3) == 3

# draw("fever", (100, 100))

# def draw(x = 'fever', y = (100, 100)):
#   shopfevertext = small_font.render('Fever', False, (0,0,0))
#   screen.blit(shopfevertext, (175,120))
# draw('ovenbroven', (175,120))


# the zoom meeting ended lmao
# i need to do something right now anyway since its been an hour since class was supposed to end
# take a look at these two videos
# https://www.youtube.com/watch?v=B0HfPTrRfxg
# https://www.programiz.com/python-programming/function

# try and understand what a function is before you try and write it I think you're having a little bit of a misunderstanding when it comes to understanding what a function is and what the purpose of it is

def f():
  return 1