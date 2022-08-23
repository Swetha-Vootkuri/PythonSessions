# read a file and count the occurence of each character

def letterFrequency(fileName, letter):
    file = open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", 'r')
    text = file.read()
    return text.count(letter)
print(letterFrequency('poem.txt', 'a'))