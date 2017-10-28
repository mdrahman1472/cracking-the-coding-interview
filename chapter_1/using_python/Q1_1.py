__author__ = 'Rahman'

"""
This is my code.
book's sol on java file where she used boolean array for tracking which is good interm of size of boolean value.
She also check first if length of string is more than 128 which indicate there is repetation any/some chars then retun false
"""
def isUniqeChars(s):
    str_char = [0]*128 # 128 chars initialize as 0

    for c in s:
        index = ord(c)
        if (str_char[index] == 0):
            str_char[index] += 1

        else:
            return False

    return True


# Test
str = "abty97kl/)4,"
print(isUniqeChars(str))

