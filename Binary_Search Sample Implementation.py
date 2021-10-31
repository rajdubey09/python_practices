#Sample Binary Search Implementation -->

def binary_search(required_element, elements_list):
    #pass
    #print(required_element, elements_list)

    left = 0
    right = len(elements_list) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        mid_num = elements_list[mid]

        if mid_num == required_element:
            return mid

        elif mid_num < required_element:
            left = mid + 1

        else:
            right = mid - 1

    return "Not Found"


if __name__ == '__main__':
    #print("working")
    #binary_search(9,[1,2,3,4,5])
    print("----------------- Binary Search -----------------")
    req_num = int(input("Enter the Number to Search..."))
    elements_list = [12,23,34,45,56,67,78,89,90]

    idx = binary_search(req_num, elements_list)
    print(f"Required Number {req_num}")
    print(f"Elements List {elements_list}")
    if type(idx) is int:
        print(f"Required Element found at {idx} index and at {idx+1} position using Binary Search.")
    else:
        print(idx)

