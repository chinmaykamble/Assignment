##### Question 1

### solution one using locale
import locale
locale.setlocale(locale.LC_NUMERIC, "en_IN") # set the locale to Indian English
num = 504678
ans = locale.format_string("%d", num, grouping=True) # format the number with grouping
print(ans) # output: 5,04,678


## Solution 2 pythonic way
# Converted the initial number to string

s = str(num)

## List comprehension 

"""
divide the string into 2 digit substring excluding the last 3 characters right to left.
[::-1] to reverses the order of the list.
[s[-3:]] gets the last three characters of s.
+ is a concatenation operator that joins two lists together
",".join(...) is a string method that joins the elements of a list with a specified separator, which is ',' 
"""

d = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
print(d)
