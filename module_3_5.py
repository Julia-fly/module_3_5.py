def get_multiplied_digits(number):
    str_number= str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    rest_product = get_multiplied_digits(int(str_number[1:]))
    if rest_product == 0:
        rest_product = 1
        return first* rest_product
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)