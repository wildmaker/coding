# 给定年月日的数字，打印出格式化的日期
MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

SUFFIX = ['st', 'nd', 'rd'] + 17 * ['th'] \
       + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
q = True
while q:
    Year = input("Year: ")
    Month = input("Month: ")
    Day = input("Day: ")
    q = "q" != input("PRESS 'q' TO EXIT.")