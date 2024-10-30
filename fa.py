
N = int(input())
List = []
list = []
while N > 0:
    List.append(int(input()))
    N -= 1

        
for num in List:
    if num % 2 == 0:
        list.append(num)
    else: 
        pass
print(sum(list))
