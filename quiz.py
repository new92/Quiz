#Imports

import time

#End of imports 

#Program

name=input("Please enter your name: ")
print("Welcome ",name," to this quiz game !")
chapters=["Sports","Science","Animals","Geography","food","TV","Music"]
codes=["1010","1020","1030","1040","1050","1060","1070"]
print("Please pick a chapter: ")
for i in range(len(chapters)):
    print(chapters[i],codes[i])
time.sleep(6)
chapter=input("Please type the code of the chapter you want to start with: ")
"1010" == "sports"
"1020" == "science"
"1030" == "animals"
"1040" == "geography"
"1050" == "food"
"1060" == "TV"
"1070" == "Music"
#This is the Sports chapter 
if chapter == "1010": 
    print("So you have chosen Sports chapter :)")
    time.sleep(1)
    print("Okay then let's start !")
    time.sleep(2)
    #First question of sports
    print("First question: Which countrie has not missed one of the modern-day Olympics?")
    time.sleep(3)
    print("a) Greece b) Russia c) Bulgaria d) US")
    time.sleep(2)
    answer1=input("Please enter the answer here: ")
    if answer1 != "Greece": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Greece")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Second question of sports 
    print("Second question: Which country won the first-ever soccer World Cup in 1930?")
    time.sleep(3)
    print("a) Brazil b) Germany c) Uruguay d) Portugal")
    time.sleep(2)
    answer2=input("Please enter the answer here: ")
    if answer2 != "Uruguay": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Uruguay")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Third question of sports
    print("Third question: What sport is dubbed the 'king of sports'?")
    time.sleep(3)
    print("a) Basketball b) Volleyball c) Football d) Cricket")
    time.sleep(2)
    answer3=input("Please type the answer here: ")
    if answer3 != "Football": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Football")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fourth question of sports
    print("Fourth question: Dump, floater, and wipe are terms used in which team sport?")
    time.sleep(3)
    print("a) Football b) Basketball c) Volleyball d) Tennis")
    time.sleep(2)
    answer4=input("Please type the answer here: ")
    if answer4 != "Volleyball": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Volleyball")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fifth question of sports
    print("Fifth question: How many points did Michael Jordan score on his first NBA game?")
    time.sleep(3)
    print("a) 24 b) 8 c) 10 d) 16")
    time.sleep(2)
    answer5=input("Please type the answer here: ")
    if answer5 != 16: 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 16")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of sports
    print("Sixth question: Who has won more tennis grand slam titles?")
    time.sleep(3)
    print("a) Venus Williams b) Serena Williams")
    time.sleep(2)
    answer6=input("Please type the answer here: ")
    if answer6 != "Serena Williams": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Serena Williams")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Seventh question of sports
    print("Seventh question: Which is the only American Football team to go a whole season undefeated, including the Super Bowl?")
    time.sleep(3)
    print("a) Arizona Cardinals b) Detroit Lions c) Los Angeles Rams d) The Miami Dolphins")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != "The Miami Dolphins":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: The Miami Dolphins")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Eighth question of sports
    print("Eighth question: Which Former NBA Player Was Nicknamed “Agent Zero”?")
    time.sleep(3)
    print("a) Charles Barkley b) Clyde Drexler c) Patrick Ewing d) Gilbert Arenas")
    time.sleep(2)
    answer8=input("Please type the answer here: ")
    if answer8 != "Gilbert Arenas":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Gilbert Arenas")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Ninth question of sports
    print("Ninth question: What is the name of the professional ice hockey team based in Toronto, Canada?")
    time.sleep(3)
    print("a) Canadiens b) Maple Leafs c) Canucks d) Flames")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != "Maple Leafs":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Maple Leafs")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Tenth question of sports
    print("Tenth question: Who was the first female driver to score points in a Grand Prix ?")
    time.sleep(3)
    print("a) Lella Lombardi b) Divina Galica c) Giovanna Amati d) Desire Wilson")
    time.sleep(2)
    answer10=input("Please type your answer here: ")
    if answer10 != "Lella Lombardi": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Lella Lombardi")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
#This is the Science chapter 
elif chapter == "1020": 
    print("So you have chosen Science chapter :) ")
    time.sleep(1)
    print("Okay then let's start ! ")
    time.sleep(2)
    #First question of science
    print("First question: In what type of matter are atoms most tightly packed ?")
    time.sleep(3)
    print("a) Solid b) Liquid c) Gase")
    time.sleep(2)
    answer1=input("Please type your answer here: ")
    if answer1 != "Solid": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Solid")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Second question of science
    print("Second question: What is the hottest planet in the solar system ?")
    time.sleep(3)
    print("a) Mercury b) Earth c) Venus d) Mars")
    time.sleep(2)
    answer2=input("Please type your answer here: ")
    if answer2 != "Venus": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Venus")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Third question of science
    print("Third question: What is the opposite of matter ?")
    time.sleep(3)
    answer3=input("Please type your answer here: ")
    time.sleep(2)
    if answer3 != "Antimatter":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Antimatter")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fourth question of science
    print("Fourth question: Which of Newton's Laws states that 'for every action, there is an equal and opposite reaction' ?")
    time.sleep(3)
    print("a) The First Law b) The Second Law c) The Third Law d) None of the above")
    time.sleep(2)
    answer4=input("Please type your answer here: ")
    if answer4 != "The Third Law":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: The Third Law")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fifth question of science
    print("Fifth question: In 2004 what was discovered on the island of Flores in Indonesia ?")
    time.sleep(3)
    print("a) Remains of a hobbit-size human b) Remains of an ancient dinosaur c) Remains of a mutated human d) Nothing")
    time.sleep(2)
    answer5=input("Please type your answer here: ")
    if answer5 != "Remains of a hobbit-size human": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Remains of a hobbit-size human")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of science
    print("Sixth question: What is the nearest planet to the sun ?")
    time.sleep(3)
    print("a) Mars b) Earth c) Mercury d) Jupiter")
    time.sleep(2)
    answer6=input("Please type the answer here: ")
    if answer6 != "Mercury":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Mercury")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move to on the next question !")
        time.sleep(2)
    #Seventh question of science 
    print("Secenth question: What color is your blood when it's inside your body ?")
    time.sleep(3)
    print("a) Blue b) Yellow c) Red d) Black")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != "Red":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Red")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Eighth question of science 
    print("Eighth question: Is Pluto a planet ?")
    time.sleep(3)
    print("a) Yes b) No")
    time.sleep(2)
    answer8=input("Please type the answer here: ")
    if answer8 != "No":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: No")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Ninth question of science
    print("Ninth question: How many teeth does an adult human have ?")
    time.sleep(3)
    print("a) 30 b) 26 c) 28 d) 32")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != 32: 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 32")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Tenth question of science 
    print("Tenth question: What tissues connect the muscles to the bones ?")
    time.sleep(3)
    answer10=input("Please type the answer here: ")
    if answer10 != "Tendons": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Tendons")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
#This is the Animals chapter
elif chapter == "1030":
    print("So you have chosen Animals chapter :)")
    time.sleep(1)
    print("Okay then let's start !")
    time.sleep(2)
    #First question of animals
    print("First question: Which is the loudest animal on Earth ?")
    time.sleep(3)
    print("a) Lion b) Whale c) Elefant d) Bear")
    time.sleep(2)
    answer1=input("Please type the answer here: ")
    if answer1 != "Whale":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Whale")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Second question of animals 
    print("Second question: How many hearts does an octopus have ?")
    time.sleep(3)
    print("a) 5 b) 2 c) 3 d) 8")
    time.sleep(2)
    answer2=input("Please type the answer here: ")
    if answer2 != 3:
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 3")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Third question of animals
    print("Third question: The unicorn is the national animal of which country ?")
    time.sleep(3)
    print("a) US b) Russia c) Germany d) Scotland")
    time.sleep(2)
    answer3=input("Please type the answer here: ")
    if answer3 != "Scotland": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Scotland")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fourth question of animals 
    print("Fourth question: What are the folds of skin on a cat's ears called ?")
    time.sleep(3)
    print("a) Henry's pockets b) Pockets c) Henry d) None of the above")
    time.sleep(2)
    answer4=input("Please type the answer here: ")
    if answer4 != "Henry's pockets":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Henry's pockets")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fifth question of animals
    print("Fifth question: A group of ravens is known as ?")
    time.sleep(3)
    answer5=input("Please type the answer here: ")
    if answer5 != "Unkindness":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Unkindness")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of animals 
    print("Sixth question: How many legs does a spider have ?")
    time.sleep(3)
    print("a) 4 b) 6 c) 8 d) 10")
    time.sleep(2)
    answer6=input("Please type the answer here: ")
    if answer6 != 8: 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 8")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Seventh question of animals 
    print("Seventh question: How many monthes do elephant pregnancies last ?")
    time.sleep(3)
    print("a) 22 b) 18 c) 14 d) 10")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != 22: 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 22")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move to the next question !")
        time.sleep(2)
    #Eighth question of animals 
    print("Eighth question: What type of animal is a Flemish giant ?")
    time.sleep(3)
    print("a) Crocodile b) Bear c) Rabbit d) Reindeer")
    time.sleep(2)
    answer8=input("Please type the answer here: ")
    if answer8 != "Rabbit":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Rabbit")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move to the next question !")
        time.sleep(2)
    #Ninth question of animals 
    print("Ninth question: The name of which African animal means 'river horse' ?")
    time.sleep(3)
    print("a) Sea Horse b) Crocodile c) Hippopotamus d) Fish")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != "Hippopotamus":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Hippopotamus")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move to the next question !")
        time.sleep(2)
    #Tenth question of animals 
    print("Tenth question: What mammals lay eggs ?")
    time.sleep(3)
    print("a) Platypus b) Lion c) Raccoon d) Otter")
    time.sleep(2)
    answer10=input("Please type the answer here: ")
    if answer10 != "Platypus":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Platypus")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
#This is the Geography chapter 
elif chapter == "1040": 
    print("So you have chosen Geography chapter :)")
    time.sleep(1)
    print("Okay then let's start !")
    time.sleep(2)
    #First question of geography
    print("First question: What is the Earth's largest continent ?")
    time.sleep(3)
    print("a) Asia b) Africa c) Europe d) North America")
    time.sleep(2)
    answer1=input("Please type the answer here: ")
    if answer1 != "Asia": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Asia")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question")
        time.sleep(2)
    #Second question of geography 
    print("Second question: What's the smallest country in the world ?")
    time.sleep(3)
    print("a) Monaco b) San Marino c) Tuvalu d) Vatican City")
    time.sleep(2)
    answer2=input("Please type the answer here: ")
    if answer2 != "Vatican City":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Vatican City")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question")
        time.sleep(2)
    #Third question of geography
    print("Third question: Area 51 is located in which US state ?")
    time.sleep(3)
    print("a) Alabama b) Nevada c) Arizona d) California")
    time.sleep(2)
    answer3=input("Please type the answer here: ")
    if answer3 != "Nevada": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Nevada")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question")
        time.sleep(2)
    #Fourth question of geography 
    print("Fourth question: What country touches the Indian Ocean, the Arabian Sea, and the Bay of Bengal ?")
    time.sleep(3)
    print("a) Pakistan b) India c) Sri Lanka d) Myanmar")
    time.sleep(2)
    answer4=input("Please type the answer here: ")
    if answer4 != "India": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: India")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question")
        time.sleep(2)
    #Fifth question of geography 
    print("Fifth question: What's the city with the most diversity in terms of language ?")
    time.sleep(3)
    print("a) London b) Beijing c) New York d) Paris")
    time.sleep(2)
    answer5=input("Please type the answer here: ")
    if answer5 != "New York":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: New York")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of geography
    print("Sixth question: The ancient Phoenician city of Constantine is located in what modern-day Arab country ?")
    time.sleep(3)
    print("a) Algeria b) Egypt c) Jordan d) Libya")
    time.sleep(2)
    answer6=input("Please type the answer here: ")
    if answer6 != "Algeria":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Algeria")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Seventh question of geography 
    print("Seventh question: Which country borders 14 nations and crosses 8 time zones ?")
    time.sleep(3)
    print("a) China b) Australia c) US d) Russia")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != "Russia": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Russia")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Eighth question of geography
    print("Eighth question: Havana is the capital of which country ?")
    time.sleep(3)
    print("a) Brazil b) Cuba c) Dominican Republic d) Jamaica")
    time.sleep(2)
    answer8=input("Please type the answer here: ")
    if answer8 != "Cuba":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Cuba")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Ninth question of geography
    print("Ninth question: What country has the most natural lakes ?")
    time.sleep(3)
    print("a) US b) Norway c) Sweden d) Canada")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != "Canada":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Canada")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Tenth question of geography
    print("Tenth question: In what country would you find Lake Bled ?")
    time.sleep(3)
    print("a) Slovenia b) Germany c) Russia d) Japan")
    time.sleep(2)
    answer10=input("Please type the answer here: ")
    if answer10 != "Slovenia": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Slovenia")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
#This is the Food chapter
elif chapter == "1050":
    print("So you have chosen Food chapter :)")
    time.sleep(1)
    print("Okay then let's start !")
    time.sleep(2)
    #First question of food 
    print("First question: Which is the rarest M&M color ?")
    time.sleep(3)
    print("a) Yellow b) Blue c) Red d) Brown")
    time.sleep(2)
    answer1=input("Please type the answer here: ")
    if answer1 != "Brown":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Brown")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Second question of food
    print("Second question: What is the common name for dried plums?")
    time.sleep(3)
    print("a) Prunes b) Moyer c) Friar d) Greengage")
    time.sleep(2)
    answer2=input("Please type the answer here: ")
    if answer2 != "Prunes":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Prunes")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Third question of food
    print("Third question: Which country consumes the most chocolate per capita ?")
    time.sleep(3)
    print("a) Luxembourg b) Germany c) Switzerland d) Canada")
    time.sleep(2)
    answer3=input("Please type the answer here: ")
    if answer3 != "Switzerland": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Switzerland")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fourth question of food 
    print("Fourth question: What is the name given to Indian food cooked over charcoal in a clay oven ?")
    time.sleep(3)
    print("a) Palak paneer b) Tandoori c) Fish curry d) Chana masala")
    time.sleep(2)
    answer4=input("Please type the answer here: ")
    if answer4 != "Tandoori":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Tandoori")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fifth question of food 
    print("Fifth question: What was the first soft drink in space ?")
    time.sleep(3)
    print("a) Fanta b) Pepsi c) Sprite d) Coca Cola")
    time.sleep(2)
    answer5=input("Please type the answer here: ")
    if answer5 != "Coca Cola":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Coca Cola")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of food
    print("Sixth question: What is the most consumed manufactured drink in the world?")
    time.sleep(3)
    print("a) Tea b) Orange Juice c) Milk d) Coca Cola")
    time.sleep(2)
    answer6=input("Please type the answer here: ")
    if answer6 != "Tea":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Tea")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Seventh question of food 
    print("Seventh question: Which is the only edible food that never goes bad ?")
    time.sleep(3)
    print("a) Legumes b) Meat c) Honey d) Cereals")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != "Honey":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Honey")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Eighth question of food
    print("Eigthth question: Which country invented ice cream ?")
    time.sleep(3)
    print("a) China b) France c) US d) Belgium")
    time.sleep(2)
    answer8=input("Please type the answer here: ")
    if answer8 != "China":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: China")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Ninth question of food 
    print("Ninth question: 'Hendrick’s,' 'Larios,' and 'Seagram’s' are some of the best-selling brands of which spirit ?")
    time.sleep(3)
    print("a) Vodka b) Bourbon c) Gin d) Scotch")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != "Gin":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Gin")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Tenth question of food
    print("Tenth question: From which country does Gouda cheese originate ?")
    time.sleep(3)
    print("a) Netherlands b) Italy c) France d) Monaco")
    time.sleep(2)
    answer10=input("Please type the answer here: ")
    if answer10 != "Netherlands":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Netherlands")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
#This is the TV chapter
elif chapter == "1060":
    print("So you have chosen the TV chapter :)")
    time.sleep(1)
    print("Okay then let's start !")
    time.sleep(2)
    #First question of TV
    print("First question: What was the first toy to be advertised on television ?")
    time.sleep(3)
    print("a) Frisbee b) Furby c) Mr Potato Head d) Slinky")
    time.sleep(2)
    answer1=input("Please type the answer here: ")
    if answer1 != "Mr Potato Head":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Mr Potato Head")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Second question of TV
    print("Second question: What was the first feature-length animated movie ever released ?")
    time.sleep(3)
    print("a) Bambi b) Snow White and the Seven Dwarfs c) Dumbo d) Fantasia")
    time.sleep(2)
    answer2=input("Please type the answer here: ")
    if answer2 != "Snow White and the Seven Dwarfs": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Snow White and the Seven Dwarfs")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Third question of TV
    print("Third question: What TV series showed the first interracial kiss on American network television ?")
    time.sleep(3)
    print("a) Family Affair b) Mission Impossible c) Batman d) Star Trek")
    time.sleep(2)
    answer3=input("Please type the answer here: ")
    if answer3 != "Star Trek":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Star Trek")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fourth question of TV
    print("Fourth question: Which was the name of one of the main characters from the TV serie 'Golden Girls' that ran from 1985-1992 ?")
    time.sleep(3)
    print("a) Olivia b) Emma c) Mia d) Sophia")
    time.sleep(2)
    answer4=input("Please type the answer here: ")
    if answer4 != "Sophia":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Sophia")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #FIfth question of TV 
    print("Fifth question: Who created Sherlock Holmes ?")
    time.sleep(3)
    print("a) Arthur Conan Doyle b) Agatha Christie c) Andrew Lane d) Oscar Wilde")
    time.sleep(2)
    answer5=input("Please type the answer here: ")
    if answer5 != "Arthur Conan Doyle": 
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Arthur Conan Doyle")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of TV
    print("Sixth question: What awards has an EGOT winner won ?")
    time.sleep(3)
    print("a) Emmy b) Grammy c) Oscar d) Tony e) All the mentioned above")
    time.sleep(2)
    answer6=input("Please type the answer here: ")
    if answer6 != "All the mentioned above":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: All the mentioned above")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Seventh question of TV
    print("Seventh question: Which member of the Beatles married Yoko Ono ?")
    time.sleep(3)
    print("a) Ringo Starr b) George Harrison c) John Lennon d) Paul McCartney")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != "John Lennon":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: John Lennon")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Eigthth question of TV
    print("Eigthth question: What are the names of Cinderella’s stepsisters ?")
    time.sleep(3)
    print("a) Anastasia b) Drizella c) Emma d) Sophia e) a & b f) c & d")
    time.sleep(2)
    answer8=input("Please type the answer here: ")
    if answer8 != "a & b":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: a & b")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Ninth question of TV
    print("Ninth question: What famous US festival hosted over 350,000 fans in 1969 ?")
    time.sleep(3)
    print("a) Bath Festival of Blues b) Woodstock c) Denver Pop Festival d) Laurel Pop Festival")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != "Woodstock":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Woodstock")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Tenth question of TV
    print("Tenth question: The biggest selling music single of all time is ?")
    time.sleep(3)
    print("a) Peru b) House on Fire c) Down Under d) Candle in the Wind")
    time.sleep(2)
    answer10=input("Please type the answer here: ")
    if answer10 != "Candle in the Wind":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: ")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
#This is the Music chapter
elif chapter == "1070":
    print("So you have chosen the Music chapter :)")
    time.sleep(1)
    print("Okay then let's start !")
    time.sleep(2)
    #First question of music
    print("First question: Which English Sir has had No. l’s in the 50’s, 60’s, 70’s, 80’s and 90’s ?")   
    time.sleep(3)
    answer1=input("Please type the answer here: ")
    if answer1 != "Sir Cliff Richard":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Sir Cliff Richard")
        time.sleep(2)
    else: 
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Second question of Music
    print("Second question: Which rock band was founded by Trent Reznor in 1988 ?")
    time.sleep(3)
    answer2=input("Please type the answer here: ")
    if answer2 != "Nine Inch Nails":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Nine Inch Nails")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Third question of Music
    print("Third question: What is the name of the duet recorded by Robbie Williams and Gary Barlow in 2010 ?")
    time.sleep(3)
    answer3=input("Please type the answer here: ")
    if answer3 != "Shame":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Shame")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fourth question of Music
    print("Fourth question: Jimmy, Robert, John and John: can you identify this rock band from the first names of their original line-up ?")
    time.sleep(3)
    answer4=input("Please type the answer here: ")
    if answer4 != "Led Zeppelin":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Led Zeppelin")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Fifth question of Music
    print("Fifth question: In what year did The Clash release their iconic album London Calling ?")
    time.sleep(3)
    print("a) 1970 b) 1980 c) 1979 d) 1969")
    time.sleep(2)
    answer5=input("Please type the answer here: ")
    if answer5 != "1979":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 1979")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Sixth question of Music
    print("Sixth question: Which singer-songwriter had studio albums titled Hejira, Ladies of the Canyon and Blue ?")
    time.sleep(3)
    answer6=input("Please type the answer here: ")
    if answer6 != "Joni Mitchell":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Joni Mitchell")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Seventh question of Music
    print("Seventh question: In what year did Elvis Presley die ?")
    time.sleep(3)
    print("a) 1975 b) 1977 c) 1972 d) 1979")
    time.sleep(2)
    answer7=input("Please type the answer here: ")
    if answer7 != "1977":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 1977")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Eigthth question of Music
    print("Eigthth question: How many UK number ones did The Beatles have in total ?")
    time.sleep(3)
    print("a) 7 b) 9 c) 4 d) 11")
    answer8=input("Please type the answer here: ")
    if answer8 != "11":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 11")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Ninth question of Music
    print("Ninth question: In which year did the Spice Girls release Wannabe ?")
    time.sleep(3)
    print("a) 1996 b) 1990 c) 2000 d) 1993")
    time.sleep(2)
    answer9=input("Please type the answer here: ")
    if answer9 != "1996":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: 1996")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("Let's move on to the next question !")
        time.sleep(2)
    #Tenth question of Music
    print("Tenth question: Which music legend won the Nobel Prize for literature in 2016 ?")
    time.sleep(3)
    answer10=input("Please type the answer here: ")
    if answer10 != "Bob Dylan":
        print("Sorry wrong answer :( Don't worry tho you will make it :)")
        time.sleep(3)
        print("The correct answer is this: Bob Dylan")
        time.sleep(2)
    else:
        print("Correct ! :)")
        time.sleep(1)
        print("This is the end of the quiz ! Congrats !!")
        time.sleep(2)
else: 
    print("Sorry this is an invalid option :(")
    time.sleep(2)
    print("Please run again the program and type a valid option in order to start quiz")
    time.sleep(4)
#End of the program 
