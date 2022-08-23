#read a file and find all the unique word count

count = 0
'''with open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r") as fp:
    content = fp.read()

words_list = content.split() #It gives list of lines
#print(words_list)
unique_word_list = set(words_list)
print(unique_word_list)
'''
#or

with open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r") as fp:
    lines = fp.readlines()
words_list = []
for line in lines:
    #print(line.split())
    #words_list.extend(line) #It gives each letter as a result in list
    words_list.extend(line.split())
    print(words_list)
    #print(len(words_list)) #Gives each line word count and then add that count to second line and gives total
unique_words_list = set(words_list) #removes duplicates
print(unique_words_list) #gives all words in a set without adding each line by line
print(len(unique_words_list)) #Gives total word count for all lines without duplicates