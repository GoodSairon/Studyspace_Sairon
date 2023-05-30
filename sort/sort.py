import random as rand
import string
import timeit

def gen_rand_string():
    letters = string.ascii_lowercase
    return ''.join(rand.choice(letters) for i in range(rand.randint(1, 6)))


def sort(list):
    for num in range(len(list)):
        min_value = num
        for item in range(num, len(list)):
            if list[min_value] > list[item]:
                min_value = item
        list[num], list[min_value] = list[min_value], list[num]
    return list

int_list = [rand.randint(0, 1000) for i in range(1, 5000)]
float_list = [round(rand.uniform(0.1, 100.0), 2) for i in range(1, 5000)]
str_list = [gen_rand_string() for i in range(1, 5000)]

print(sort(int_list))
print(sort(float_list))
print(sort(str_list))

print(timeit.timeit("sort(int_list)", globals = globals(), number = 1))
print(timeit.timeit("sort(float_list)", globals = globals(), number = 1))
print(timeit.timeit("sort(str_list)", globals = globals(), number = 1))
