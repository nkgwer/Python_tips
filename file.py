f = open('text.txt', 'w')
f.write('I have a pen! I have an apple... oh! apple pen')
f.close()

with open("text.txt", "r") as file:
    line = file.read()
    print(line)
    # no need to close
