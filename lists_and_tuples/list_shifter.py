def shift_list(list_of_numbers, start_position):
    shift_direction = None
    while type(shift_direction) != int and shift_direction != 1 or 2:
        try:
            shift_direction = int(input("Please enter 1 to rotate numbers to the left, 2 to the right: "))
        except ValueError:
            print("Shift_direction value not valid. Value must be 1 or 2")
        if shift_direction == 1:
            shifted_list = list_of_numbers[1:(start_position + 1)] + list_of_numbers[start_position+1:]
            shifted_list.append(list_of_numbers[0])
            return print(shifted_list)
        elif shift_direction == 2:
            shifted_list = list_of_numbers[0:(start_position)] + list_of_numbers[(start_position):len(list_of_numbers)-1]
            shifted_list.insert(0,list_of_numbers[len(list_of_numbers)-1])
            return print(shifted_list)


test_list = [78,9,20,45,5,66,77]
shift_list(test_list, 3)
