def print_fibonacci_sequence():

    sequence_controller = 0
    index = 0
    first_term = 1
    sum = 0

    number_of_sequence = int(input("Please enter a number and see the fibonacci sequence: "))

    #A storage that holds the sum of the previous two numbers
    sum_storage = [1]
    print(f"The first {number_of_sequence + 1} number of the fibonacci series is : {first_term}", end=" ")

    #Iterate the whole process by adding the current sum to the previous number in the list
    while(sequence_controller < number_of_sequence):
        sum += sum_storage[index - 1]
        print(sum, end=" ")
        sum_storage.append(sum)
        sequence_controller+=1
        index+=1
    print("\nThe nth number in the fibonnaci series is: ",sum)

print_fibonacci_sequence()
