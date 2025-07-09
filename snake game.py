import random
import curses

def start_screen(window):
    screen_height, screen_width = window.getmaxyx()
    window.clear()
    window.addstr(screen_height // 2 - 2, screen_width // 2 - 10, "Welcome to Snake Game!", curses.A_BOLD)
    window.addstr(screen_height // 2, screen_width // 2 - 14, "Press any key to start playing", curses.A_NORMAL)
    window.refresh()
    window.getch()
    window.clear()

def game_over_screen(window, score):
    screen_height, screen_width = window.getmaxyx()
    window.clear()
    window.addstr(screen_height // 2 - 2, screen_width // 2 - 5, "Game Over", curses.A_BOLD)
    window.addstr(screen_height // 2, screen_width // 2 - 7, f"Your Score: {score}", curses.A_NORMAL)
    window.addstr(screen_height // 2 + 2, screen_width // 2 - 12, "Press any key to exit", curses.A_NORMAL)
    window.refresh()
    window.getch()
    curses.endwin()
    quit()

def main(screen):
    # initialize the curses library to create our screen
    screen = curses.initscr()

    # hide the mouse cursor
    curses.curs_set(0)

    # getmax screen height and width
    screen_height, screen_width = screen.getmaxyx()
    # create a new window
    window = curses.newwin(screen_height, screen_width, 0, 0)

    # allow window to receive input from the keyboard
    window.keypad(1)

    # set the delay for updating the screen
    window.timeout(100)

    # start screen
    start_screen(window)

    # set the x,y coordinates of the initial position of snake's head
    snk_x = screen_width // 4
    snk_y = screen_height // 2

    # define the initial position of the snake body
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # create the food in the middle of window
    food = [screen_height // 2, screen_width // 2]

    # add the food by using PI character from curses module
    if 0 <= food[0] < screen_height and 0 <= food[1] < screen_width:
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        curses.endwin()
        raise ValueError("Food coordinates are out of bounds")

    # set initial movement direction to right
    key = curses.KEY_RIGHT

    # initialize score and level
    score = 0
    level = 1

    # colors for snake and food
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food color

    # create game loop that loops forever until player loses or quits the game
    while True:
        # display the score and level
        window.addstr(0, 2, f'Score: {score} ')
        window.addstr(0, screen_width // 2, f'Level: {level} ')
        window.border(0)

        # get the next key that will be pressed by user
        next_key = window.getch()
        # if user doesn't input anything, key remains same, else key will be set to the new pressed key
        key = key if next_key == -1 else next_key

        # check if snake collided with the walls or itself
        if snake[0][0] in [0, screen_height - 1] or snake[0][1] in [0, screen_width - 1] or snake[0] in snake[1:]:
            game_over_screen(window, score)

        # set the new position of the snake head based on the direction
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        # insert the new head to the first position of snake list
        snake.insert(0, new_head)
        # check if snake ate the food
        if snake[0] == food:
            score += 1  # increase score
            food = None  # remove food if snake ate it
            # while food is removed, generate new food in a random place on screen
            while food is None:
                new_food = [
                    random.randint(1, screen_height - 2),
                    random.randint(1, screen_width - 2)
                ]
                food = new_food if new_food not in snake else None
            if 0 <= food[0] < screen_height and 0 <= food[1] < screen_width:
                window.addch(food[0], food[1], curses.ACS_PI, curses.color_pair(2))
            else:
                curses.endwin()
                raise ValueError("Food coordinates are out of bounds")

            # increase level every 5 points
            if score % 5 == 0:
                level += 1
                window.timeout(100 - (len(snake) // 5 + len(snake) // 10) % 120)
                window.addstr(screen_height // 2, screen_width // 2 - 5, 'Level Up!', curses.A_BOLD)
                window.refresh()
                curses.napms(2000)  # Increase the duration to 2 seconds
                window.addstr(screen_height // 2, screen_width // 2 - 5, '         ')
        else:
            # otherwise remove the last segment of snake body
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD, curses.color_pair(1))

        # adjust the speed based on the score
        window.timeout(100 - (len(snake) // 5 + len(snake) // 10) % 120)

# run the main function
curses.wrapper(main)