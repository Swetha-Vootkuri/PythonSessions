#read a file, find the word count

#read a file, find the character count
count = 0
fp = open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r")
r=fp.read()
#print(r)
word_list = r.split()
print(word_list)
word_to_find = "personal"
for word in word_list:
    if word_to_find == word:
        count += 1
print(count)

#or
word_count = word_list.count(word_to_find)
print(word_count)

