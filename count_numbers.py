try:
    with open('number.txt') as f:
        # get the strings from the file skipping the commented lines '#'
        str_numbers = [number.strip() for number in f if '#' not in number]
        # convert the string to float skipping empty string
        numbers = [float(number) for number in str_numbers if not len(number) == 0]
        # print the sum of the numbers in the list
        print(sum(numbers))
except IOError:
    print("It looks like something went wrong :(")
