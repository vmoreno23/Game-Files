def Chapter_1():
    choices = ["1", "2", "3", "4"]

    print("2 days have passed since the unknown contagious virus infected the first human and widespread chaos amongst neighboring cities. The virus turned the living into the undead. Time to find more supplies")

    user_input = ""
    
    print("You wake up in your home where you are barricaded from the outdoor threats. There are no survivors on your street. You remember the neighbor gave you keys to his house before he left, but no promising there will be supplies")
    
    while user_input not in choices:
        print("""
        Options:
        1. Check current supplies
        2. Check the news media
        3. Leave your home to search neighbor’s home
        4. Leave home to search for resources
        """)

        if user_input == "1":
            print("You have little food and water, a pocket knife, and a small backpack")
        elif user_input == "2":
            print("You are informed that the west coast is overtaken by the virus and all survivors are order to take shelter where they can. The military is sending teams to round up survivors")
        elif user_input == "3":
            print("You find a crowbar")
            global crowbar #User finds crowbar, final program will announce crowbar = False
            Chapter_2()
        elif user_input == "4":
            Chapter_2()
        else:
            print("Enter a valid option")

def Chapter_2():
    choices = ["1", "2", "3"]

    print("After sneaking through your block, you find the local market where resources may be in abundance. The undead monsters you tried to avoid on your street fill the neighborhood")

    user_input = ""

    print("The front door of the market is boarded up, but there is a side entrance. There are screams heard throughout the neighborhood, but one scream sounds eerily close by. A woman is trapped inside her vehicle as an undead mob try to pry doors open. She's a lost cause")

    while user_input not in choices:
        print("""
        Options:
        1. Attempt to save the woman
        2. Enter the market through side entrance
        3. Break window to enter market
        """)

        if user_input == "1":
            print("You use your knife to fend off the undead, but you are overrun and become the dead’s next meal")
            Chapter_4()
        elif user_input == "2":
            print("Door is locked")
            if crowbar: #crow was found from chapter 1
                print("You break in through side door and resources are gathered, hearing a loud bang you witness the woman from the car scream and run into the window of the market shattering it as she gets devoured. The noise attracts unwanted attention to you")
            else:
                Chapter_3()
        elif user_input == "3":
            print("Resources are gathered, but the noise attracted unwanted attention")
            Chapter_3()
        else:
            print("Enter a valid option")

def Chapter_3():
    choices = ["1", "2", "3"]

    print("You run for your life out of the market as the undead chase you")

    user_input = ""

    print("You quickly analyze your options of escape")

    while user_input not in choices:
        print("""
        Options:
        1. Fight off the undead
        2. Attempt escape through market side entrance 
        3. Exit through the broken window
        """)

        if user_input == "1":
            print("You fend off the undead and find a bite mark on your shoulder and forearm. You are taken over by the virus")
            Chapter_4()
        elif user_input == "2":
            print("The door is jammed; you get swarmed by the undead and become lunch")
            Chapter_4()
        elif user_input == "3":
            print("You escape with slight cuts bruises, but you manage to escape")
            Chapter_5()
        else:
            print("Enter a valid option")
            
def Chapter_4():
    choices = ["1", "2", "3"]

    print("Hours after becoming a meal for the undead, you gain control of your body once more. An unquenchable sense of hunger fogs your thoughts leaving you unable to speak")

    user_input = ""

    print("Your decomposing body is all you have left. Feeding on whatever you find. You make your way into the city")

    while user_input not in choices:
        print("""
        Options:
        1. Attack a group of 5 survivors
        2. Attack a lone teenage girl hiding
        3. Attack a military convoy heading to the city
        """)

        if user_input == "1":
            print("Assisted by a mob of undead you feast on 2 survivors, but the rest of the survivors avenge their fallen. They take out the mob including yourself")
            quit()
        elif user_input == "2":
            print("You underestimate the skills and survivability of the teenage girl, she puts an end to your suffering")
            quit()
        elif user_input == "3":
            print("You stood no chance against the power of the military")
            quit()
        else:
            print("Enter a valid option")
def Chapter_5():
    choices = ["1", "2", "3"]

    print("After escaping the market, you need to find shelter. There are flares shot from the city. You figure the city is where the military would start saving survivors")

    user_input = ""

    print("As daylight starts to fade, you think of ways to get closer to the city. You need to quickly get inside the city before you miss the military rescue. No time to waste")

    while user_input not in choices:
        print("""
        Options:
        1. Head to a nearby car dealership
        2. Head to your friend's house
        3. Head to a nearby gas station
        """)

        if user_input == "1":
            print("You find keys to a sports car with enough fuel to reach the city on time. The military rescues you and other survivors")
            quit()
        elif user_input == "2":
            print("You find your friend alive at his home. He tells you that you're welcome to stay until help arrives, he does not tell you he's received a bite from the undead, you unexpectedly get bitten by your friend")
            Chapter_4()
        elif user_input == "3":
            print("You find the remains of the gas station clerk and search the employee room. His car keys are still hanging. You take his car to reach the city and find the military pickup zone. They rescue you and other survivors")
            quit()
        else:
            print("Enter a valid option")


def main():
    if __name__ == "__main__":
      while True:
        print("Welcome to the Adventure Game!")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " +name+ ".")
        Chapter_1()
