def calculate_sum(num1, num2):
    summarum = num1 + num2
    return summarum


def calculate_cube(num):
    cube = num ** 3
    return cube


def count_steps(total_distance, step_length):
    step_count = int(total_distance//step_length)
    return step_count


def absolute_distance(num1, num2):
    diff = num2 - num1
    abs_dist = (diff ** 2) ** (1/2)
    return abs_dist


print(calculate_sum(100, 2))
print(calculate_cube(2))
print(count_steps(100.5, 2))
print(absolute_distance(-2, -5))
