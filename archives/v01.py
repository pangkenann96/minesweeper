# field = [[], []]

# hard coded
field = [['*', '.'], ['.', '.']]

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
print(field[int(row_input)-1][int(col_input)-1])



