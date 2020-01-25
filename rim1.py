# По задонаму числу сформировать его римскую запись
# I - 1
# IV - 4
# V - 5
# IX - 9
# X - 10
# XIV - 14
# XX - 20
# XL - 40
# L - 50
# XC - 90
# C - 100
# CD - 400
# D - 500
# CM - 900
# M - 1000

n1 = 7
n2 = 9
n3 = 31
n4 = 45
n5 = 56
n6 = 105
n7 = 221
n8 = 232
n9 = 4
n10 = 2123

def get_rim(n):
    result = 'I' * n

    result = result.replace('I' * 5, 'V')
    result = result.replace('V' * 2, 'X')
    result = result.replace('X' * 5, 'L')
    result = result.replace('L' * 2, 'C')
    result = result.replace('C' * 5, 'D')
    result = result.replace('D' * 2, 'M')

    result = result.replace('DCCCC', 'CM')
    result = result.replace('CCCC', 'CD')
    result = result.replace('LXXXX', 'XC')
    result = result.replace('XXXX', 'XL')
    result = result.replace('VIIII', 'IX')
    result = result.replace('IIII', 'IV')

    return result

print(get_rim(n1))
print(get_rim(n2))
print(get_rim(n3))
print(get_rim(n4))
print(get_rim(n5))
print(get_rim(n6))
print(get_rim(n7))
print(get_rim(n8))
print(get_rim(n9))
print(get_rim(n10))

