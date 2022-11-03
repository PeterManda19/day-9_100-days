from datetime import date
import time


def endGame():
  while True:
    print()
    x= input("""To try again please click Stop on top right page and click Run """)
    print()
    continue

print("Welcome to Generation Generator!")
print()
time.sleep(1)
current_year = date.today().year
print("I hope the year",current_year,"is kind to you.😀")
print()
time.sleep(1)
print("If you tell me your age I will tell what generation you are a part of.")
print()
time.sleep(1)
print("Use 'quit' or 'exit' to end the game")
print()
time.sleep(1)
while True:
    age = input("Hello there! How old are you? ")
    print()
    if age.isalpha() == True:
        if age.lower().strip() == "quit" or age.lower().strip() == "exit":
            endGame()
            break
        else:
            print()
            time.sleep(1)
            print(
                "Please enter your age as a whole number  or enter 'quit' or 'exit' to end the game."
            )
            print()
            continue
    elif age.isalnum() == True and (int(age) >= (current_year - 1946) and int(age) <= (current_year - 1925)):
        print()
        time.sleep(1)
        print("Awesome! so you are", int(age), "years old.")
        print()
        time.sleep(2)
        print("Looking for your generation name...")
        print()
        time.sleep(3)
        print("Your generation name is Traditionalist.Greetings my honourable senior citizen!😀")    
        endGame()
        break
    
    elif age.isalnum() == True and (int(age) >= (current_year - 1964) and int(age) <= (current_year - 1947)):
        print()
        time.sleep(1)
        print("Awesome! so you are", int(age), "years old.")
        print()
        time.sleep(2)
        print("Looking for your generation name...")
        print()
        time.sleep(3)
        print("Your generation name is Baby Boomers.Greetings my senior citizen!😀") 
        endGame()
        break  
    
    elif age.isalnum() == True and (int(age) >= (current_year - 1981) and int(age) <= (current_year - 1965)):
        print()
        time.sleep(1)
        print("Awesome! so you are", int(age), "years old.")
        print()
        time.sleep(2)
        print("Looking for your generation name...")
        print()
        time.sleep(3)
        print("Your generation name is Generation X.Greetings my honourable senior citizen!😀") 
        endGame()
        break  
    
    elif age.isalnum() == True and (int(age) >= (current_year - 1995) and int(age) <= (current_year - 1982)):
        print()
        time.sleep(1)
        print("Awesome! so you are", int(age), "years old.")
        print()
        time.sleep(2)
        print("Looking for your generation name...")
        print()
        time.sleep(3)
        print("Your generation name is Millenials.Greetings my fellow Millenial!😀")
        endGame()
        break
    
    elif age.isalnum() == True and (int(age) >= (current_year - 2015) and int(age) <= (current_year - 1996)):
        print()
        time.sleep(1)
        print("Awesome! so you are", int(age), "years old.")
        print()
        time.sleep(2)
        print("Looking for your generation name...")
        print()
        time.sleep(3)
        print("Your generation name is Generation Z. Hello!😀") 
        endGame()
        break
    
    elif age.isalnum() == True and (int(age) >= 0 and int(age) <= (current_year - 2016)):
        print()
        time.sleep(1)
        print("Awesome! so you are", int(age), "years old.")
        print()
        time.sleep(2)
        print("Looking for your generation name...")
        print()
        time.sleep(3)
        print("Hi young one! You are too young to have a generation name.😀") 
        endGame()
        break
   
    else:
        print()
        print("Please enter your age as a whole number  or enter 'quit' or 'exit' to end the game.")
        print()
        continue


if __name__ == "__main__":
  endGame()
