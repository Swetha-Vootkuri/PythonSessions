#read a file and count the occurence of each word

fp = open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r")
data = fp.read()
word_data = input("Enter each word: ")
word_occurrences = data.count(word_data)
print('Number of occurrences of the word :', word_occurrences)