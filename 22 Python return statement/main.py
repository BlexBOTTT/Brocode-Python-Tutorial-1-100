# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number_1, number_2):
    result = number_1 * number_2
    return result

x = multiply(6, 2)

print(x)