## Question 2

input_data = '''3
4 10
2 13 4 16
5 8
9 3 8 8 4
4 6
1 2 3 4'''

## Basic function to check if the input string matches the input format.. can be improved.
def check_input(lines):
    if ((len(lines[1:])/2 % int(lines[0])) == 0) & (int(lines[0])>1):
        return True
    else:
        print("please check the input")

def min_number(lines):
    if check_input(lines): ## proceed only if input is valid
        # list comprehensions to split the lines list into set of two nested lists
        # one for the height one for the players
        heights = [line.split() for line in lines[1::2]]
        players = [line.split() for line in lines[2::2]]

        for i in range(len(heights)):
            # list comprehension to compare player heights with K, ie height if ALI,
            # only get the numbers greater then N and then the lenght of the list, ie the solution in this case
            print(len([ans for ans in players[i] if int(ans)>int(heights[i][1])]))

## Split the input data into list
lines = input_data.splitlines()

## calling the min_number function to get the desired output
min_number(lines)
