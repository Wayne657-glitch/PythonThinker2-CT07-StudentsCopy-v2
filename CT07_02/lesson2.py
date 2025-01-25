#toppings = ""
#while True:
    #topping = input("Enter a topping! (type 'end' to finish):")
   # if topping.lower() == 'end':
       # break
    #if toppings:
        #toppings += ", " + topping
    #else:
        #toppings = topping
    #print("Your pizza has the following toppings:" + toppings)
#print("You have chosen the following toppings: " + toppings)
questions = [
    "How many days are in 1 week?",
    "How many minutes are in 1 hour?",
    "How many seconds are in 1 minute?"
]
answers = [
    "7",
    "60",
    "60"
]

question_count = 0
score = 0
fail_count = 0
max_fails = 5

while question_count < 3:
    answer = input(questions[question_count] + " (type 'skip' to skip): ")
    
    if answer.lower() == 'skip':
        print("Question skipped.")
        question_count += 1
        continue
    
    if answer == answers[question_count]:
        print("Correct!")
        score += 1
        question_count += 1
        fail_count = 0  
    else:
        print("Incorrect. The correct answer is " + answers[question_count] + ".")
        fail_count += 1
        if fail_count >= max_fails:
            print("You have been disqualified after failing 5 times.")
            break

if fail_count < max_fails:
    print("Thank you for answering the questions!")
    print("Your final score is: " + str(score))

