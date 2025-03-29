# field = [[], []]

# hard coded
field = [['.', '*', '.'], ['*', '.', '.'], ['.', '.', '.']]

for row in field:
    print(''.join(row))


# so we have 4 cases. user chooses:
'''
(1,1)
(1,2)
(2,1)
(2,2)

'''

# need to allow user to input a choice. going with (row, col)
row_input= int(input("choose a row num:"))
col_input = int(input("choose a col num:"))

#need to map (row, col) to the relevant field item. realise its all -1. ie (row, col) corresponds to [row-1][col-1]

def cell_check(row, col):
    return field[int(row)-1][int(col)-1]

def is_mine(row, col):
    return 1 if cell_check  == "*" else 0


selected_cell = cell_check(row_input, col_input)
# print(f"is mine checker says: {is_mine(row_input, col_input)}")


'''
def count_adjacent_mines(row, col):
    first = is_mine(cell_check(row-1, col-1))
    second = is_mine(cell_check(row-1, col))
    third = is_mine(cell_check(row-1, col+1))
    fourth = is_mine(cell_check(row, col-1))
    fifth = is_mine(cell_check(row, col+1))
    sixth = is_mine(cell_check(row+1, col-1))
    seventh = is_mine(cell_check(row+1, col))
    eighth = is_mine(cell_check(row+1, col+1))
    print(f"we get [{first}, {second}, {third}, {fourth}, {fifth}, {sixth}, {seventh}, {eighth}]")
    return first + second + third + fourth + fifth + sixth + seventh + eighth


print(count_adjacent_mines(row_input, col_input))
'''

'''
# simple calculation logic
if selected_cell == ".":
    print(". found") #need to trigger calculation here
else:
    print("KABOOM")
#simple calculation logic. decision: I will make it 3x3 hard coded, and select the centre for ease of testing. 
'''
