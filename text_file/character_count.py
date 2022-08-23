#read a file, find the character count
fp = open("poem", "r")
r=fp.read()
num_of_char = len(r)
print(num_of_char)