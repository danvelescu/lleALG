# a = 0
# try:
#     a = int(input("dai mne nomer"))
# except ValueError:
#     print("Inavlid data")
#
# if a == 1 and True or 1 == 1:
#     print("one")
# elif a == 2:
#     print("two")
# elif a == 3:
#     print("three")
#
# if True or False:
#     print("true")
#
# if True and False:
#     print("true")
# else:
#     print("False")
#
# word = ''
# while word != "stop":
#     word = input("set word")
#     print("asdas")

# a = [1, 2, 3, 4, 99, 123, 123, 123, 124, 1, 99999, 241, 24, 124, 124]
# summ = 0
# for nr in a:
#     summ += nr
# print(summ)
#
# for x in range(1, 10):
#     if (x == 5):
#         break
#     print(x)
#
# text = input("set number")
# numbers = [1, 12, 3234, 234, 234, 324, 234, "da", "324"]
#
# i = 0
#
# for el in numbers:
#     if (str(el) == text):
#         print(i)
#     i += 1

array = [12, 23, 12, 312, 3, 3, 3, 23, 12]
dictionary = {"s": "asd", "sada": 1, "Key": "Value"}
tuple = (1, 2, 31, 23)
set = {"ss", "Asdas", "ss", "Asdas", 1, 1, 1, 1, 1, 11, 1, 1}


def nameOfFunction(array):
    for nr in array:
        c = 0
        for nr1 in array:
            if (nr == nr1):
                c += 1
        print("Number:" + str(nr) + " Count:" + str(c))

nameOfFunction(array)
