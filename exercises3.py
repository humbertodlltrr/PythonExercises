import time

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
a = [1,1,2,3,5,8,13,21,34,55,89]
def list_lt_10():
#    for i in a:
#        if i < 5:
#            print(i)
    n = int(input("Lower than:"))
    new_list = [i for i in a if i < n]
    print(new_list)

#Divisors
def divisor():
    num = int(input("Number:"))
    for i in range(1,num+1):
        if num%i == 0:
            print(i)

#List Overlap Comprehensions
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
import random
def list_overlap():
    a = []
    for k in range(20):
        a.append(random.randrange(1,101))
    b = []
    for l in range(20):
        b.append(random.randrange(1,101))
    
    overlap = [i for i in set(a) if i in b]
    print(overlap)

#String Lists
def is_palindrome():
    string = list(input("String:"))
    print(string == list(reversed(string)))

#List Comprehensions
c = [1,4,9,16,25,36,49,64,81,100]
def even_only():
    print([i for i in c if i%2==0])

#Rock Paper Scissors
def rps_game():
    while (True):
        while (True):
            p1 = input("P1:Rock(r),paper(p),scissors(s):")
            if(p1 != "r" or p1 != "p" or p1 != "s"):
                break
        while (True):
            p2 = input("P2:Rock(r),paper(p),scissors(s):")
            if(p2 != "r" or p2 != "p" or p2 != "s"):
                break
        
        if (p1 == "r" and p2 == "r") or (p1 == "s" and p2 == "s") or (p1 == "p" and p2 == "p"):
            print("Tie")
        elif (p1 == "r" and p2 == "s") or (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r"):
            print("P1 wins!")
        else:
            print("P2 wins!")
        while(True):
            ng = input("New game(y/n)?")
            if(ng == "y" or ng == "n"):
                break
        if(ng == "n"):
            break

#Guessing Game One
def guess_game1():
    guesses = 0
    num = random.randrange(1,10)
    while(True):
        inp = input("Guess which number(1-9):")
        if (inp == "exit"):
            print("Guesses:",guesses)
            break
        elif(str(num) == inp):
            print("Correct")
            guesses += 1
        elif(int(inp) > num):
            print("Too high")
            guesses += 1
        else:
            print("Too low")
            guesses += 1

#Check Primality Functions
def is_prime():
    num = int(input("Check primality of:"))
    for i in range(2,num):
        if num%i == 0:
            print("Not prime")
            break
        else:
            print("Is prime")
            break
    
#Print primes from 2 to n
def primes(n=2):
    if n < 2:
        print("Nope, 2 or higher")
        return None
    start_time = time.time()
    pa = list(range(2,n+1))
    i = 0
    while(len(pa)!=i+1):
        pa = pa[:i+1]+[x for x in pa[i+1:] if x%pa[i]!=0]
        i += 1
    print(pa)
    print("--- %s seconds ---" % (time.time() - start_time))

#List Ends
def list_ends(lst):
    return lst[:1] + lst[-1:]

#Fibonacci, 1 1 2 3 5...
def fib(n):
    fibArr = [0,1]
    if n == 0:
        print(fibArr[0])
    elif n == 1:
        print(fibArr[1])
    else:
        for i in range(1,n+1):
            print(fibArr[1])
            fib = fibArr[0]+fibArr[1]
            fibArr[0] = fibArr[1]
            fibArr[1] = fib

#List Remove Duplicates, default mode 1 uses loop, mode anything but 1 uses sets
def remove_dups(lst,mode=1):
    if(mode == 1):
        ret = []
        for i in lst:
            if i not in ret:
                ret.append(i)
        return ret
    else:
        return list(set(lst))

#Reverse Word Order
def rword_order():
    s = input("Input string with multiple words:")
    lst = s.split()
    print(" ".join(reversed(lst)))

#Password Generator
pw_words = ["cool","shortstop", "apple","angry","happy","pear",
            "fast","password","crazy","beans","cat","dog","bear",
            "ninja","workplace","beer","ferrari","aston","martin",
            "firefly","rhythm","firefighter","astronaut"]
pw_nums = "1234567890"
pw_chars = "aAbBcCdDeEfFgGhHiIlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
pw_schars = "!#$%&()*+-/<=>?@[\]^_{|}~"

def rand_word():
    return pw_words[random.randrange(0,len(pw_words))]
def rand_num():
    return pw_nums[random.randrange(0,len(pw_nums))]
def rand_char():
    return pw_chars[random.randrange(0,len(pw_chars))]
def rand_schar():
    return pw_schars[random.randrange(0,len(pw_schars))]
def rand_all(n):
    if n == 0:
        return rand_word()
    elif n == 1:
        return rand_char()
    elif n == 2:
        return rand_num()
    else:
        return rand_schar()

def pass_gen():
    strength = int(input("Password strength(1-4):"))
    password = ""
    d = random.randrange(0,2)
    if d == 0:
        d = -1
    else:
        d = 1
    if(strength == 4):
        for i in range(0,20+(random.randrange(0,4))):
            rng = random.randrange(0,20)
            if rng <= 7:
                password += rand_all(1)
            elif rng <= 12:
                password += rand_all(2)
            else:
                password += rand_all(3)
    elif(strength == 3):
        for i in range(0,14+(d*random.randrange(0,5))):
            rng = random.randrange(0,20)
            if rng <= 9:
                password += rand_all(1)
            elif rng <= 17:
                password += rand_all(2)
            else:
                password += rand_all(3)
    elif(strength == 2):
        password += rand_all(0)[:4]
        for i in range(0,4+(d*random.randrange(0,3))):
            rng = random.randrange(0,10)
            if rng <= 7:
                password += rand_all(1)
            else:
                password += rand_all(2)
    else:
        while (len(password) <= 6):
            password += rand_word()
        password += rand_num() + rand_num()
    return password

#Cows And Bulls
def cows_bulls():
    num = str(random.randrange(1,10)) + str(random.randrange(0,10)) + str(random.randrange(0,10)) + str(random.randrange(0,10))
    guesses = 0
    while True:
        guess = input("Guess:")
        if guess == num:
            guesses += 1
            print("Correct! Attempts:",guesses)
            break
        else:
            guesses += 1
            cows = 0
            bulls = 0

            for i in range(len(num)):
                if num[i] in guess:
                    if num[i] == guess[i]:
                        cows += 1
                    else:
                        bulls += 1
            
            ret = str(cows)
            if cows == 1:
                ret += " cow, "
            else:
                ret += " cows, "
            ret += str(bulls)
            if bulls == 1:
                ret += " bull"
            else:
                ret += " bulls"
            print(ret)

#Element Search
bin_search = [1,3,5,30,42,43,100,157,201,382,418,419,420,499,500]
def search_binary(lst,n):
    median = lst[len(lst)//2]
    if lst == [] or (len(lst)==1 and lst[0]!=n):
        return False
    elif median > n:
        return search_binary(lst[:len(lst)//2],n)
    elif median < n:
        return search_binary(lst[-len(lst)//2:],n)
    else:
        return True
