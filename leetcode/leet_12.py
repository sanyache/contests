def intToRoman(nums):
    R = {1: 'I', 5 : 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    n = ''
    pow = 1
    buff = ''
    for num in nums[::-1]:
        tmp = int(num)*pow
        if tmp < 4*pow:
            buff = R[pow]*int(num)
        elif tmp == 4 * pow:
            buff = R[pow] + R[5*pow]
        elif 4*pow < tmp < 9*pow:
            buff = R[5*pow] + R[pow]*(int(num) - 5)
        else:
            buff = R[pow] + R[pow*10]
        pow *= 10
        n = buff + n

    return n

roman = input()
print(intToRoman(roman))