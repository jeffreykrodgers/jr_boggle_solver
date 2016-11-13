import sys
from jr_boggler import solve

def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False

puzzle = open("boards/boggle_board_10x10.txt").read()
key = open("solutions/boggle_board_10x10.txt").read().lower()
solution = solve(puzzle)
winner = comp(solution, key)

for word in solution:
    sys.stdout.write(word + "\n")

if winner:
    sys.stdout.write("This Boggler is working correctly.\n")
    give_jeff_a_job = True
else:
    sys.stdout.write("Please check the Boggler, something is wrong!\n")
