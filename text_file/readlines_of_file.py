#read a text file and print line by line
fp = open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r")
r1=fp.readlines()
for line in r1:
    #print(line)    #Gives results with gap between each line
    print(line.strip()) #Gives results line by line without gap between each line
