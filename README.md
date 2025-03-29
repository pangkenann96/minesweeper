This is a quick project to test code kata, TDD philosophy
Objective: create a CLI minesweeper game from scratch


iterations
0. you can just print the field -> success with 2x2 hard coded
Q: is the next iteration a bigger field? autocreation of field? player able to click a mine to guess? going with the latter
1. you can click a hard coded 2x2 field -> success with 2x2 hard coded, no calculation logic
Q: between auto creation, bigger field, and calculation logic, going with claculation logic
2. user selects field, and it shows number (ie. calculation logic implemented) -> forced to take field expansion route to 3x3 and select middle, (2,2) -> created `is_mine` function to check a cell and turn into 1 if mine 0 if no mine -> refactored `cell_check` for 8 cell check, `count_adjacent_mines`. -> too heavy. need to chunk it down to just checking 1 cell
3. (rescope 2) user selects field, and it shows the number of mines to the upper left cell adjacent to it. -> success but does not handle if cell is outside the field (still shows value)
Q: between handling out of field range or expanding to 8 cells, which? I decide the field range.
4. user selects field, and it shows the upper left adjacent cell, and value = `none` if out of field range, mine count = 0 if out of field range -> success for upper left adjacent cell. next, expand to 8 cells
5. user selects a cell, and 8 adjcent cells calculated number of mines, and handle case of out of field range -> dismantled by `is_mine` function and jsut weave into the formula -> success with lots of cli prints
D: need a state. always have the initial. but then an evolving one that is shown to the user as he clicks. show current field state after each user click. 
6. user selects a cell, and field state is updated with original still stored. -> `current_field_state` implemented and update with print under a while loop -> success but no KABOOM when user selects a mine
7. user clicks on mine, KABOOM -> found bug in `is_mine`, reimplemented in other formulas
D: need to hide the answer from the user at the start.
8. the initial board is hidden from sigh from user. -> success. 
D: now back to the initial decisions. autocreate
9. now autocreate field
10. now clean up the cli prints 
11. now add a score counter


