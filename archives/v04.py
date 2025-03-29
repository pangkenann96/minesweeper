

# field dimension number is a single interger. eg if field is 3x3, field_dimension_number = 3
field_dimension_number = 3


# hard coded
field = [['.', '*', '.'], ['*', '.', '.'], ['.', '.', '.']]

for row in field:
    print(''.join(row))



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


# check for out of field range
def is_cell_within_field(row, col, field_dimension_number):
    if row <= 0:
        return False
    if row > field_dimension_number:
        return False
    if col <=0:
        return False
    if col > field_dimension_number:
        return False
    return True


upper_left_adjacent_cell_check = is_cell_within_field(row_input-1, col_input-1, field_dimension_number)
print(upper_left_adjacent_cell_check)

if upper_left_adjacent_cell_check:
    upper_left_adjacent_cell_value = cell_check(row_input-1, col_input-1)
    print(f"the upper left cell mine value is: {upper_left_adjacent_cell_value}")


