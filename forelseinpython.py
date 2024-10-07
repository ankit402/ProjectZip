numbers = [2,3,5,-1,0,53]

for i in numbers:
    if i == 5:
        print("stop printing due to break")
        break
    print(i)
else:
    print("successfully")