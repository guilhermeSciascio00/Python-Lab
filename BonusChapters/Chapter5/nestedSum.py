#this code will get a list and sum all the elements inside it 

def nested_sum(elements : list):
    total = 0
    for i in range(len(elements)):
        for j in range(len(elements[i])):
            total += elements[i][j]
    print(f"The total sum of the nested list is: {total}")

nested_list = [[1,2], [3], [4,5,6]]
nested_sum(nested_list)
