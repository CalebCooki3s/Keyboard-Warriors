#opening the file then writing the questions into it

file=open("pythonquestions.txt", "w")
question1=file.write("1.Which statement will print? a.Print('Hello World') b.print('Hello World') c.print(Hello World) d.print(Hello + World)")
question2=file.write("\n2.True or False:Python is an interpreted language? a.True b.False")
question3=file.write("\n3.Which is NOT a type of loop? a.for x in s b.while x>0 c.for i in range() d.if x>0")
question4=file.write("\n4.What is an if statement? a.A statement that will run if all conditions are met b.A loop that won't stop until all conditions are met c.A statement that will break the loop if all conditions are met d.A statement that runs only if conditions aren't met")
question5=file.write("\n5.What index values need to be entered for x to get Burgers, Pizza, and Fries? \nMenu = ('Burgers,Pizza,Fries,Soda,Water') \nChoice=menu.split(',') \nprint(Choice[x:x]) \na.[1:3] b.[0:2] c.[0:3] d.[0:4]")


#making an index for the questions
file=open("pythonquestions.txt")
readfile = file.read()
questionsplit = readfile.split("\n")

#opening the file and writing the answers into it

answer_file=open("Answers.txt", "w")
answer1=answer_file.write("b.print('Hello World')")
answer2=answer_file.write("\na.True")
answer3=answer_file.write("\nd.if x>0(next line)x-=1")
answer4=answer_file.write("\na.A statement that will run if all conditions are met")
answer5=answer_file.write("\nc.[0:3]")

#list for the answers
answer_file=open("Answers.txt")
answer_r=answer_file.read()
answer_s=answer_r.split("\n")
#print(answer_s)

#Making user input for menu options
#user_input = input("Menu: a.Play a game b.View LeaderBoard c.exit")

#User input for questions makes sure the user inputs a,b,c, or d.
def isvalid_5(a,b,c,d,e):
    user_answer = input("Answer: ")
    user_answer = user_answer.lower()
    print(user_answer)
    if user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
        return user_answer
    while user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d":
        print("\nMust enter a,b,c, or d as the answer")
        print("\n"+str(questionsplit[a]), "\n\n" + str(questionsplit[b]),"\n" + str(questionsplit[c]),"\n" + str(questionsplit[d]),"\n\n" + str(questionsplit[e]))
        user_answer = input("Answer: ")
        if user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            return user_answer

def keyboard_warriors():
    username = input("Whats your username? ")
    score = 0
    print("\nHey",username,"there are 5 programming questions on this quiz, each one worth more than the last.\nAnswer each question carefully, Good luck!")
    print("\n"+str(questionsplit[0]))
    if isvalid(0) == answer_s[0][0]:
        score += 1
        print("Thats right",username+"!","\nScore:",score)
    else:
        print("Not quite",username+"...","\nScore:"+str(score))
    
    print(questionsplit[1])
    if isvalid(1) == answer_s[1][0]:
        score += 2
        print("Thats right",username+"!","\nScore:",score)
    else:
        print("Not quite",username+"...","\nScore:"+str(score))

    print(questionsplit[2])
    if isvalid(2) == answer_s[2][0]:
        score += 3
        print("Thats right",username+"!","\nScore:",score)
    else:
        print("Not quite",username+"...","\nScore:"+str(score))

    print(questionsplit[3])
    if isvalid(3) == answer_s[3][0]:
        score += 4
        print("Thats right",username+"!","\nScore:",score)
    else:
        print("Not quite",username+"...","\nScore:"+str(score))

    print(questionsplit[4], "\n\n" + str(questionsplit[5]),"\n" + str(questionsplit[6]),"\n" + str(questionsplit[7]),"\n\n" + str(questionsplit[8]))
    if isvalid_5(4,5,6,7,8) == answer_s[4][0]:
        score += 5
        print("Thats right",username+"!","\nScore:",score)
    else:
        print("Not quite",username+"...","\nScore:"+str(score))

    print("\nUsername:",username,"\nScore:",score)
    print("Thanks for Playing!")
    Leader_file = open("Leaderboard.txt","a")
    Leaderboard = Leader_file.write(str(username)+ " " +str(score))

    user_input2 = input("Wanna play again? y/n ")
    if user_input2 == "y" or user_input2 == "yes":
        keyboard_warriors()
    elif user_input2 == "n" or user_input2 == "no":
        menu = int(input("Menu:\n1.Play Game\n2.View Leaderboard\n3.View Answers\n4.Exit\n"))
    if menu == 1:
        keyboard_warriors()


    if menu == 3:
        print("\nAnswers:""\n"+str(answer_r))

    if menu == 4:
        user_input = input("Do you want to exit? y/n ")
        if user_input == "y" or "yes":
            SystemExit



    




Leader_f = open("Leaderboard.txt")
Leader_read = Leader_f.read()
Leader_split = Leader_read.split(" ")

print(answer_s)
    


def isvalid(b):
    user_answer = input("Answer: ")
    user_answer = user_answer.lower()
    print(user_answer)
    if user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
        return user_answer
    while user_answer != "a" or user_answer != "b" or user_answer != "c" or user_answer != "d":
        print("Must enter a,b,c, or d as the answer")
        print(questionsplit[b])
        user_answer = input("Answer: ")
        if user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            return user_answer

#Menu
menu = int(input("Menu:\n1.Play Game\n2.View Leaderboard\n3.View Answers\n4.Exit\n"))
if menu == 1:
    keyboard_warriors()


if menu == 3:
    print("\nAnswers:""\n"+str(answer_r))

if menu == 4:
    user_input = input("Do you want to exit? y/n")
    if user_input == "y" or "yes":
        SystemExit


#for i in range((len(leaderboard)))







    





