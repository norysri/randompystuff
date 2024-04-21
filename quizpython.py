
questions = ("Who won the baloon d'or in 2007?", 
             "When did Fulham come back to the premier league?",
             "Who did Abyusif featured the most on his songs?", 
             "When did the naksa happen?")
options = (("a. kaka"," b. messi", "c. rooney"), ("a. 2018","b. 2017", "c. 2021"), 
           ("a. abo el anwar", "b. marwan moussa", "c. santa") , ("a. 1948", "b. 1967", "c. 1973"))
answers = ("a", "c", "a", "b")
guesses = []
score = 0 
question_no = 0

while True: 
   x=input("Welcome to Wquiz, press a to start ")
   if x.lower() == "a":
       break 

for i in range(len(questions)): 
    x = input(f"{questions[i]}, {options[i]}")
    guesses.append(x)
    if guesses[i] == answers[i]:
        print("CORRECT!")
        score += 1 
    else:
       print(f"sadly your answer is wrong")
print(f"we done! your score is {score} out of {len(questions)}")

