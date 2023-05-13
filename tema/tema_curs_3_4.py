import math


# def my_function_args(*args, **kargs):
#     my_sum = 0
#     for i in args:
#         if type(i) == int or type(i) == float:
#             my_sum = my_sum + i
#     print(my_sum)
#
#
# my_function_args(1, 2.5, -3, "abc", [12, 56, "cad"])
# my_function_args()
# my_function_args(2, 4, "abc", param_1=2)
#
#
# def my_function_all(my_list):
#     if len(my_list) == 0:
#         return 0
#     my_sum_total = my_list[0] + my_function_all(my_list[1:])
#     return my_sum_total
#
#
# print(my_function_all([2, 3, 4, 7, 2]))
#
#
# def my_function_even(my_list):
#     if len(my_list) == 0:
#         return 0
#     if my_list[0] % 2 == 0:
#         my_sum_even = my_list[0] + my_function_even(my_list[1:])
#     else:
#         return my_function_even(my_list[1:])
#     return my_sum_even
#
#
# print(my_function_even([2, 3, 4, 7, 2]))
#
#
# def my_function_odd(my_list):
#     if len(my_list) == 0:
#         return 0
#     if my_list[0] % 2 != 0:
#         my_sum_odd = my_list[0] + my_function_odd(my_list[1:])
#     else:
#         return my_function_odd(my_list[1:])
#     return my_sum_odd
#
#
# print(my_function_odd([2, 3, 4, 7, 2]))
#
#
# def my_function():
#     user_input = input("Please insert a character: ")
#     try:
#         my_int = int(user_input)
#         return my_int
#     except ValueError:
#         return 0
#
#
# print(my_function())


class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"Numarator : {self.numarator}, Numitor: {self.numitor}"

    def add(self, other):
        numarator = (self.numarator * other.numitor) + (self.numitor * other.numarator)
        numitor = self.numitor * other.numitor
        cmmdc = math.gcd(numarator, numitor)
        numarator_final = int(numarator / cmmdc)
        numitor_final = int(numitor / cmmdc)
        return Fractie(numarator_final, numitor_final)

    def subtract(self, other):
        numarator = (self.numarator * other.numitor) - (self.numitor * other.numarator)
        numitor = self.numitor * other.numitor
        cmmdc = math.gcd(numarator, numitor)
        numarator_final = int(numarator / cmmdc)
        numitor_final = int(numitor / cmmdc)
        return Fractie(numarator_final, numitor_final)
    def inverse(other):
        numaratorul_nou = other.numitor
        numitorul_nou = other.numarator
        return Fractie(numaratorul_nou, numitorul_nou)
f_1 = Fractie(2, 4)
f_2 = Fractie(5, 2)

print(f_1)
result_add = f_1.add(f_2)
result_subtract = f_1.subtract(f_2)
result_inverse = f_2.inverse()
print(result_add)
print(result_subtract)
print(result_inverse)
