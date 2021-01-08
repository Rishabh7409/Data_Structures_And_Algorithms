# In Linear Search We Search Element In The Array By Comapring The Key Element with Elements of array until we found it

def Linear_search(element,array):

    for index,x in enumerate(array):
        if x==element:
            return index
    
    return -1

if __name__ == "__main__":
    arr=[5,4,3,6,7,1,8,9,5,4]
    element=4

    ind=Linear_search(element,arr)
    if ind!=-1:
        print(f"Element Is At {ind} Index")
    else:
        print("Element not Found")