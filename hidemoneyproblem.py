row1 = ['😀', '😀', '😀']
row2 =['😀', '😀', '😀']
row3 =['😀', '😀', '😀']

matrix =[row1,row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("enter the position to hide our  money")
row_selected = matrix[int(position[0])-1]
row_selected[int(position[1])-1] ='X'
print(f"{row1}\n{row2}\n{row3}")