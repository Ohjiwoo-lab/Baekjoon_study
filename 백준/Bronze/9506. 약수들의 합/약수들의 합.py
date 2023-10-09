while True:
    num_list=[]
    n=int(input())
    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            num_list.append(i)
    if sum(num_list)==n:
        print(f"{n} = ", end="")
        for j in range(len(num_list)):
            if j!=len(num_list)-1:
                print(f"{num_list[j]} + ", end="")
            else:
                print(f"{num_list[j]}")
    else:
        print(f"{n} is NOT perfect.")