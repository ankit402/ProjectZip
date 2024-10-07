list =input("enter the list separated by space")
height_list = list.split()
count = 0
for i in height_list:
    count  = count+1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])
print(height_list)
sum = 0;
for k in height_list:
    sum += k
    avg = sum/count

print(avg)

