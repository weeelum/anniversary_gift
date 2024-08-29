from classQuestion import Question, ChoiceQuestion, TrueFalse

"""Initialize song questions."""
q0 = ChoiceQuestion(
    f"\nQ1. What is Seattle's metropolitan population?",
    "A. 5.6 million",
    "B. 10 million",
    "C. 0",
    "D. 4.02 million"
)
q0_ans = "D"

q1 = ChoiceQuestion(
    f"\nQ2. Who is Luna?",
    "A. My cat :3",
    "B. A gremlin from Middle Earth",
    "C. The greatest wizard who ever lived",
    "D. A little pooper"
)
q1_ans = "A"

q2 = Question(
    "\nQ3. To receive this next song, please enter the secret code (hint: it "
    "takes two to pucker up)"
)
q2_ans = "😚"

q3 = ChoiceQuestion(
    "\nQ4. Where are we going to live next year after your lease ends?",
    "A. Somewhere in Florida 🌦️",
    "B. Somewhere in Georgia 🍑",
    "C. Somewhere in Washington 🌧️",
    "D. Wherever works best for us 😊"
)
q3_ans = "D"

q4 = Question(
    "\nQ5. Complete these song lyrics:\n"
    "Hang all the mistletoe\n"
    "I'm gonna get to know you better ______________"
)
q4_ans = "this Christmas"

q5 = Question(
    "\nQ6. Here's some Python code:\n\n"

    "def greeting(name):\n"
    "   print(f'Hello, {name}!')"
    "\nWhat will the output be if you call this function with your name as an "
    "argument and run it?"
)
q5_ans = "Hello, Gabby!"

q6 = ChoiceQuestion(
    "\nQ7. I love going out with you and being able to simply stand next to "
    "you. Is this: ",
    "A. True",
    "B. False",
    "C. Very true",
    "D. I've never heard of this, ever. 🤨"
)
q6_ans = "A"

q7 = ChoiceQuestion(
    "\nQ8. Am I afraid of heights?",
    "A. True",
    "B. False",
    "C. Maybe?",
    "D. I know nothing."
)
q7_ans = "A"

q8 = ChoiceQuestion(
    "\nQ9. What is your favorite kind of flower?",
    "A. Roses",
    "B. Baby's Breath",
    "C. Orchids",
    "D. Tulips"
)
q8_ans = "B"

q9 = ChoiceQuestion(
    "\nQ10. Who is the greatest animated character of all time?",
    "A. Uncle Iroh",
    "B. Spongebob",
    "C. Shrek",
    "D. Mickey Mouse"
)
q9_ans = "C"

q10 = ChoiceQuestion(
    "\nQ11. 'Welcome to the Salty Spitoon. How tough are ya?'",

    "A. You got a new bottle of ketchup?",

    "B. Super Weenie Hut Jr's",

    "C. How tough am I... how tough am I??? I had a bowl of nails for "
    "breakfast this mornin'..... without any milk!",

    "D. I'll have you know I stubbed my toe last week while watering my spice "
    "garden, and I only cried for 20 minutes!"
)
q10_ans = "A"

q11 = ChoiceQuestion(
    "\nQ12. What is another word for 'thrilled'?",
    "A. Dampened",
    "B. Excited",
    "C. Disenchanted",
    "D. Dulled"
)
q11_ans = "B"

q12 = TrueFalse(
    "\nQ13. This app is working as intended so far:",
    "A. True",
    "B. False"
)
q12_ans = "A"

q13 = Question(
    "\nQ14. Remember the Artemis Fowl book series? What role did Butler act as "
    "for Artemis?"
)
q13_ans = "bodyguard"

q14 = ChoiceQuestion(
    "\nQ15. Complete these song lyrics:\n"
    "________ next to you",
    "A. Standing",
    "B. Sidding",
    "C. Eading",
    "D. Farding"
)
q14_ans = "A"


q_list = [
    q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14
]

ans_list = [
    q0_ans, q1_ans, q2_ans, q3_ans, q4_ans, q5_ans, q6_ans, q7_ans, q8_ans, 
    q9_ans, q10_ans, q11_ans, q12_ans, q13_ans, q14_ans
]