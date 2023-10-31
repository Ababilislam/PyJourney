def check_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evn_num_iter = filter(check_even, numbers)

evn_num = list(evn_num_iter)

print(evn_num)
