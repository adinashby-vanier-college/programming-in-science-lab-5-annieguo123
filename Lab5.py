# Example for n = 5: USING WHILE LOOP
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range(n):
        for j in range(n):
            if(i == 0 or i == n - 1 or j == 0 or j == n - 1):
                result += "*"
            else:
                result += " "
        result += "\n"
    return result.rstrip()

print(hollow_square(5))

# USING WHILE LOOP:
# 1
# 12
# 123
# 1234

def number_pattern(n):
    result =""
    i = 1

    while i <= n:
        j = 1
        while j <= i:

            # result = result + str(j)
            result += str(j)
            j += 1

        if i != n:
            result += "\n"

        i += 1

    return result


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15 USING A WHILE LOOP
def sum_of_natural_numbers(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum

print(sum_of_natural_numbers(3))


       









# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        for j in range(n - i - 1):
            result += " "

        for k in range(((i + 1) * 2) - 1):
            result += "*"
        result += "\n"

    return result.rstrip()

print(centered_star_pyramid(4))
