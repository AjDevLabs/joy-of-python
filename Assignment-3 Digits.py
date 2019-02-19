#Programming Assignment-3: Digits
"""
You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

Input Format:
The first line contains a number made up of 0's and 1's.

Output Format:
Print 'YES' or 'NO' accordingly without quotes.

Example:
Input:101
Output:YES
"""

#method one : By counting no of zeros and one if no of zeros ==1 or no of one ==1
num = input()
o=num.count('0')
i=num.count('1')
if o==1 or i==1:
     print("YES",end='')
else:
     print("NO",end='')
#method two : By counting no. of digits and sum of digits
# if no.of digit == sum-1 or ==sum

