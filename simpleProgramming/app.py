# read data.dat file and save each line in index of array
with open("data.dat") as file:
    lines = file.readlines()

# define a function for counting 0s and 1s of each line
def count(num):

    ones = 0
    zeros = 0
    
    for temp in num:
        if temp == "0":
            zeros += 1
        elif temp == "1":
            ones += 1

    return {
            "zeros": zeros,
            "ones": ones
            }


# define a count variable to count number of lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2

countLines = 0

for line in lines:
    if (count(line)["zeros"]) % 3 == 0 or (count(line)["ones"]) % 2 == 0:
        countLines += 1

print (countLines)


