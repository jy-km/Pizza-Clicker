
def inside_rect(mousepos, rectbounds): # IMPORTANT!
  if rectbounds[0][0] < mousepos[0] and mousepos[0] < rectbounds[1][0] and rectbounds[0][1] < mousepos[1] and mousepos[1] < rectbounds[1][1]:
    return True
  else:
    return False