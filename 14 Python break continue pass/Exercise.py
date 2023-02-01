# https://pynative.com/python-break-continue-pass/


def for_loop_break():
    numbers = [10, 40, 120, 230]
    for i in numbers:
        if i > 100:
            break
        print('current number', i)


def while_loop_break():
    name = 'Jesaa29 Roy'

    size = len(name)
    i = 0
    # iterate loop till the last character
    while i < size:
        # break loop if current character is space
        if name[i].isspace():
            break
        # print current character
        print(name[i], end='')
        i = i + 1


def nested_for_loop_break_inner():
    for i in range(1, 11):
        print('Multiplication table of', i)
        for j in range(1, 11):
            # condition to break inner loop
            if i > 5 and j > 5:
                break
            print(i * j, end=' ')
        print('')


def nested_loop_break_outer():
    for i in range(1, 11):
        # condition to break outer loop
        if i > 5:
            break
        print('Multiplication table of', i)
        for j in range(1, 11):
            print(i * j, end=' ')
        print('')


def for_loop_continue():
    numbers = [2, 3, 11, 7]
    for i in numbers:
        print('Current Number is', i)
        # skip below statement if number is greater than 10
        if i > 10:
            continue
        square = i * i
        print('Square of a current number is', square)


def while_loop_continue():
    name = 'Je sa a'

    size = len(name)
    i = -1
    # iterate loop till the last character
    while i < size - 1:
        i = i + 1
        # skip loop body if current character is space
        if name[i].isspace():
            continue
        # print current character
        print(name[i], end='')


def nested_for_loop_continue_inner():
    for i in range(1, 11):
        print('Multiplication table of', i)
        for j in range(1, 11):
            # condition to skip current iteration
            if j == 5:
                continue
            print(i * j, end=' ')
        print('')


def nested_for_loop_continue_outer():
    for i in range(1, 11):
        # condition to skip iteration
        # Don't print multiplication table of even numbers
        if i % 2 == 0:
            continue
        print('Multiplication table of', i)
        for j in range(1, 11):
            print(i * j, end=' ')
        print('')

def for_loop_pass():
    months = ['January', 'June', 'March', 'April']
    for mon in months:
        pass
    print(months)
