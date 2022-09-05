quiz = {
    "question1": {
        "question": "Vad är Sveriges huvudstad?",
        "answer": "Stockholm"
    },
    "question2": {
        "question": "Vad är blir 1 + 1?",
        "answer": "2"
    },
    "question3": {
        "question": "Vilken är Blekinges landskapsdjur?",
        "answer": "Ekoxen"
    },
    "question4": {
        "question": "Vad är Frankrikes huvudstad?",
        "answer": "Paris"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print("Your score is: " + str(score))

    else:
        print("Wrong")
        print("Your answer is : " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 4 questions correctly")
print("Your percentage is " + str(int(score/4 * 100)) + "%")
