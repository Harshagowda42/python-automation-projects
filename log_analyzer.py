count = 0

file = open("server.log", "r")

for line in file:
    if "ERROR" in line:
        print(line)
        count += 1

print("Total Errors:", count)

file.close()