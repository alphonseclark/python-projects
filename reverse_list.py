def reverse_list(list):
    result=[]
    for i in range(len(list)):
        result.append(list[-i-1])
    print(result)
    
reverse_list([1,2,3,4])