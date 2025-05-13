# Roman number on each digits
THOUSANDS   =  ['', 'M', 'MM', 'MMM']
HUNDREDS    =  ['', 'C', 'CC', 'CCC', 'CD',
                'D', 'DC', 'DCC', 'DCCC', 'CM']
TENS        =  ['', 'X', 'XX', 'XXX', 'XL',
                'L', 'LX', 'LXX', 'LXXX', 'XC']
ONES        =  ['', 'I', 'II', 'III', 'IV',
                'V', 'VI', 'VII', 'VIII', 'IX']

# Input
num = int(input())
# Output
print(THOUSANDS[num // 1000], end = '')
num %= 1000
print(HUNDREDS[num // 100], end = '')
num %= 100
print(TENS[num // 10], end = '')
num %= 10
print(ONES[num])