import os

def checkEmpty():
  filepath = 'loggedInToken.txt'
  if(os.stat(filepath).st_size==0):
    return True
  else:
    return False
  
def getToken():
  filepath = 'loggedInToken.txt'
  f = open(filepath, 'r')
  return str(f.read())
    
def writeToken(tokenID):
  filepath = 'loggedInToken.txt'
  f = open(filepath, 'w')
  f.write(str(tokenID))
  
def deleteActualToken():
  filepath = 'loggedInToken.txt'
  f = open(filepath, 'w').close()
