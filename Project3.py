# these are the things being tracked:

Fall_points = 0
Winter_points = 0
Spring_points = 0
Summer_points = 0

# these are all the questions:

answer0 = input("Take my test? (A) Yes, (Z) No ")
if answer0 == "A" or answer0 == "a":
    print("Okay.")
    answer1 = input("Question one: Would you rather,(A) wear a sweater, (B) wear a coat, (C) wear a tee shirt, (D) or wear a tank top?")
    if answer1 == "A" or answer1 == "a":
        Fall_points += 1
    elif answer1 == "B" or answer1 == "b":
        Winter_points += 1
    elif answer1 == "C" or answer1 == "c":
        Spring_points =+ 1
    elif answer1 == "D" or answer1 == "d":
        Summer_points += 1

    answer2 = input("Question two: would you rather, (A) drink tea, (B) drink hot chocolate, (C) drink water, (D) or drink soda?")
    if answer2 == "A" or answer2 == "a":
        Fall_points += 1
    elif answer2 == "B" or answer2 == "b":
        Winter_points += 1
    elif answer2 == "C" or answer2 == "c":
        Spring_points += 1
    elif answer2 == "D" or answer2 == "d":
        Summer_points += 1

    answer3 = input("Question three: would you rather eat, (A) Punkin pie, (B) Blueberry pie, (C) Peach pie, (D) or Apple pie?")
    if answer3 == "A" or answer3 == "a":
        Fall_points += 1
    elif answer3 == "B" or answer3 == "b":
        Winter_points += 1
    elif answer3 == "C" or answer3 == "c":
        Spring_points += 1
    elif answer3 == "D" or answer3 == "d":
        Summer_points += 1

    answer4 = input("Question four: would you rather wear, (A) a scarf, (B) gloves, (C) an umbrella, (D) or sunglasses?")
    if answer4 == "A" or answer4 == "a":
        Fall_points += 1
    elif answer4 == "B" or answer4 == "b":
        Winter_points += 1
    elif answer4 == "C" or answer4 == "c":
        Spring_points += 1 
    elif answer4 == "D" or answer4 == "d":
        Summer_points += 1

    answer5 = input("Question five: would you rather, (A) jump in a pile of leafs, (B) a pile of snow, (C) a flower bed, (D) or a lake?")
    if answer5 == "A" or answer5 == "a":
        Fall_points += 1
    elif answer5 == "B" or answer5 == "b":
        Winter_points += 1
    elif answer5 == "C" or answer5 == "c":
        Spring_points += 1
    elif answer5 == "D" or answer5 == "d":
        Summer_points += 1

    answer6 = input("Question six: would you rather, (A) it'd be cold but sunny, (B) cold and cloudy, (C) wet but warm, (D) or dry and sunny?")
    if answer6 == "A" or answer6 == "a":
        Fall_points += 1
    elif answer6 == "B" or answer6 == "b":
        Winter_points += 1
    elif answer6 == "C" or answer6 == "c":
        Spring_points += 1
    elif answer6 == "D" or answer6 == "d":
        Summer_points += 1

    answer7 = input("Question seven: what color combo do you like the best, (A) Orange, Brown, Red, (B) White, Blue, Navy, (C) Pink, Yellow, Green, (D) Yellow, Baby blue, Hot pnk?")
    if answer7 == "A" or answer7 == "a":
        Fall_points += 1
    elif answer7 == "B" or answer7 == "b":
        Winter_points += 1
    elif answer7 == "C" or answer7 == "c":
        Spring_points == 1
    elif answer7 == "D" or answer7 == "d":
        Summer_points += 1

    answer08 = input("Questions eight: what is your favorite holiday out of these choices, (A) Halloween, (B) Christmas, (C) Easter, or (D) Fourth of July?")
    if answer08 == "A" or answer08 == "a":
        Fall_points += 1
    if answer08 == "B" or answer08 == "b":
        Winter_points += 1
    if answer08 == "C" or answer08 == "c":
        Spring_points += 1
    if answer08 == "D" or answer08 == "d":
        Summer_points +=1

# this is the end of the quiz, and where all teh points are added up:
        
    if Fall_points > Winter_points and Fall_points > Spring_points and Fall_points > Summer_points:
        print("You are a Fall person!! :D")
    elif Winter_points > Fall_points and Winter_points > Spring_points and Winter_points > Summer_points:
        print("You are a winter person! :)")
    elif Spring_points > Winter_points and Spring_points > Summer_points and Spring_points > Fall_points:
        print("You are a Spring person!")
    elif Summer_points > Spring_points and Summer_points > Fall_points and Summer_points > Winter_points:
         print("You are a Summer person.")

# this is if there are any ties in points:

    if Fall_points == Winter_points and Fall_points > Spring_points and Fall_points > Summer_points:
        answer8 = input("You have tied between two things. would you rather, (A) Sit outside with a blanket, or (B) Sit by a fireplace?")
        if answer8 == "A" or answer8 == "a":
            Fall_points += 1
        elif answer8 == "B" or answer8 == "b":
            Winter_points += 1

    if Fall_points == Spring_points and Fall_points > Summer_points and Fall_points > Winter_points:
        answer9 = input("You have tied between two things. would you rather, (A) Sit outside with a blanket, or (B) Sit by your window watching the early morning?")
        if answer9 == "A" or answer9 == "a":
            Fall_points += 1
        elif answer9 == "B" or answer9 == "b":
            Spring_points += 1
            
    if Fall_points == Summer_points and Fall_points > Winter_points and Fall_points > Spring_points:
        answer9 = input("You have tied between two things. Would you rather, (A) Sit outside with a blanket, or (B) Sit on warm sand on teh beach?")
        if answer9 == "A" or answer9 == "a":
            Fall_points += 1
        elif answer9 == "B" or answer9 == "b":
            Summer_points += 1

    if Winter_points == Spring_points and Winter_points > Summer_points and Winter_points > Fall_points:
        answer10 = input("You have tied between two things. would you rather, (A) Sit by a fireplace, or (B) Sit by your window watching the early morning?")
        if answer10 == "A" or answer10 == "a":
            Winter_points += 1
        elif answer10 == "B" or answer10 == "b":
            Spring_points +=1

    if Winter_points == Summer_points and Winter_points > Spring_points and Winter_points > Fall_points:
        answer11 = input("You have tied between two things. would you rather, (A) Sit by a fireplace, or (B) Sit on warm sand on teh beach?")
        if answer11 == "A" or answer11 == "a":
            Winter_points += 1
        elif answer11 == "B" or answer11 == "b":
            Summer_points += 1

    if Summer_points == Spring_points and Summer_points > Fall_points and Summer_points > Winter_points:
        answer12 = input("You have tied between two things. would you rather, (A) Sit on warm sand on teh beach, or (B) Sit by your window watching the early morning?")
        if answer12 == "A" or answer12 == "a":
            Summer_points += 1
        elif answer12 == "B" or answer12 == "b":
            Spring_points +=1

# this is apart of the of the very first question:

if answer0 == "Z" or answer0 == "z":
    print("Then why are you even playing this?")