#Insertion sort

def insertion_sort(elements_list):
    for i in range(1,len(elements_list)):
        picked = elements_list[i]
        j = i-1
        
        while j>=0 and picked < elements_list[j]:
            elements_list[j+1] = elements_list[j]
            j = j-1
        
        elements_list[j+1] = picked
        
    return elements_list

if __name__ == '__main__':
    elements = [21,29,38,17,4,25,11,32,9]
    res = insertion_sort(elements)
    print(res)
