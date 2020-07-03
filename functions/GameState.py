def game_state():
    input_list=[[1, 0, 0], [0, 1, 1], [0, 0, 1]]
    print(input_list)
    if input_list[0][0] == 1 and input_list[1][1] == 1 and input_list[2][2]:
        return True
    else:
        return False

        

print(game_state())
