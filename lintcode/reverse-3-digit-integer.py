num = 900
str1 = str(num)
# print(str1)
arr = []
for item in str1:
    arr.append(item)

arr.reverse()
print(arr)
print(int(''.join(arr)))


def reverseInteger(self, number):
    num_str = str(number)
    num_arr = []
    for item in num_str:
        num_arr.append(item)

    num_arr.reverse()
    return int(''.join(num_arr))


class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        num_str = str(number)
        num_arr = []
        for item in num_str:
             num_arr.append(item)

        num_arr.reverse()
        return int(''.join(num_arr))