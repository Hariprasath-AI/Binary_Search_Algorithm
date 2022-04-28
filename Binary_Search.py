# Insertion Sort:
# No Temporary array/list used. Swapping ocurrs within the original array/list. 
def Insertion_Sort(arr):
    # Initializing start value with 1. In this Insertion sort, Unsorted Array index starts with 1.
    # Start value indicates the starting index of unsorted array.
    start = 1
    
    # This for loop is to loop the unsorted array till the end.
    for i in range(start, len(arr)):
        # For every value in unsorted array is compared with the sorted array to fix the position. 
        # And the current checking value in unsorted array is stored in the variable 'val'. 
        val = arr[i]
        
        # Each unsorted array value is compared with sorted array in reverse order starts form i - 1 th position till 0th position.
        for j in range(start - 1, -1, -1):
            
            # If value in sorted array not greater than i'th value(val) means that there is no need to change in the sorted array. Then the loop will break.
            if arr[j] <= val:
                break

            # If greater the value will be jumped to the next index to fix the position. 
            if j >= 0 and arr[j] > val:
                arr[j + 1] = arr[j]
                # After jumping the value from their position we have to clear the value from their original position to avoid incorrect output.
                arr[j] = None
            else:
                break

        # At the end of one check there is possible that 'None' at j'th position or j + 1'th position.
        # Scenario of 'None' at j'th position only occurs when the comparing value comes at the 1st element of the array.
        # Rest of the scenarios j + 1 th position have 'None', 'val' is assigned for that position. 
        if arr[j + 1] == None:
            arr[j + 1] = val
        if arr[j] == None:
            arr[j] = val

        # Increment start value by 1 to move forward one by one value.
        start += 1

    # * before variable 'arr' used to pint the list elements without bracket and commas. 
    return arr

def Binary_Search(lst, to_Find):
    # Before Going into Binary Search Algorithm, we have to sort the given array.
    # Here we have used Insertion Sorting method.
    lst = Insertion_Sort(lst)

    # Binary Search searches the elements in the list only if the 'if' condition satisfies.
    # If not satisfies the condition 'else' part will be executed.
    if to_Find <= lst[-1] and to_Find >= lst[0]:

        # Initialize start value as 0, end value as length of list - 1,
        # start - starting index of array,
        # end - ending index of array,
        # By adding start and end value, we can get mid_loc(middle_location).
        start = 0
        end = len(lst) - 1
        mid_loc = (start + end) // 2

        # Initialize found value as True.
        found = True

        # While loop runs until we found the position of the element/integer.
        while found:
            # If we found the element, loop gets stopped by reinitializing found value as 'False'.
            if to_Find == lst[mid_loc]:
                print(to_Find, "found at Position of", mid_loc + 1)
                found = False

            # If our finding value is greater than updated mid_loc, 'start' value will be re-initialized to start search from updated mid_loc + 1 index. 
            # And mid_loc value is updated again by using mid_loc formula.
            elif to_Find > lst[mid_loc]:
                start = mid_loc + 1
                mid_loc = (start + end) // 2
                found = True

            # If our finding value is lesser than updated mid_loc, 'end' value will be re-initialized to end the search till updated mid_loc - 1 index. 
            # And mid_loc value is updated again by using mid_loc formula.
            # 'found' reamins 'True' because we din't find exact postion.    
            elif to_Find < lst[mid_loc]:
                end = mid_loc - 1
                mid_loc = (start + end) // 2
                found = True
    else:
        print(to_Find,"not found")
    
    
if __name__ == "__main__":
    # At first line, get number of integers seperated by spaces
    lst = list(map(int, input().split()))

    # At second line, get the number we want to search
    to_Find = int(input())

    # That's all, call the function and pass two arguments('lst' and 'to_Find')
    Binary_Search(lst, to_Find)


