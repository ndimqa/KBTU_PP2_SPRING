# https://www.hackerrank.com/challenges/validating-the-phone-number/problem 
# Validating phone numbers

import re

m = int(input())

for i in range(m):
    if re.match(r'[7-9]\d{9}$',raw_input()):   
        print 'YES'  
    else:  
        print 'NO'