#bubble sort-taking input from the user
def b_sort(list):

for iter_num in range(len(list)-1,0,-1):
    for idx in range(iter_num):

        if list[idx] > list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp

str_input= input("Enter numbers:  ")
list = [int(x) for x in str_input.split()]

b_sort(list)
print('sorted elements are: ')
print(list)
