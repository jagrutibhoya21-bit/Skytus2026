# Quiz Game Project in Python

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit",
                    "C. Computer Personal Unit", "D. Central Program Unit"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
    "question": "Which of the following is a mutable data type in Python?",
    "options": ["A. List", "B. Tuple", "C. String", "D. int"],
    "answer": "A"
},
{
    "question": "What is the output of print(2 * 3 ** 2)?",
    "options": ["A. 36", "B. 18", "C. 12", "D. 9"],
    "answer": "B"
},
{
    "question": "Which keyword is used to create a class in Python?",
    "options": ["A. class", "B. def", "C. object", "D. struct"],
    "answer": "A"
},
{
    "question": "What is the correct way to import the math module?",
    "options": ["A. import math", "B. include math", "C. using math", "D. require math"],
    "answer": "A"
},
{
    "question": "Which method adds an item to the end of a list?",
    "options": ["A. append()", "B. insert()", "C. add()", "D. push()"],
    "answer": "A"
},
{
    "question": "Which keyword is used to define a function in Python?",
    "options": ["A. func", "B. define", "C. def", "D. function"],
    "answer": "C"
},
{
    "question": "Which data type is used to store text in Python?",
    "options": ["A. int", "B. float", "C. str", "D. char"],
    "answer": "C"
},
{
    "question": "Which symbol is used for comments in Python?",
    "options": ["A. //", "B. #", "C. <!-- -->", "D. **"],
    "answer": "B"
},
{
    "question": "Which function is used to display output in Python?",
    "options": ["A. display()", "B. print()", "C. show()", "D. output()"],
    "answer": "B"
},
{
    "question": "Which keyword is used for conditional statements?",
    "options": ["A. if", "B. for", "C. while", "D. def"],
    "answer": "A"
},
{
    "question": "Which loop is used to iterate over a sequence in Python?",
    "options": ["A. if", "B. while", "C. for", "D. loop"],
    "answer": "C"
},
{
    "question": "What is the correct file extension for Python files?",
    "options": ["A. .java", "B. .py", "C. .python", "D. .p"],
    "answer": "B"
},
{
    "question": "Which function is used to get input from the user?",
    "options": ["A. get()", "B. input()", "C. scan()", "D. read()"],
    "answer": "B"
},
{
    "question": "Which operator is used for exponentiation in Python?",
    "options": ["A. ^", "B. **", "C. %", "D. //"],
    "answer": "B"
},
{
    "question": "Which data structure is used to store key-value pairs?",
    "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
    "answer": "D"
}



    
]

score = 0

print("===== QUIZ GAME =====")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is", q["answer"])

print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Better luck next time!")
