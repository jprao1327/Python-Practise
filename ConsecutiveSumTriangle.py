def con_sum(int_list):
    list_b=[]
    end_index=len(int_list)-1
    for i in range(end_index):
        con_sum_value=int_list[i]+int_list[i+1]
        list_b.append(con_sum_value)
    return(list_b)    
def consecutive_triangle(int_list):
    print(int_list)
    while len(int_list)>1:
        con_sum_list=con_sum(int_list)
        print(con_sum_list)
        int_list=con_sum_list
def convert_list_into_int_list(list_a):
    list_b=[]
    for item in list_a:
        list_b+=[int(item)]
    return list_b    


int_list=list(map(int,input().split(",")))
consecutive_triangle(int_list)
