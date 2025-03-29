

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



# refactoring into function
def check_cell_and_count(row, col, field_dimension_number):
    print("")
    print(f"row: {row}")
    print(f"col: {col}")
    print(f"field dimension number: {field_dimension_number}")


    cell_in_field_check = is_cell_within_field(row, col, field_dimension_number)
    print(f"cell in field range: {cell_in_field_check}")

    if cell_in_field_check:
        cell_value = cell_check(row, col)
        print(f"cell value: {cell_value}")

        # will break my is_mine function and just write here
        return 1 if cell_value  == "*" else 0

    return 0

def count_adjacent_mines(row, col, field_dimension_number):
    first = check_cell_and_count(row-1, col-1, field_dimension_number)
    second = check_cell_and_count(row-1, col, field_dimension_number)
    third = check_cell_and_count(row-1, col+1, field_dimension_number)
    fourth = check_cell_and_count(row, col-1, field_dimension_number)
    fifth = check_cell_and_count(row, col+1, field_dimension_number)
    sixth = check_cell_and_count(row+1, col-1, field_dimension_number)
    seventh = check_cell_and_count(row+1, col, field_dimension_number)
    eighth = check_cell_and_count(row+1, col+1, field_dimension_number)
    print(f"we get [{first}, {second}, {third}, {fourth}, {fifth}, {sixth}, {seventh}, {eighth}]")
    return first + second + third + fourth + fifth + sixth + seventh + eighth


print(count_adjacent_mines(row_input, col_input, field_dimension_number))


