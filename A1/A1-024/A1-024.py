# Input
year = int(input())
motor = int(input())
# Output
TAX = [[1250, 1400, 2000],
       [1100, 1300, 1700],
       [1000, 1200, 1500]]

YEAR_TYPE = 1
if(year <= 1990):
    YEAR_TYPE = 0
if(year >= 2000):
    YEAR_TYPE = 2

MOTOR_TYPE = 1
if(motor <= 1500):
    MOTOR_TYPE = 0
if(motor > 2000):
    MOTOR_TYPE = 2

print(TAX[YEAR_TYPE][MOTOR_TYPE])