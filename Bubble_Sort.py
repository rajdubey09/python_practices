#Bubble Sort

def bubble_sort(elements_list):
    #sorted_list = sorted(elements_list)
    for k in range(len(elements_list) -1):
        for i in range(len(elements_list) -1 -k): #k is used bcoz last elements after each iteration is sorted to last k positions
            if elements_list[i] > elements_list[i+1]:
                tmp = elements_list[i]
                elements_list[i] = elements_list[i+1]
                elements_list[i+1] = tmp
        #print(elements_list) #to understand step by step sorting
                
    return elements_list #comment this while printing step by step output

if __name__ == '__main__':

    #elements = [55,53,57,56,59,51,52]
    elements = list(map(int,input("Enter the Elements of the List").split()))
    print("Before Bubble Sorting...")
    print(elements)
    #bubble_sort(elements)
    res = bubble_sort(elements) #comment this while printing step by step output
    print("After Bubble Sorting...")
    print(res) #comment this while printing step by step output
