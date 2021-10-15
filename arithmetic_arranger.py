def arithmetic_arranger(problems, result_flag=False):
    def error_check(fac):
        # Checks for the errors specifies

        # Checks for correct number of problems
        if len(fac) > 5:
            return 'Error: Too many problems.'

        #for all problems we check for errors
        for elem in fac:
            # Check that we only have + and - operators
            if elem[1] == '*' or elem[1] == '/':
                return "Error: Operator must be \'+\' or \'-\'."
            #Check the number of digits must be <4 in first operand
            if any(c.isalpha() for c in elem[0]):
                return "Error: Numbers must only contain digits."

            #Check the number of digits must be <4 in second operand
            if any(c.isalpha() for c in elem[2]):
                return "Error: Numbers must only contain digits."
            # check that there are only number characters

            if len(elem[0]) > 4 or len(elem[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'

    def rearange(fac, flag):
        # Rearanges the equations

        # For each equation save the length of the largest number
        # It will be used to arrange number based on that
        max_len = [max(len(elem[0]), len(elem[2])) for elem in factors]

        first_line = []
        second_line = []
        third_line = []

        # make seperate string for each line
        for i in range(len(factors)):
            first_line += [(' ' * (max_len[i] - len(factors[i][0]) + 2) +
                            factors[i][0] + ' ' * 4)]
            second_line += [(factors[i][1] + ' ' *
                             ((1 + max_len[i] - len(factors[i][2]))) +
                             factors[i][2] + ' ' * 4)]
            third_line += [('-' * (max_len[i] + 2) + ' ' * 4)]

        # Remove empty characters after the last number
        first_line = ''.join(first_line).rstrip()
        second_line = ''.join(second_line).rstrip()
        third_line = ''.join(third_line).rstrip()

        # combine all lines
        rearanged = first_line + '\n' + second_line + '\n' + third_line

        # if I want the result of the equation we receive a second bool variable
        if flag == True:
            first_num = []
            second_num = []
            operator = []
            result = []
            # Turn all numbers to integers
            first_num = [int(elem[0]) for elem in fac]
            second_num = [int(elem[2]) for elem in fac]
            operator = [(elem[1]) for elem in fac]

            for i in range(0, len(fac)):
                # Depending on operation we append each result on the list
                if operator[i] == '+':
                    result.append(first_num[i] + second_num[i])

                if operator[i] == '-':
                    result.append(first_num[i] - second_num[i])

            # turn all elements to strings and then the variable that the results are saved to a list
            result = map(str, result)
            result = list(result)

            # combine all elements in a single string including spacing
            result = [
                ' ' * (max_len[i] - len(result[i]) + 2) + (result[i]) + ' ' * 4
                for i in range(len(fac))
            ]
            result = ''.join(result).rstrip()
            rearanged = rearanged + '\n' + result

        return rearanged

    # main part

    # seperate the input to lists that contain strings with operand1 operator operand 2
    factors = [elem.replace(' +-', '').split() for elem in problems]
    error_message = " "
    error_message = error_check(factors)

    # checks for wrong input and returns error message
    if error_message != None:
        return error_message
    # rearange the inputs
    arranged_problems = rearange(factors, result_flag)

    return arranged_problems
