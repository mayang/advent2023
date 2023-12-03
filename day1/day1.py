import re

file = open('input.txt')
# file = ['1abc2',
# 'pqr3stu8vwx',
# 'a1b2c3d4e5f',
# 'treb7uchet']

total = 0

for line in file:
  config = re.findall(r'\d{1}', line)
  config_no = config[0] + config[-1]
  total = total + int(config_no)

print (total)