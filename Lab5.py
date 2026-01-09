# Example for n = 5: USING WHILE LOOP
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n <= 0:
        return ""

    result = ""
    i = 0

    while i < n:
        if i == 0 or i == n - 1:
            result += "*" * n
        else:
            if n == 1:
                result += "*"
            else:
                result += "*" + " " * (n - 2) + "*"

        if i != n - 1:
            result += "\n"

        i += 1

    return result
print(hollow_square(5))

# USING WHILE LOOP:
# 1
# 12
# 123
# 1234

# def number_pattern(n):
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
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

print(sum_of_natural_numbers(5))


# FOR LOOP:

# def sum_of_natural_numbers(n):
#     sum = 0
#     for i in range(n+1):
#         sum += i
#     return sum
# print(sum_of_natural_numbers(8))
       









# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    if n <= 0:
        return ""
    result = ""
    i = 0

    while i < n:
        if i == 0:
        result += " " * (n-1) + "*" + " " * (n-1)
