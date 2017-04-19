#문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에
#그 반복 횟수를 표시하여 문자열을 압축하기.

#입력 예시: aaabbcccccca
#출력 예시: a3b2c6a1

import sys
string = sys.argv[1]

def del_duplicate(s):
    result = s[0]
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]: count+= 1
        else:
            result += str(count) + s[i+1]
            count = 1
    result += str(count)
    return result

print(del_duplicate(string))



"""
import sys

i_string = sys.argv[1]
o_string = ""
count = 1
for i in range(1, len(i_sting)):
    if i_string[i-1] == i_string[i]:
        count += 1
    else:
        o_string += i_string[i-1]+str(count)
        count = 1
o_string += i_string[-1] + str(count)
print(o_string)
"""