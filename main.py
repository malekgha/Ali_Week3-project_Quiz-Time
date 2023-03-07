# Display the title (Geography Quiz) using ASCII Art and print(r"""""")
print(r"""
/      \                                                            /  |                       /      \           /  |          
/$$$$$$  |  ______    ______    ______    ______   ______    ______  $$ |____   __    __       /$$$$$$  | __    __ $$/  ________ 
$$ | _$$/  /      \  /      \  /      \  /      \ /      \  /      \ $$      \ /  |  /  |      $$ |  $$ |/  |  /  |/  |/        |
$$ |/    |/$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |/$$$$$$  |$$$$$$$  |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |$$$$$$$$/ 
$$ |$$$$ |$$    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |_ $$ |$$ |  $$ |$$ |  /  $$/  
$$ \__$$ |$$$$$$$$/ $$ \__$$ |$$ \__$$ |$$ |     /$$$$$$$ |$$ |__$$ |$$ |  $$ |$$ \__$$ |      $$ / \$$ |$$ \__$$ |$$ | /$$$$/__ 
$$    $$/ $$       |$$    $$/ $$    $$ |$$ |     $$    $$ |$$    $$/ $$ |  $$ |$$    $$ |      $$ $$ $$< $$    $$/ $$ |/$$      |
 $$$$$$/   $$$$$$$/  $$$$$$/   $$$$$$$ |$$/       $$$$$$$/ $$$$$$$/  $$/   $$/  $$$$$$$ |       $$$$$$  | $$$$$$/  $$/ $$$$$$$$/ 
                              /  \__$$ |                   $$ |                /  \__$$ |           $$$/                         
                              $$    $$/                    $$ |                $$    $$/                                         
                               $$$$$$/                     $$/                  $$$$$$/                                          

""")

#Display the rules of the game
print("Welcome to Geography Quiz! There are four True or False questions about the U.S. geography below. For each question please enter 'T' for True or 'F'' for False." )
#add space
print()

#add three questions in a tuple named questions
questions = ("Q1. Andes, is not the world's Longest Mountain Range.", "Q2. Amazon river is the world's longest river.", "Q3. Mississippi is the longest river in the North America.", "Q4. Mount McKinley is the highest point in the conterminous Uunited States." )

#add a variable for keeping the number of answers the user responded correctly
count = 0
answerRight = 1


#add three answers in another tuple
Correct_answers = ("F", "F", "T", "F")
user_answers = ("", "", "", "")

#add a line to get the numebr of question
numberOfQuestions = len(questions)
numberOfCorrect_answers = len(Correct_answers)
numberOfuser_answers = len(user_answers)

#add a loop to go through the questions' range
for index in range(numberOfQuestions):

  print(f"{questions[index]}")
  print()
  user_answers = input("Please enter 'T' for True and 'F' for false: ")
  print(f"Correct Answer: {Correct_answers[index]}")


  

#keep track of the questions the user has answered right

print(f"You got {answerRight} right.")
answerRight += 1
print("answerRight")






  

#Display the number of right answers out of the total number of questions


