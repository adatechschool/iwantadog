from dog import *

print("Va chercher!")
def main():
   x = Dog()
   x.colour("brun")
   x.sex("male")
   x.age(2, 4)
   print(x.colour, x.sex, x.age)

if __name__ == "__main__":
   main()
