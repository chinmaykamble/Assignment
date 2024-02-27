##### Question 1
import locale
locale.setlocale(locale.LC_NUMERIC, "en_IN") # set the locale to Indian English
num = 504678
ans = locale.format_string("%d", num, grouping=True) # format the number with grouping
print(ans) # output: 5,04,678


s = str(num)

d = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
print(d)
