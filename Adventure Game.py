import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GOLDEN = (255, 215, 0)
GRAY = (128, 128, 128)

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Cursed Town of Eldora Adventure")

# Fonts
font_large = pygame.font.SysFont('Arial', 32)
font_medium = pygame.font.SysFont('Arial', 24)
font_small = pygame.font.SysFont('Arial', 18)

# Game variables
points = 0
lives = 3
inventory = []
level = 1
skills = {"strength": 1, "speed": 1, "luck": 1}
goal_points = 500
current_door = None
message = "You are an adventurer in the cursed town of Eldora, seeking the Legendary Crown!"
show_input_box = False
input_text = ""
input_purpose = ""
game_active = True

# Helper functions
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_status_bar():
    # Draw status bar
    pygame.draw.rect(screen, GRAY, (20, 20, WIDTH-40, 80))
    draw_text(f"Level: {level} | Lives: {lives} | Points: {points}", font_medium, WHITE, WIDTH//2, 40)
    inv_text = f"Inventory: {', '.join(inventory) if inventory else 'Empty'}"
    draw_text(inv_text, font_small, WHITE, WIDTH//2, 70)
    skill_text = f"Skills: Strength: {skills['strength']}, Speed: {skills['speed']}, Luck: {skills['luck']}"
    draw_text(skill_text, font_small, WHITE, WIDTH//2, 90)

def draw_doors():
    # Draw doors
    door_width = WIDTH // 6
    door_height = HEIGHT // 2
    doors = ["red", "blue", "green", "yellow", "black"]
    
    # Check if golden door should appear
    if random.randint(1, 100) == 1:
        doors.append("golden")
    
    for i, door in enumerate(doors):
        x = (i+1) * WIDTH // (len(doors) + 1) - door_width // 2
        y = HEIGHT // 2 - door_height // 2
        
        # Set door color
        if door == "red":
            color = RED
        elif door == "blue":
            color = BLUE
        elif door == "green":
            color = GREEN
        elif door == "yellow":
            color = YELLOW
        elif door == "black":
            color = BLACK
        elif door == "golden":
            color = GOLDEN
        
        # Draw door
        pygame.draw.rect(screen, color, (x, y, door_width, door_height))
        pygame.draw.rect(screen, WHITE, (x, y, door_width, door_height), 2)
        
        # Add door handle
        pygame.draw.circle(screen, WHITE, (x + door_width - 15, y + door_height // 2), 5)
        
        # Write door name
        draw_text(door.capitalize(), font_small, WHITE, x + door_width // 2, y + door_height + 20)

def draw_message_box():
    # Draw message box
    pygame.draw.rect(screen, GRAY, (50, HEIGHT - 150, WIDTH - 100, 100))
    pygame.draw.rect(screen, WHITE, (50, HEIGHT - 150, WIDTH - 100, 100), 2)
    
    # Split message into multiple lines if too long
    words = message.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        if font_small.size(test_line)[0] < WIDTH - 150:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    
    lines.append(current_line)
    
    # Draw each line
    for i, line in enumerate(lines):
        draw_text(line, font_small, WHITE, WIDTH // 2, HEIGHT - 135 + i * 20)

def draw_input_box():
    if show_input_box:
        # Draw input box
        pygame.draw.rect(screen, WHITE, (150, HEIGHT - 200, WIDTH - 300, 40))
        pygame.draw.rect(screen, BLACK, (150, HEIGHT - 200, WIDTH - 300, 40), 2)
        
        # Draw text
        input_surface = font_small.render(input_text, True, BLACK)
        screen.blit(input_surface, (160, HEIGHT - 190))
        
        # Draw cursor
        if pygame.time.get_ticks() % 1000 < 500:
            cursor_pos = 160 + font_small.size(input_text)[0]
            pygame.draw.line(screen, BLACK, (cursor_pos, HEIGHT - 190), (cursor_pos, HEIGHT - 160), 2)
        
        # Draw input question
        draw_text(input_purpose, font_medium, WHITE, WIDTH // 2, HEIGHT - 220)

def process_door_red():
    global lives, level, points, message, show_input_box, input_purpose, inventory
    
    message = "The red door creaks ominously as you approach..."
    trap_chance = min(3 + level // 2, 7)
    
    if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
        lives -= 1
        level -= 1
        points -= 10
        message = "A trap snaps shut!"
    elif "shield" in inventory:
        message = "Your shield saves you from a deadly trap!"
        inventory.remove("shield")
    elif random.randint(1, 10) <= 2:
        message = "A wild thief appears!"
        show_input_box = True
        input_purpose = "Do you want to fight or run? (fight / run)"
    elif random.randint(1, 10) == 5:
        message = "A mysterious merchant appears from the mist!"
        show_input_box = True
        input_purpose = "Trade 20 points for a shield? (yes / no)"
    else:
        message = "You found a treasure! Do you want to take it or continue the game?"
        show_input_box = True
        input_purpose = "Take the treasure? (yes / no)"

def process_door_blue():
    global lives, level, points, message, show_input_box, input_purpose, inventory
    
    message = "The blue door glows faintly as you step closer..."
    trap_chance = min(3 + level // 2, 7)
    
    if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
        lives -= 1
        level -= 1
        points -= 10
        message = "A hidden spike shoots out!"
    elif "shield" in inventory:
        message = "Your shield blocks a sudden attack!"
        inventory.remove("shield")
    elif random.randint(1, 10) == 4:
        message = "You find a locked chest with a riddle: 'I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?'"
        show_input_box = True
        input_purpose = "Your answer: "
    elif random.randint(1, 10) <= 2:
        message = "A wild thief appears!"
        show_input_box = True
        input_purpose = "Do you want to fight or run? (fight / run)"
    elif random.randint(1, 10) == 5:
        message = "A mysterious merchant appears from the mist!"
        show_input_box = True
        input_purpose = "Trade 20 points for a shield? (yes / no)"
    else:
        message = "You found $100! Do you want to take it?"
        show_input_box = True
        input_purpose = "Take the money? (yes / no)"

def process_door_green():
    global lives, level, points, message, show_input_box, input_purpose, inventory
    
    message = "The green door hums with strange energy..."
    trap_chance = min(3 + level // 2, 7)
    
    if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
        lives -= 1
        level -= 1
        points -= 10
        message = "A pit opens beneath you!"
    elif "shield" in inventory:
        message = "Your shield catches you from falling!"
        inventory.remove("shield")
    elif random.randint(1, 10) <= 2 and level >= 3:
        message = "A mighty dragon blocks your path!"
        show_input_box = True
        input_purpose = "Fight or run? (fight / run)"
    elif random.randint(1, 10) == 5:
        message = "A mysterious merchant appears from the mist!"
        show_input_box = True
        input_purpose = "Trade 20 points for a shield? (yes / no)"
    else:
        message = "You enter a room and found $1,000,000! Do you want to take it or continue?"
        show_input_box = True
        input_purpose = "Take the money? (yes / no)"

def process_door_yellow():
    global lives, level, points, message, show_input_box, input_purpose, inventory
    
    message = "The yellow door shimmers like the sun..."
    trap_chance = min(3 + level // 2, 7)
    
    if random.randint(1, 10) <= trap_chance and "shield" not in inventory:
        lives -= 1
        level -= 1
        points -= 10
        message = "A dart shoots from the wall!"
    elif "shield" in inventory:
        message = "Your shield deflects a dart!"
        inventory.remove("shield")
    elif random.randint(1, 10) <= 2:
        message = "A wild thief appears!"
        show_input_box = True
        input_purpose = "Do you want to fight or run? (fight / run)"
    elif random.randint(1, 10) == 5:
        message = "A mysterious merchant appears from the mist!"
        show_input_box = True
        input_purpose = "Trade 20 points for a shield? (yes / no)"
    else:
        message = "You found a secret tunnel! Do you want to enter?"
        show_input_box = True
        input_purpose = "Enter the tunnel? (yes / no)"

def process_door_black():
    global lives, level, points, message, inventory
    
    message = "The black door pulses with dark energy..."
    trap_chance = min(3 + level // 2, 7)
    
    if random.randint(1, 10) <= trap_chance + 2:
        lives -= 2
        message = "A void swallows you!"
    elif "magic tresure" in inventory:
        points += 200
        level += 3
        inventory.append("shadow cloak")
        message = "Your magic treasure unlocks the secrets of the void!"
    else:
        points -= 50
        level -= 2
        message = "The darkness drains your soul!"

def process_door_golden():
    global lives, level, points, message, show_input_box, input_purpose, inventory
    
    message = "The golden door radiates with unimaginable power..."
    show_input_box = True
    input_purpose = "Enter the golden door? (yes / no)"

def process_door_choice(door):
    global current_door
    
    current_door = door
    
    if door == "red":
        process_door_red()
    elif door == "blue":
        process_door_blue()
    elif door == "green":
        process_door_green()
    elif door == "yellow":
        process_door_yellow()
    elif door == "black":
        process_door_black()
    elif door == "golden":
        process_door_golden()

def process_input_response(response):
    global points, lives, level, message, show_input_box, input_purpose, inventory, game_active
    
    response = response.lower()
    show_input_box = False
    
    # Process response based on current door and question
    if current_door == "red":
        if "fight / run" in input_purpose:
            if response == "fight":
                if random.randint(1, 2) == 1 + skills["strength"] - 1:
                    lives += 1
                    points += 30
                    level += 1
                    inventory.append("thief's dagger")
                    message = "You defeated the thief and took his dagger!"
                else:
                    lives -= 1
                    level -= 1
                    points -= 30
                    message = "The thief overpowered you!"
            elif response == "run":
                if random.randint(1, 2) == 1 + skills["speed"] - 1:
                    points += 10
                    message = "You escaped safely!"
                else:
                    points -= 10
                    level -= 1
                    message = "You failed to run and lost some loot!"
        elif "yes / no" in input_purpose and "shield" in input_purpose:
            if response == "yes" and points >= 20:
                points -= 20
                inventory.append("shield")
                message = "You got a shield!"
            else:
                message = "The merchant vanishes into the shadows."
        elif "yes / no" in input_purpose:
            if response == "yes":
                points += 50
                level += 1
                inventory.append("treasure")
                message = "You win the treasure!"
            elif response == "no":
                points += 100
                level += 2
                inventory.append("magic treasure")
                message = "You found magic treasure, you became a sorcerer!"
    
    elif current_door == "blue":
        if "Your answer" in input_purpose:
            if response == "pencil":
                points += 50
                inventory.append("riddle key")
                message = "Correct! You unlocked the chest."
            else:
                points -= 10
                message = "Wrong answer! The chest vanishes."
        elif "fight / run" in input_purpose:
            if response == "fight":
                if random.randint(1, 2) == 1 + skills["strength"] - 1:
                    lives += 1
                    points += 30
                    level += 1
                    inventory.append("thief's dagger")
                    message = "You defeated the thief and took his dagger!"
                else:
                    lives -= 1
                    level -= 1
                    points -= 30
                    message = "The thief overpowered you!"
            elif response == "run":
                if random.randint(1, 2) == 1 + skills["speed"] - 1:
                    points += 10
                    message = "You escaped safely!"
                else:
                    points -= 10
                    level -= 1
                    message = "You failed to run and lost some loot!"
        elif "yes / no" in input_purpose and "shield" in input_purpose:
            if response == "yes" and points >= 20:
                points -= 20
                inventory.append("shield")
                message = "You got a shield!"
            else:
                message = "The merchant vanishes into the shadows."
        elif "yes / no" in input_purpose:
            if response == "yes":
                points += 20
                level += 1
                inventory.append("$100")
                message = "You take $100!"
            elif response == "no":
                level -= 1
                points -= 10
                message = "You found a big dragon, you died."
    
    elif current_door == "green":
        if "fight / run" in input_purpose:
            if response == "fight" and "thief's dagger" in inventory:
                if random.randint(1, 2) + skills["strength"] - 1 >= 2:
                    points += 100
                    level += 2
                    inventory.append("dragon scale")
                    message = "You slayed the dragon!"
                else:
                    lives -= 2
                    message = "The dragon incinerates you!"
            elif response == "run":
                if random.randint(1, 2) + skills["speed"] - 1 >= 2:
                    points += 20
                    message = "You narrowly escaped the dragon!"
                else:
                    lives -= 1
                    message = "The dragon catches you!"
        elif "yes / no" in input_purpose and "shield" in input_purpose:
            if response == "yes" and points >= 20:
                points -= 20
                inventory.append("shield")
                message = "You got a shield!"
            else:
                message = "The merchant vanishes into the shadows."
        elif "yes / no" in input_purpose:
            if response == "yes":
                points += 50
                level += 1
                inventory.append("$1,000,000")
                message = "You win $1,000,000! Game over."
            elif response == "no":
                points += 75
                level += 2
                message = "You found a room full of gold! How many kilograms do you want to take?"
                show_input_box = True
                input_purpose = "How many kilograms of gold? (enter a number)"
    
    elif current_door == "yellow":
        if "fight / run" in input_purpose:
            if response == "fight":
                if random.randint(1, 2) == 1 + skills["strength"] - 1:
                    lives += 1
                    points += 30
                    level += 1
                    inventory.append("thief's dagger")
                    message = "You defeated the thief and took his dagger!"
                else:
                    lives -= 1
                    level -= 1
                    points -= 30
                    message = "The thief overpowered you!"
            elif response == "run":
                if random.randint(1, 2) == 1 + skills["speed"] - 1:
                    points += 10
                    message = "You escaped safely!"
                else:
                    points -= 10
                    level -= 1
                    message = "You failed to run and lost some loot!"
        elif "yes / no" in input_purpose and "shield" in input_purpose:
            if response == "yes" and points >= 20:
                points -= 20
                inventory.append("shield")
                message = "You got a shield!"
            else:
                message = "The merchant vanishes into the shadows."
        elif "yes / no" in input_purpose:
            if response == "yes":
                points += 100
                level += 1
                inventory.append("hidden city map")
                message = "You discover a hidden city!"
            elif response == "no":
                level -= 1
                message = "You go back empty-handed."
    
    elif current_door == "golden":
        if "yes / no" in input_purpose and not "End game" in input_purpose:
            if response == "yes":
                points += 1000
                inventory.append("golden crown")
                message = "You found the Golden Crown! You can end the game as a legend!"
                show_input_box = True
                input_purpose = "End game now? (yes / no)"
            elif response == "no":
                points += 50
                level += 1
                message = "You resist the temptation and grow stronger!"
        elif "End game" in input_purpose:
            if response == "yes":
                message = "Game ended! You retire as a legend!"
                game_active = False
    
    # Special case for gold amount
    if "How many kilograms of gold" in input_purpose:
        try:
            gold = int(response)
            inventory.append(f"{gold} kg of gold")
            message = f"You win {gold} kg of gold!"
        except ValueError:
            message = "Please enter a valid number!"
    
    # Check for skill improvement
    if level > 1 and level % 2 == 0:
        message += " You can improve a skill!"
        show_input_box = True
        input_purpose = "Improve a skill (strength / speed / luck)"
    
    # Check for game end conditions
    if points >= goal_points:
        message = f"Congratulations! You found the Legendary Crown with {points} points and {inventory} in your inventory!"
        game_active = False
    
    if lives <= 0:
        message = f"Game over! The cursed town claims another soul. Final points: {points}, Inventory: {inventory}"
        game_active = False

def improve_skill(skill):
    global skills, message, show_input_box
    
    if skill in skills:
        skills[skill] += 1
        message = f"{skill.capitalize()} improved to {skills[skill]}!"
    else:
        message = "Sorry, your choice is unknown! Try again."
    
    show_input_box = False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle door clicks
        elif event.type == pygame.MOUSEBUTTONDOWN and game_active and not show_input_box:
            mouse_pos = pygame.mouse.get_pos()
            door_width = WIDTH // 6
            door_height = HEIGHT // 2
            
            # Check if any door was clicked
            doors = ["red", "blue", "green", "yellow", "black"]
            if random.randint(1, 100) == 1:
                doors.append("golden")
            
            for i, door in enumerate(doors):
                x = (i+1) * WIDTH // (len(doors) + 1) - door_width // 2
                y = HEIGHT // 2 - door_height // 2
                
                if x <= mouse_pos[0] <= x + door_width and y <= mouse_pos[1] <= y + door_height:
                    process_door_choice(door)
        
        # Handle text input
        elif event.type == pygame.KEYDOWN and show_input_box:
            if event.key == pygame.K_RETURN:
                if "skill" in input_purpose:
                    improve_skill(input_text)
                else:
                    process_input_response(input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
    
    # Draw game elements
    if game_active:
        draw_status_bar()
        draw_doors()
    
    draw_message_box()
    draw_input_box()
    
    if not game_active:
        draw_text("Game Over! Press ESC to exit", font_large, WHITE, WIDTH // 2, HEIGHT // 4)
    
    # Check for ESC key to exit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()