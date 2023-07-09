print("")
print("")
print("")

print("Welcome to my Quiz Game, I hope you enjoy!")

points = 0
aa = input("This game will consist of 10 questions where the difficulty will increase per question. Are you sure you want to play? ")

if aa.lower() == "yes":
    print("Let's proceed then")
    first = input("Question 1: When did the Titanic sink? ")
    while first == "":
        first = input("Question 1: In what year did the Titanic sink? ")
    else:
        second = input("Question 2: What is 1 + 1? ")
        
        while second == "":
            second = input("Question 2: What is 1 + 1? ")   
        else:
            third = input("Question 3: How many eyes do snipers close when they shoot? ") 
            
            while third == "":
                third = input("Question 3: How many eyes do snipers close when they shoot? ")
            else:
                fourth = input("Question 4: Is Pluto considered as a planet? ")

                while fourth == "":
                    fourth = input("Question 4: Is Pluto considered as a planet? ")
                else:
                    fifth = input("Question 5: In what year did Queen Elizabeth II die? ")

                    while fifth == "":
                        fifth = input("Question 5: In what year did Queen Elizabeth II die? ")
                    else:
                            
                        if first == "1912":
                            points += 1
                        if second == "2":
                            points += 1
                        if third == "1":
                            points += 1
                        if fourth.lower() == "no":
                            points += 1
                        if fifth == "2022":
                            points += 1



                        print("You are done, good job!!")
                        bb = input("Do you want to know your score? ")

                        if bb.lower() == "yes" and points > 3:
                            print("Good job! You got", points, "points out of 5. Thank you for playing!")
                            exit
                        elif bb.lower() == "yes" and points <= 3 and points > 0:
                            print("Keep it up! You got", points, "points out of 5. Thank you for playing!")
                            exit
                        elif bb.lower() == "yes" and points == 0:
                            print("Better luck next time! You got", points, "points out of 5. Thank you for playing!")
                            exit
                        else:
                            print("Okay, thank you for playing!!!")
                            exit

else:
    print("Maybe next time then")
    exit



print("")
print("")
print("")