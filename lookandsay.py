def lookandsay(n):
    """
    Returns the look-and-say sequence of the n-th term
    """
    if n <= 0:
        raise ValueError('Reference integer should be positive-signed.')
    elif n == 1:
        return '1'
    elif n ==2:
        return '11'

    # Seeding assuming that 2 rounds of iteration has been performed to sidestep corners
    i = 3
    prev_number_string = '11'

    while i <= n:
        # Count numbers in string
        curr_char = prev_number_string[0]
        char_count = 1
        this_number_string = ''

        for char in prev_number_string[1:]:
            if char != curr_char:
                this_number_string = this_number_string + str(char_count) + curr_char
                curr_char = char
                char_count = 1
            else:
                char_count += 1

        this_number_string = this_number_string + str(char_count) + curr_char
        prev_number_string = this_number_string
        i += 1

    return this_number_string


if __name__ == '__main__':
    print(lookandsay(100))