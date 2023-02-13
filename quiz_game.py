def new_game():
    guesses=[]
    question_num=1
    correct_guess=0

    for key in questions:
        print("------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("choose the correct ans\n")
        guess=guess.upper()
        guesses.append(guess)

        correct_guess+=check_ans(questions.get(key),guess)
        question_num+=1
    display_scores(correct_guess,guesses)

def check_ans(answer,guess):
    if answer==guess:
        print("correct answer!!")
        return 1
    else:
        print("incorrect answer:(")
        return 0

def display_scores(correct_guess,guess):
    print("----------------------------------------------------")
    print("result is:")
    print("======================================================")
    print("answers are:",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("guessed answers:")    
    for i in guess:
        print(i,end=" ")
    print()

    score=int((correct_guess/len(questions))*100)
    print("your score is:"+str(score)+"%")


def play_again():
    response=input("wanna play again? yes or no  ")
    response=response.upper()

    if response=="YES":
        return True
    else:
        return False





questions={
    "full form of html is:":"A",
    "full form of css is:":"B",
    "html is used for:":"C",
    "css is used for:":"C",
}

options=[["A. hyper text markup language","B. hyper text makup language","C. hello text markup language","D. hyper texture markup language"]
,["A. casper cading style","B. casper cading stylesheet","C. copy sheet and sheets","D. none of the above"],
["A. creating utensils","B. creating computers","C. creating web pages","D. all of these"],
["A. hyper text markup language","B. making home designs","C. styling web pages","D. adding functions to weeb page"]]


new_game()

while play_again():
    new_game()


print("byeeee!!")

