import random

points = 0
lives = 3
inventory = []
level = 1
skills = {"strength": 1, "speed": 1, "Luck": 1}
goal_points = 500

print("You are an adventurer in the cursed town of Eldora, seeking the Legendary Crown!")

while lives > 0:
    if level < 1:
        level = 1
    if points < 0:
        points = 0

    print(f"level: {level} |  lives: {lives} | points: {points} | Inventory: {inventory} | Skills: {skills}")
    doors = "red, blue, green, yellow, black"
    if random.randint(1, 100) == 1:  
        doors += ", and a shimmering golden door"
    print(f"In front of you are doors: {doors}. Which one will you choose?")
    door = input("Which door do you choose? (red / blue / green / yellow / black ): ").lower()

    trap_chance = min(3 + level // 2, 7)

    if door == "red":
            print("The red door creaks ominously as you approach...")
            if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
                lives -= 1
                level -= 1
                points -= 10
                print("A trap snaps shut!")

            elif "shield" in inventory:
                print("Your shield saves you from a deadly trap!")
                inventory.remove("shield")

            elif random.randint(1, 10) <= 2:
                print("A wild thief appears!")
                while True:
                    fight = input("Do you want to fight or run? (fight / run): ").lower()

                    if fight == "fight":
                        if random.randint(1, 2) == 1 + skills["strength"] - 1:
                            lives += 1
                            points += 30
                            level += 1
                            inventory.append("thief's dagger")
                            print("you defected the thief and took his dagger!")
                            break
                        else: 
                            lives -= 1
                            level -= 1
                            points -= 30
                            print("The thief overpowered you!")
                            break

                    elif fight == "run":
                        if random.randint(1, 2) == 1 + skills["speed"] - 1:
                            points += 10
                            print("You escaped safely!")
                            break
                        else:
                            points -= 10
                            level -= 1
                            print("You failed to run and lost some loot!")
                            break
                    else:
                        print("Please choose 'fight' or 'run' only!")
                        break

            elif random.randint(1, 10) == 5: 
                print("A mysterious merchant appears from the mist!")
                trade = input("Trade 20 points for a shield? (yes/no): ").lower()
                if trade == "yes" and points >= 20:
                    points -= 20
                    inventory.append("shield")
                    print("You got a shield!")
                else:
                    print("The merchant vanishes into the shadows.")

            else:
                while True:
                        print("You found a tresure! Do you want to take it or continue the game?")
                        choice = input("yes or no: ")
                        if choice == "yes":
                            points += 50
                            level += 1
                            inventory.append("tresure")
                            print("You win the tresure!")
                            break
                        elif choice == "no":
                            points += 100
                            level += 2
                            inventory.append("magic tresure")
                            print("You Found magic tresure, you became sorcerer!")
                            break
                        else:
                            print("Please choose 'yes' or 'no' only")
                
    elif door == "blue":
                print("The blue door glows faintly as you step closer...")
                if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
                    lives -= 1
                    level -= 1
                    points -= 10
                    print("A hidden spike shoots out!")
                elif "shield" in inventory:
                    print("Your shield blocks a sudden attack!")
                    inventory.remove("shield")
                elif random.randint(1, 10) == 4:  
                    print("You find a locked chest with a riddle: 'I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?'")
                    answer = input("Your answer: ").lower()
                    if answer == "pencil":
                        points += 50
                        inventory.append("riddle key")
                        print("Correct! You unlocked the chest.")
                    else:
                        points -= 10
                        print("Wrong answer! The chest vanishes.")

                elif random.randint(1, 10) <= 2:
                    print("A wild thief appears!")
                    while True:
                        fight = input("Do you want to fight or run? (fight / run): ")

                        if fight == "fight":
                            if random.randint(1, 2) == 1 + skills["strength"] - 1:
                                lives += 1
                                points += 30
                                level += 1
                                inventory.append("thief's dagger")
                                print("you defected the thief and took his dagger!")
                                break
                            else: 
                                lives -= 1
                                level -= 1
                                points -= 30
                                print("The thief overpowered you!")
                                break

                        elif fight == "run":
                            if random.randint(1, 2) == 1 + skills["speed"] - 1:
                                points += 10
                                print("You escaped safely!")
                                break
                            else:
                                points -= 10
                                level -= 1
                                print("You failed to run and lost some loot!")
                                break
                        else:
                            print("Please choose 'fight' or 'run' only!")
                            break

                elif random.randint(1, 10) == 5: 
                        print("A mysterious merchant appears from the mist!")
                        trade = input("Trade 20 points for a shield? (yes/no): ").lower()
                        if trade == "yes" and points >= 20:
                            points -= 20
                            inventory.append("shield")
                            print("You got a shield!")
                        else:
                            print("The merchant vanishes into the shadows.")

                else:
                    while True:
                        print("You found $100!, DO you want to take it")
                        money = input("Do you want to take it? (yes/no): ").lower()
                        if money == "yes":
                            points += 20
                            level += 1
                            inventory.append("$100")
                            print("You take $100!")
                            break
                        elif money == "no":
                            level -= 1
                            points -= 10
                            print("You found a big dragon, you died.")
                            break
                        else:
                            print("Please choose 'yes' or 'no' only")

    elif door == "green":
            print("The green door hums with strange energy...")
            if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
                lives -= 1
                level -= 1
                points -= 10
                print("A pit opens beneath you!")
            elif "shield" in inventory:
                print("Your shield catches you from falling!")
                inventory.remove("shield")
            elif random.randint(1, 10) <= 2 and level >= 3:  
                print("A mighty dragon blocks your path!")
                while True:
                    fight = input("Fight or run? (fight/run): ").lower()
                    if fight == "fight" and "thief's dagger" in inventory:
                        if random.randint(1, 2) + skills["strength"] - 1 >= 2:
                            points += 100
                            level += 2
                            inventory.append("dragon scale")
                            print("You slayed the dragon!")
                            break
                        else:
                            lives -= 2
                            print("The dragon incinerates you!")
                            break
                    elif fight == "run":
                        if random.randint(1, 2) + skills["speed"] - 1 >= 2:
                            points += 20
                            print("You narrowly escaped the dragon!")
                            break
                        else:
                            lives -= 1
                            print("The dragon catches you!")
                            break
                    else:
                        print("Please choose 'fight' or 'run' only!")
            
            elif random.randint(1, 10) == 5: 
                print("A mysterious merchant appears from the mist!")
                trade = input("Trade 20 points for a shield? (yes/no): ").lower()
                if trade == "yes" and points >= 20:
                    points -= 20
                    inventory.append("shield")
                    print("You got a shield!")
                else:
                    print("The merchant vanishes into the shadows.")

            else:
                while True:
                    print("You enter a room and found $1,000,000! Do you want to take it or continue?")
                    million = input("Take it or continue? (yes/no): ").lower()
                    if million == "yes":
                        points += 50
                        level += 1
                        inventory.append("$1,000,000")
                        print("You win $1,000,000! Game over.")
                        break
                    elif million == "no":
                        points += 75
                        level += 2
                        print(f"You found room full of gold!")
                        gold = int(input("How many kilograms do you want to take? "))
                        inventory.append(f"{gold} kg of gold")
                        print(f"You win {gold} kg of gold!")
                        break
                    else:
                        print("Please choose 'yes' or 'no' only")                         

    elif door == "yellow":
                print("The yellow door shimmers like the sun...")
                if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
                    lives -= 1
                    level -= 1
                    points -= 10
                    print("A dart shoots from the wall!")
                elif "shield" in inventory:
                    print("Your shield deflects a dart!")
                    inventory.remove("shield")

                elif random.randint(1, 10) <= 2:
                    print("A wild thief appears!")
                    while True:
                        fight = input("Do you want to fight or run? (fight / run): ")

                        if fight == "fight":
                            if random.randint(1, 2) == 1 + skills["strength"] - 1:
                                lives += 1
                                points += 30
                                level += 1
                                inventory.append("thief's dagger")
                                print("you defected the thief and took his dagger!")
                                break
                            else: 
                                lives -= 1
                                level -= 1
                                points -= 30
                                print("The thief overpowered you!")
                                break

                        elif fight == "run":
                            if random.randint(1, 2) == 1 + skills["speed"] - 1:
                                points += 10
                                print("You escaped safely!")
                                break
                            else:  # <-- Changed to else
                                points -= 10
                                level -= 1
                                print("You failed to run and lost some loot!")
                                break

                elif random.randint(1, 10) == 5: 
                    print("A mysterious merchant appears from the mist!")
                    trade = input("Trade 20 points for a shield? (yes/no): ").lower()
                    if trade == "yes" and points >= 20:
                            points -= 20
                            inventory.append("shield")
                            print("You got a shield!")
                    else:
                            print("The merchant vanishes into the shadows.")

                else:
                        while True:
                            print("You found a secret tunnel! Do you want to enter?")
                            tunnel = input("yes or no: ")
                            if tunnel == "yes":
                                points += 100
                                level += 1
                                inventory.append("hidden city map")
                                print("You discover a hidden city!")
                                break
                            elif tunnel == "no":
                                level -= 1
                                print("You go back empty-handed.")
                                break
                            else:
                                    print("Please choose 'yes' or 'no' only")

    elif door == "black":
        print("The black door pulses with dark energy...")
        if random.randint(1, 10) <= trap_chance + 2: 
                lives -= 2
                print("A void swallows you!")
        elif "magic treasure" in inventory:
                points += 200
                level += 3
                inventory.append("shadow cloak")
                print("Your magic treasure unlocks the secrets of the void!")
        else:
                    points -= 50
                    level -= 2
                    print("The darkness drains your soul!")

    elif door == "golden" and "golden" in doors:
        print("The golden door radiates with unimaginable power...")
        while True:
                    choice = input("Enter the golden door? (yes/no): ").lower()
                    if choice == "yes":
                        points += 1000
                        inventory.append("golden crown")
                        print("You found the Golden Crown! You can end the game as a legend!")
                        end = input("End game now? (yes/no): ").lower()
                        if end == "yes":
                            print(f"Game ended! You retire as a legend!")
                            lives = 0  
                        break
                    elif choice == "no":
                        points += 50
                        level += 1
                        print("You resist the temptation and grow stronger!")
                        break
                    else:
                        print("Please choose 'yes' or 'no' only")

    else:
        lives -= 1
        level -= 1
        points -= 10
        print("You hesitated and stumbled into a trap!")
                    
    
    if level > 1 and level % 2 == 0:
        skill_choice = input("Improve a skill (strength/speed/luck): " ).lower()
        if skill_choice in skills:
            skills[skill_choice] += 1
            print(f"{skill_choice.capitalize()} improved to {skills[skill_choice]}!")
        else:
            print("Sorry your choise unkown! Try again")

    if points >= goal_points:
        print(f"\nCongratulations! You found the Legendary Crown with {points} points and {inventory} in your inventory!")
        break

    if lives <= 0:
        print(f"\nGame over! The cursed town claims another soul. Final points: {points}, Inventory: {inventory}")

