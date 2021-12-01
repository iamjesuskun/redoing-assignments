with open("input.txt", "r") as file:
    data = file.readlines()
for i in range(len(data)):
    data[i] = int(data[i].rstrip())
    
counter = 0

for i in range(1,len(data)):
    if data[i] > data[i-1]:
        counter +=1
print(counter)