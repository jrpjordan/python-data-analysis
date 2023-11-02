path = "examples/segismundo.txt"

# By default, is opened in read 'r' mode
f = open(path, encoding="utf-8")

for line in f:
    print(line)
    
# lines come out of the file with the EOL markers intact, you can get EOL free list:
lines = [x.rstrip() for x in open(path, encoding="utf-8")]

print(lines)

# with block ensures that resources will be free after reading from file
with open(path, encoding="utf-8") as f:
    lines = [x.rstrip() for x in f]


# With read we can read characters and also mode=rb is Binary mode
f1 = open(path)
print(f1.read(10))

f2 = open(path, mode="rb")
print(f2.read(10))

# also tell can tell you the current position
print(f1.tell())
print(f2.tell())

import sys
print(sys.getdefaultencoding())

# To write text into a file...
with open("tmp.txt", mode="w") as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)

with open("tmp.txt") as f:
    lines = f.readlines()

print("Copied file.......")
print(lines)