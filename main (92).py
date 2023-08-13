import csv


def writein(filename, list):
  with open (filename, 'a', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(list)

def readin(filename):
  directory = []
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for pair in reader:
      directory.append(pair)
  return directory

def signfor(var):
  if var == "yes":
    signup = input("username: ")
    while len(signup) <= 7:
      print ("try again! it needs to be at least 8 characters long!")
      signup = input("username: ")
    signup2 = input("password: ")
    signuplist = [signup, signup2]
    writein(filename, signuplist)

want = input("sign up or log in? ")
if want == "sign up" or want == "signup":
  signup = input("username: ")
  while len(signup) <= 7:
    print ("try again! it needs to be at least 8 characters long!")
    signup = input("username: ")
  signup2 = input("password: ")
  signuplist = [signup, signup2]
  writein(filename, signuplist)
elif want == "log in" or want == "login":
  login = input("username: ")
  login2 = input("password: ")
  loginlist = [login, login2]
  directorysignins = readin("signups.csv")
  for i in directorysignins:
    if i == loginlist:
      print ("welcome")
      break
    else:
      print("we don't have a login for you, sorry!")
      want = input("want to sign up?")
      signfor(want)
      break