#read a file and find the line count
fp = open("C:\\Users\\SVI22\\PycharmProjects\\PythonSessions\\text_file\\poem", "r")
lines= fp.readlines()
print(type(lines))
line_count = 0
for line in lines:
  line_count += 1
print(line_count)

#line_count = len(lines)