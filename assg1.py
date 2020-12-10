
def name_diagnol(name):
  size=len(name)
  for x in range(size):   #0-4
    for y in range(x):    #0-4
        print("  ",end="")
    print(name[x]+"\n")


def rev_diagnol(name):
  size=len(name)
  for x in range(size):   #0-4
    for y in range(size,x,-1):    #0-4
        print("  ",end="")
    print(name[x]+"\n")

name=input("Enter name to print its daignol:")
name_diagnol(name)
rev_diagnol(name)