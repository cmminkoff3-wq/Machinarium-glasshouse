## Author: Charles "miles" Michael Minkoff III
## Creation Date: Aug. 28th, 2025
## Last Edited: Jan. 9th, 2026
#
## questions? comments? concerns? crying?
# currently none (unless you enter n when asked if you want to try again)

### IMPORTS ###
from graphics import *
import time


###~MAIN CODE~###

### PRINTING ###
print("this code is a game originally from machinarium")
print("input a number from 1 to 25 to choose where your light starts (going from top left to bottom right)")# the user should strategically start where it IS possible to turn all 0s to 1s
print("use the keys wsad to guide your light until the grid is filled")# the last 1 that the user filled in is their current position, they can only go a certain direction from their position if there is at least one 0 in that direction that is adjacent to their position
print("remember to input r to restart or e to exit the program")

### CREATE WINDOW ###
display = GraphWin("Image Display", 250, 250)

### DEFINE LEVELS_BEATEN ###
levels_beaten = [False, False, False, False, False, False]# 6 Falses for 6 levels, when a level is beaten it turns the corresponding False to True

### DEFINE ALL_LISTS ###
all_lists = [1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,
             1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,
             1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,
             1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,
             1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,
             1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,
             1,1,1,1,1]
## each seperate list is begins with 5 1s, ends with 5 1s, and has an extra 1 every 5 digits
## all extra 1s are for the game over function. since it's based on the user being
# "surrounded by 1s", there must be 1s on the outskirts of each row and column
## this is what a grid (level 1) actually looks like: [1,1,1,1,1]
# so 1s above each row and between each column        [0,0,0,0,0,1]
# (technically the 1 on row 6 isn't between columns,  [0,0,0,0,0,1]
# but in order for the math in the code to work       [0,0,0,0,0,1]
# there must be consistency, thus the extra 1)        [0,0,0,0,0,1]
#                                                     [0,0,0,0,0,1]
#                                                     [1,1,1,1,1]

### LEVEL RUNNING FUNCTION ###
def run_level(level_number):
    print("level",level_number,
          ":")
    user_list = all_lists[((int(level_number) - 1) * 35):((int(level_number) * 35) + 5)]# each group of 35 in all_lists corresponds with the list fro a certain level

    ### FOR LOOP FOR BLOCK DISPLAY ###
    for number in range(1, 26):# the numbers in the grid that start can be
        if user_list[int(((number * 6) + 19) // 5)] == 0:# formula for displayed numbers
            grey = Image(Point(((((int(number) - 1) % 5) + 1) * 50 - 25), (((int(number) + 4) // 5) * 50 - 25)), "grey.gif")# displays a grey block in place of a 0 for the main grid
            grey.draw(display)
        elif user_list[int(((number * 6) + 19) // 5)] == 1:
            red = Image(Point(((((int(number) - 1) % 5) + 1) * 50 - 25), (((int(number) + 4) // 5) * 50 - 25)), "red.gif")# displays a red block in place of a 1 for the main grid
            red.draw(display)
        else:
            print("this should not have happened")# if anything in the grid is other than 1 or 0, there is something very wrong

    ### WHILE LOOP FOR START SELECTION ###
    while True:
        start = input("choose starting point (numbers 1-25): ")# asks for start point
        if start == 'e':# e for exit
            print("exiting...")
            exit()# stops the program
        else:
            try:# in case the user enters anything but e or any number
                if 0 < int(start) < 26:
                    if user_list[int(((int(start) * 6) + 19) // 5)] == 0:
                        start = int(start)# converts string 'start' to integer
                        break# exits the loop if start is within range
                    else:
                        print("already filled in")
                else:
                    print("number out of range")
            except ValueError:
                print("invalid starting point")# if start point entered is not an integer, loop is not broken

    ### DEFINE MAIN VARIABLES ###
    row = (int(start) + 4) // 5# calculates the row that the current position is in
    column = ((int(start) - 1) % 5) + 1# calculates the column that the current position is in
    user_list[int(((int(start) * 6) + 19) // 5)] = 1# same formula as before (if statement for block display), calculates

    ### DIPLAY STARTING POINT ###
    green = Image(Point((column * 50 - 25), (row * 50 - 25)),"green.gif")
    green.draw(display)

    ### LEVEL RUNNING ###
    while True:

        ### FUNCTION FOR "GAME OVER" ###
        game_over = False
        grid_sum = 0  # otherwise the sum would keep getting added to and you would win long before filling out the whole grid
        for e in range(1,26):# the numbers in the grid that can be changed by the user
            grid_sum += user_list[int(((e * 6) + 19) // 5)]# grid_sum is now the sum of all numbers in the displayed part of the grid
        if grid_sum == 25:# since all 0s in the 5x5 grid must be turned to 1s to win, you don't win until the sum of the digits in the 5x5 grid is 25
            break
        else:
            pass
        if user_list[((row - 1) * 6 + column - 2)] == user_list[((row + 1) * 6 + column - 2)] == user_list[(row * 6 + (column - 1) - 2)] == user_list[(row * 6 + (column + 1) - 2)] == 1:# if current position is surrounded by 1s (the user is stuck)
            game_over = True
            print("GAME OVER")
            try_again = input("would you like to try again? (y/n): ")
            if try_again == 'y':
                print("starting over...")
                break# starts the main while loop over
            elif try_again == 'n':
                print("😢")
                exit()# exits the game
            else:
                print("not cool man")
        else:
            pass

        ### FUNCTION FOR UP ACTION ###
        move = input("choose next move (w ^, s v, a <, d >): ")# asks which direction the user wants to go
        if move == 'w':# meaning up
            while row > 1:# can't move up if you're in the top row
                if user_list[((row - 1) * 6 + column - 2)] == 0:# the digit above current position
                    user_list[((row - 1) * 6 + column - 2)] = 1# digit above is now 1
                    yellow = Image(Point((column * 50 - 25), (row * 50 - 25)), "yellow.gif")# current position is now yellow
                    yellow.draw(display)
                    row -= 1# raises the row
                    green = Image(Point((column * 50 - 25), (row * 50 -25)),"green.gif")# current position is now green
                    green.draw(display)
                    ## notice current position = yellow, then move, then current position = green (then repeat) will create a trail of yellows led by a green
                else:
                    break

        ### FUNCTION FOR DOWN ACTION ###
        elif move == 's':# meaning down
            while row < 5:# can't move down if you're in the bottom row
                if user_list[((row + 1) * 6 + column - 2)] == 0:# the digit below current position
                    user_list[((row + 1) * 6 + column - 2)] = 1# digit below is now 1
                    yellow = Image(Point((column * 50 - 25), (row * 50 -25)), "yellow.gif")
                    yellow.draw(display)
                    row += 1# lowers the row
                    green = Image(Point((column * 50 - 25), (row * 50 - 25)), "green.gif")
                    green.draw(display)
                else:
                    break

        ### FUNCTION FOR LEFT ACTION ###
        elif move == 'a':# meaning left
            while column > 1:# can't move left if you're in the first column
                if user_list[(row * 6 + (column - 1) - 2)] == 0:# the digit left of current position
                    user_list[(row * 6 + (column - 1) - 2)] = 1# digit left is now 1
                    yellow = Image(Point((column * 50 - 25), (row * 50 -25)), "yellow.gif")
                    yellow.draw(display)
                    column -= 1# decreases the column
                    green = Image(Point((column * 50 - 25), (row * 50 - 25)), "green.gif")
                    green.draw(display)

                else:
                    break

        ### FUNCTION FOR RIGHT ACTION ###
        elif move == 'd':# meaning right
            while column < 5:# can't move right if you're in the last column
                if user_list[(row * 6 + (column + 1) - 2)] == 0:# the digit right of current position
                    user_list[(row * 6 + (column + 1) - 2)] = 1# digit right is now 1
                    yellow = Image(Point((column * 50 - 25), (row * 50 - 25)), "yellow.gif")
                    yellow.draw(display)
                    column += 1# increases the column
                    green = Image(Point((column * 50 - 25), (row * 50 - 25)), "green.gif")
                    green.draw(display)
                else:
                    break

        elif move == 'r':#r for restart
            print("restarting...")
            game_over = True
            break

        elif move == 'e':# e for exit
            print("exiting...")
            exit()# stops the program

        else:
            print("invalid move")# in case the user enters something other than w, s, a, or d

        blue = Image(Point(((((int(start) - 1) % 5) + 1) * 50 - 25), (((int(start) + 4) // 5) * 50 - 25)), "blue.gif")
        blue.draw(display)

    if game_over:
        pass
    elif not game_over:
        ### FOR LOOP FOR LEVEL COMPLETION ###
        for number in range(1, 26):  # the numbers in the grid that can be changed by the user
            green = Image(Point(((((int(number) - 1) % 5) + 1) * 50 - 25), (((int(number) + 4) // 5) * 50 - 25)),"green.gif")
            green.draw(display)
            ## notice that this should fill the whole visible grid with green blocks (signifying a win)
        time.sleep(1)# smooths the code and keeps the winning grid displayed a little longer
        print("you filled the grid!")# you win!

        levels_beaten[int(level_number) - 1] = True# sets whichever level the user just beat to True in levels_beaten

        ### CONGRATULATIONS ###
        if False in levels_beaten:# if levels_beaten contains False
            print("you have beaten:")
            for i in range(6):
                if levels_beaten[i]:
                    print("level",i + 1,)# ends up printing all levels that are set to True in levels_beaten
        else:
            print("you've beaten all levels! ⭐")# if levels_beaten only contains True
            print("contact the author if you're willing to share ideas for more levels")
            exit()

while True:
    ### WHILE LOOP FOR LEVEL SELECTION ###
    while True:
        level_number = input("choose a level 1-6: ")# allows the user to choose which level they'd prefer
        if level_number == 'e':# e for exit
            print("exiting...")
            exit()# stops the program
        else:
            try:# in case the user entered anything but e or any number
                if  0 < int(level_number) < 7:
                    if levels_beaten[int(level_number) - 1] == False:# if the user hasn't beaten this level yet
                        run_level(level_number)
                    elif levels_beaten[int(level_number) - 1]:
                        while True:
                            user_response = input("you've beaten this level already, are you sure? (y/n): ")
                            if user_response == "y":
                                run_level(level_number)
                                break
                            elif user_response == "n":
                                break
                            else:
                                print("not cool man")
                    else:
                        print("this should not have happened")
                else:
                    print("number out of range")
            except ValueError:
                print("invalid level")