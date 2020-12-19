import math


print('\n\t\t\tAssignment 1 - Q1.1 - start'
      '\n--------------------------------------------------------------------------')
point_values_one = int(input("Enter number one : "))
print("User enter number one : ", point_values_one)
point_values_two = int(input("Enter number two: "))
print("User enter number two : ", point_values_two)


def floating_point_values(k):
    count = 0
    if k > 0:
        for i in range(k):
            count = count + 1
        return count
    if k < 0:
        for i in range(k, 0):
            count = count + 1
        return count


if floating_point_values(point_values_one) == floating_point_values(point_values_two):
    print('\tAbsolute value equal', point_values_one, point_values_two)
else:
    print('\tAbsolute value not equal', point_values_one, point_values_two)

print('\n\t\t\tAssignment 1 - Q1.1 - end'
      '\n----------------------------------------------------------------------------')

print('\n\t\t\tAssignment 1 - Q1.2 - start'
      '\n-----------------------------------------------------------------------------')
input_number = int(input("Enter number: "))
print("user enter number : ", input_number)


def sqrt(y):
    ans = 0
    if y >= 0:
        while ans * ans < y: ans = ans + 1
        if ans * ans != y:
            # print(x, 'is not a perfect square')
            return False
        else:
            return True
    else:
        # print(x, 'is a negative number')
        return False


for x in range(input_number):
    if sqrt(x) and (x % 2) != 0:
        print('\tOdd prefect square numbers :', x)
print('\n\t\t\tAssignment 1 - Q1.2 - end'
      '\n---------------------------------------------------------------------------')

print('\n\t\t\tAssignment 1 - Q1.3 - start'
      '\n---------------------------------------------------------------------------')
area = 235
user_enter_side_length = int(input(
    "235 square meter rectangle is there, \nif you guest length, would be provide width \nenter your guest length : "))
print('\n\n\tyou enter length is ', user_enter_side_length, ' meter width is ', area / user_enter_side_length, ' meter')

print('\n\t\t\tAssignment 1 - Q1.3 - end'
      'n----------------------------------------------------------------------------')

print('\n\t\t\tAssignment 1 - Q2 - start'
      '\n---------------------------------------------------------------------------')
request_count = int(input("Enter number: "))
print("user request fried chicken count : ", request_count)


def fried_chicken_package(z):
    if z < 6:
        print('\tSorry there is no available package according to you request count : ', z)
    elif z == 6:
        print('\tYou are able to select 6 fried chicken package\n\t you can use any of following option to buy\n')
    elif z < 9:
        print('\tYou are able to select 6 fried chicken package\n\t you can use any of following option to buy\n')
    elif z == 9:
        print(
            '\tYou are able to select 6 fried chicken package and 9 fried chicken package\n\t you can use any of '
            'following option to buy\n')
    elif z < 20:
        print(
            'You are able to select 6 fried chicken package and 9 fried chicken package\n\t you can use any of '
            'following option to buy\n')
    elif z == 20 or 20 < z:
        print(
            '\tYou are able to select 6 fried chicken package, 9 fried chicken package and 20 fried chicken '
            'package\n\t you can use any of following option to buy\n')
    pack_one = z // 6
    pack_two = z // 9
    pack_three = z // 20
    a = 1
    for l in range(pack_one + 1):
        for m in range(pack_two + 1):
            for n in range(pack_three + 1):
                if l * 6 + m * 9 + n * 20 == z:
                    print(
                        '\t\toption = {0}\nyou can buy packages of 6 pieces : {1} \npackages of 9 pieces : {2} '
                        '\npackages of 20 pieces : {3}\nTotal pieces count : {4}\n'.format(a, l, m, n,
                                                                                           (l * 6 + m * 9 + n * 20)))
                    a = a + 1


print(' you can not buy any pieces')

fried_chicken_package(request_count)
print('\n\t\t\tAssignment 1 - Q2 - end\n----------------------------------------------------------------------------')

print('\n\t\t\tAssignment 1 - Q3 - start\n--------------------------------------------------------------------------')
base = int(input("Please enter any positive integer : "))
print("you entered base : ", base)
exponent = int(input("Enter exponent : "))
print("you entered exponent : ", exponent)


def integer_power_exponents(a, y):
    if a > 0:
        result = 1.00
        for a in range(a):
            result = result * y
        print('\tYou enter positive number as exponent, \n\t\tYou entered exponent value :', a,
              '\n\t\tbase value you entered : ', y, '\n\t\tanswer is : ', result)


integer_power_exponents(exponent, base)

power = math.pow(base, exponent)

print("\tUsing math pow\n\t\tThe Result of {0} Power {1} = {2}".format(base, exponent, power))
print('\n\t\t\tAssignment 1 - Q3 - end\n----------------------------------------------------------------------------')
