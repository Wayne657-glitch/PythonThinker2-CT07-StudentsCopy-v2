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
question_count = 0
while question_count < 3:
    answer = input(questions[question_count] + " ")
    if answer == answers[question_count]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is " + answers[question_count] + ".")
    
    question_count += 1

print("Thank you for answering the questions!")
        

