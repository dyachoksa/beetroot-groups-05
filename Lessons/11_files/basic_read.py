f = open("data.txt", "r")

# content = f.read()
# print("Content of the file:\n", content)

print("Content of the file:")
# or read line-by-line
for line in f:
    print(line)

f.close()
