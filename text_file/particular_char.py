# read a file and find all words starting with a particular character
startswith_char = []
fp = open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r")
r=fp.read()
num_of_words = r.split()
#print(num_of_words)
for word in num_of_words:
    #print(word)
    #if word.startswith("a"):
    if word.strip().startswith("a"):
        startswith_char.append(word)
        print(startswith_char)
