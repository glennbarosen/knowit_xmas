def findMissingNum(numlist):
    n = len(numlist)
    total = (n + 1) * (n + 2) / 2
    sum_of_numlist = sum(numlist)
    return total - sum_of_numlist


f = open("numbers.txt", "r")
num_as_string = f.read().split(",")
num_as_int = list(map(int, num_as_string))
missing_num = findMissingNum(num_as_int)
print(missing_num)