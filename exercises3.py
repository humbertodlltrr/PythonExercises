#Character Input
import datetime
def character_input():
    name = input("What's your name?")
    age = int(input("How old are you?"))
    num = int(input("Favorite number?"))
    year = str(datetime.datetime.now().year - age + 100)
    print(num*("Hey "+name+"! You will turn 100 in "+year+"\n"))

#Odd Or Even
def odd_even():
    num = int(input("Choose a number:"))
    if num%4 == 0:
        print("Multiple of 4!")
    elif num%2 == 0:
        print("It's even!")
    else:
        print("It's odd!")
    check = int(input("Another number:"))
    if(num%check == 0):
        print("Divides evenly")
    else:
        print("Doesn't divide evenly")

#List Less Than 10
