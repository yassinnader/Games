
#import turtle module
import turtle
# Import the time module for time control
import time 
# Import the random module for generating random numbers
import random  

# initialize screen
wind = turtle.Screen()  # Create a screen object
wind.title("ping pong") # Set the title of the screen
wind.bgcolor("black") # Set the background color of the screen to black
wind.setup(width=1600, height=800) # set the width and height of the window
wind.tracer(0) # stops the window from updating automatically

# game starts as not running
game_running = False # Initialize the game running state to False
paused = False # Initialize the paused state to False
difficulty = 1.2  # Initialize the difficulty (speed multiplier)

# Backgrounds
backgrounds = ["black", "darkblue", "darkgreen", "darkred", "darkorange"]  # List of background colors

# Score and timer settings
score1 = 0  # Initialize player 1's score
score2 = 0  # Initialize player 2's score
game_time = 5  # Set the game time to 60 seconds
start_time = 0  # Initialize the start time

# initialize the first paddle (madrab1)
madrab1 = turtle.Turtle()  # Create a turtle object for player 1's paddle
madrab1.speed(0) # set the speed of the animation to maximum
madrab1.shape("square") # set the shape of the paddle
madrab1.color("blue") # set the color of the paddle
madrab1.shapesize(stretch_wid=10, stretch_len=1) # Set the paddle's size
madrab1.penup()  # Lift the pen to prevent drawing
madrab1.goto(-750, 0) # Move the paddle to its initial position

# initialize the second paddle (madrab2)
madrab2 = turtle.Turtle() # set the speed of the animation to maximum
madrab2.speed(0) # Set the paddle's speed to the fastest
madrab2.shape("square") # set the shape of the paddle
madrab2.color("red") # set the color of the paddle
madrab2.shapesize(stretch_wid=10, stretch_len=1) # Set the paddle's size
madrab2.penup() # Lift the pen to prevent drawing
madrab2.goto(750, 0) # Move the paddle to its initial position

# initialize the ball
ball = turtle.Turtle() # Create a turtle object for the ball
ball.speed(0) # set the speed of the ball animation to maximum
ball.shape("circle") # set the shape of the ball
ball.color("white") # set the color of the ball
ball.penup() # Lift the pen to prevent drawing
ball.goto(0, -50) # Move the ball to the center, but lower
ball.dx = 4 * difficulty  # Set the ball's horizontal speed
ball.dy = 4 * difficulty  # Set the ball's vertical speed
ball_speed_increase = 0.1 * difficulty  # Set the ball's speed increase rate

# Score display
score = turtle.Turtle() # Create a turtle object for displaying the score
score.speed(0) # set the speed of the score object
score.color("white") # set the color of the score text
score.penup() # prevent the score object from drawing lines
score.hideturtle() # hide the score turtle object (no shape)
score.goto(0, 350) # set the position for the score display
score.write("Player Blue: 0  Player Red: 0", align="center", font=("Courier", 24, "normal"))  # Write the initial score

# Timer display
timer = turtle.Turtle()  # Create a turtle object for displaying the timer
timer.speed(0)  # Set the timer display's speed to the fastest
timer.color("white")  # Set the timer display's color to white
timer.penup()  # Lift the pen to prevent drawing
timer.hideturtle()  # Hide the turtle object
timer.goto(0, 300)  # Move the timer display to its position
timer.write(f"Time left: {game_time}s", align="center", font=("Courier", 24, "normal"))  # Write the initial time

# Paddle movements
def madrab1_up():  # Function to move player 1's paddle up
    y = madrab1.ycor()  # Get the current y-coordinate of the paddle
    if y < 300:  # Check if the paddle is within the upper boundary
        y += 40  # Move the paddle up
        madrab1.sety(y)  # Set the new y-coordinate

def madrab1_down():  # Function to move player 1's paddle down
    y = madrab1.ycor()  # Get the current y-coordinate of the paddle
    if y > -290:  # Check if the paddle is within the lower boundary
        y -= 40  # Move the paddle down
        madrab1.sety(y)  # Set the new y-coordinate

def madrab2_up():  # Function to move player 2's paddle up
    y = madrab2.ycor()  # Get the current y-coordinate of the paddle
    if y < 300:  # Check if the paddle is within the upper boundary
        y += 40  # Move the paddle up
        madrab2.sety(y)  # Set the new y-coordinate

def madrab2_down():  # Function to move player 2's paddle down
    y = madrab2.ycor()  # Get the current y-coordinate of the paddle
    if y > -290:  # Check if the paddle is within the lower boundary
        y -= 40  # Move the paddle down
        madrab2.sety(y)  # Set the new y-coordinate

# Start the game when space is pressed
def start_game():  # Function to start the game
    global game_running, start_time
    game_running = True  # Set the game running state to True
    start_time = time.time()  # Record the start time
    start_menu.clear()  # Clear the start menu display

# Power-up to increase ball speed
def increase_speed():  # Function to increase the ball's speed
    global ball_speed_increase
    ball_speed_increase += 0.001  # Increase the speed increase rate
    wind.bgcolor(random.choice(backgrounds))  # Change the background color randomly

# Movement bindings
def toggle_pause():
    global paused
    paused = not paused

# New game menu
start_menu = turtle.Turtle()
start_menu.speed(0)
start_menu.color("white")
start_menu.penup()
start_menu.hideturtle()
start_menu.goto(0, 0)
start_menu.write("Press SPACE to start\nPress P to pause\nPress R to reset",
                align="center", font=("Courier", 36, "normal"))

def reset_game():
    global game_running, score1, score2, start_time
    game_running = False
    score1 = score2 = 0
    score.clear()
    score.write("Player Blue: 0  Player Red: 0", align="center", font=("Courier", 24, "normal"))
    ball.goto(0, -50)
    ball.dx = 4 * difficulty * random.choice([-1, 1])
    ball.dy = 4 * difficulty * random.choice([-1, 1])
    start_menu.clear()
    start_menu.write("Press SPACE to start\nPress P to pause\nPress R to reset",
                    align="center", font=("Courier", 36, "normal"))

# Keyboard bindings
wind.listen()  # Listen for keyboard events
wind.onkeypress(start_game, "space")  # Bind the space key to the start_game function
wind.onkeypress(madrab1_up, "w")  # Bind the 'w' key to the madrab1_up function
wind.onkeypress(madrab1_down, "s")  # Bind the 's' key to the madrab1_down function
wind.onkeypress(madrab2_up, "Up")  # Bind the up arrow key to the madrab2_up function
wind.onkeypress(madrab2_down, "Down")  # Bind the down arrow key to the madrab2_down function
wind.onkeypress(toggle_pause, "p")
wind.onkeypress(reset_game, "r")

# Main game loop
while True:
    wind.update()  # update the screen every frame

    if game_running and not paused: # Check if the game is running and not paused
        # Update ball position
        ball.setx(ball.xcor() + ball.dx)  # move the ball along the x-axis
        ball.sety(ball.ycor() + ball.dy)  # move the ball along the y-axis

        # Ball and top boundary collision
        if ball.ycor() > 390: # check for collision with the top boundary
            ball.sety(390) # set the ball position and reverse direction
            ball.dy *= -1 # Reverse the ball's vertical direction

        # Ball and bottom boundary collision
        if ball.ycor() < -390: # check for collision with the bottom boundary
            ball.sety(-390) # set the ball position and reverse direction
            ball.dy *= -1 # Reverse the ball's vertical direction

        # Ball and right boundary collision (score for player 1)
        if ball.xcor() > 790: # check if the ball crosses the right boundary (player 1 scores)
            ball.goto(0, -50) # reset the ball to the center, but lower
            ball.dx *= -1 # reverse the direction of the ball
            score1 += 1 # increment the score of player 1
            score.clear() # update the score display
            score.write(f"Player Blue: {score1}  Player Red: {score2}", align="center", font=("Courier", 24, "normal"))  # Update and display the score

        # Ball and left boundary collision (score for player 2)
        if ball.xcor() < -790:  # Check if the ball hit the left boundary
            ball.goto(0, -50) # reset the ball to the center, but lower
            ball.dx *= -1 # reverse the direction of the ball
            score2 += 1 # increment the score of player 2
            score.clear() # update the score display
            score.write(f"Player Blue: {score1}  Player Red: {score2}", align="center", font=("Courier",24,"normal")) # Update and display the score

        # check for collision between the ball and the second paddle
        if (ball.xcor() > 740 and ball.xcor() < 750) and (ball.ycor() < madrab2.ycor() + 120 and ball.ycor() > madrab2.ycor() - 120):
            ball.setx(740) # Move the ball to the paddle's edge
            ball.dx *= -1 # Reverse the ball's horizontal direction
            ball.dx += ball_speed_increase * (1 if ball.dx > 0 else -1) # increase the ball's speed
            increase_speed()  # Increase speed and change background color

        # check for collision between the ball and the first paddle
        if (ball.xcor() < -740 and ball.xcor() > -750) and (ball.ycor() < madrab1.ycor() + 120 and ball.ycor() > madrab1.ycor() - 120):
            ball.setx(-740) # Move the ball to the paddle's edge
            ball.dx *= -1 # Reverse the ball's horizontal direction
            ball.dx += ball_speed_increase * (1 if ball.dx > 0 else -1) # increase the ball's speed
            increase_speed()  # Increase speed and change background color

        # Update timer
        elapsed_time = time.time() - start_time  # Calculate the elapsed time
        time_left = max(0, int(game_time - elapsed_time))  # Calculate the remaining time
        timer.clear()  # Clear the timer display
        timer.write(f"Time left: {time_left}s", align="center", font=("Courier", 24, "normal"))  # Update and display the remaining time

        # End the game when time runs out
        if time_left == 0:  # Check if the time has run out
            game_running = False  # Set the game running state to False
            score.clear()  # Clear the score display
            timer.clear()  # Clear the timer display
            timer.goto(0, 100)  # Adjust the position of the timer display
            score.goto(0, 50)  # Adjust the position of the score display
            timer.write("Game Over!", align="center", font=("Courier", 70, "normal"))  # Display "Game Over"
            if score1 > score2:
                winner_message = "Player Blue Wins!"
            elif score2 > score1:
                winner_message = "Player Red Wins!"
            else:
                winner_message = "It's a Draw!"
            score.write(f"Final Score - Player Blue: {score1}  Player Red: {score2}\n{winner_message}", align="center", font=("Courier", 24, "normal"))  # Display the final score and winner

    # Prevent overwhelming CPU usage
    wind.update()
    time.sleep(0.01) 