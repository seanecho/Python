#Author: Sean Gao

age_of_sean = 32

count = 0
while count <3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_sean:
        print("You got it!")
        break
    elif guess_age > age_of_sean:
        print("Think smaller..")
    else:
        print("Think bigger..")
    count += 1
else:
    print("You've tried too many times, fuck off!")
