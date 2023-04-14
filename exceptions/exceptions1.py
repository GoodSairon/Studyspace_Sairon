def un_num (numbers):
    try:
        for i in numbers:
            i = int(i)
        setnumbers = set(numbers)
        if len(numbers) == len(setnumbers):
            print("All numbers are unique")
        else:
            print("Not all numbers are unique")
    except ValueError as exc:
        print(exc)

un_num(input('Enter numbers separated by space: ').split())
