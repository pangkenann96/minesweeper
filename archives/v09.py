import random

def random_choice(probability):
    if random.random() < probability:
        return "*"
    else:
        return "."

def generate_field(n, probability):
    return [[random_choice(probability) for _ in range(n)] for _ in range(n)]



# field dimension number is a single interger. eg if field is 3x3, field_dimension_number = 3
field_dimension_number = int(input("Create a game. How many rows? (insert a non zero number) "))
probability = 0.3  # You can adjust this value between 0 and 1

field = generate_field(field_dimension_number, probability)

for row in field:
    print("".join(row))





backend_field_state = list(field)
# print(f"backend field state: {backend_field_state}")



frontend_field_state = [[ "." for i in range(field_dimension_number) ] for i in range(field_dimension_number) ]
# print(f"frontend field state: {frontend_field_state}")






#need to map (row, col) to the relevant field item. realise its all -1. ie (row, col) corresponds to [row-1][col-1]

def cell_check(row, col):
    return field[int(row)-1][int(col)-1]

def is_mine(row, col):
    return 1 if cell_check(row, col)  == "*" else 0




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



def check_cell_and_count(row, col, field_dimension_number):
    # checks 1 cell for field range and give mine count
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
        # return 1 if cell_value  == "*" else 0
        return is_mine(row, col)
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






while True:
    # need to allow user to input a choice. going with (row, col)
    row_input= int(input("choose a row num:"))
    col_input = int(input("choose a col num:"))

    # end game if land on mine
    if is_mine(row_input, col_input):
        print("KABOOM!\nYou stepped on a mine")
        for row in backend_field_state:
            print("".join(row))
        break
 
    frontend_field_state[row_input - 1][col_input - 1] = str(count_adjacent_mines(row_input, col_input, field_dimension_number))
    frontend_field_state = list(frontend_field_state)

    backend_field_state[row_input - 1][col_input - 1] = str(count_adjacent_mines(row_input, col_input, field_dimension_number))
    backend_field_state = list(backend_field_state)



    for row in frontend_field_state:
        print("".join(row))




