def nm_by_num():
    try:
        num = int(input("Enter place number:"))
    except ValueError:
        print("It isn't number")
        return None
    if int(num) <= 0:
        raise ValueError('Number must be more than zero')
        return None
    print("Your's place")

nm_by_num()
