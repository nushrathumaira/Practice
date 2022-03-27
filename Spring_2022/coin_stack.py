import sys
from collections import deque


def posi(lst):
    return [x for x in lst if x > 0] or None
    
def main():
    n = sys.stdin.readline()
    #print(n)
    numbers = sys.stdin.readline().split(" ")
    int_numbers = [int(i) for i in numbers]

    """
    #one solution
    totalSum = 0
    totalCount = 0
    yes = True
    no = False
    #print(max(int_numbers))
    #print(min(int_numbers))
    for i in int_numbers:
        totalSum += i
        totalCount = totalSum
    #print(totalSum)
    while(totalCount !=0 and no != True):
        maxVal = max(int_numbers)
        maxIndex = int_numbers.index(maxVal)
        minVal = min(int_numbers)
        minIndex = int_numbers.index(minVal)
        #print( " min {} min {} max {} max {}".format(minVal,minIndex, maxVal, maxIndex))
        if totalSum % 2 == 0 and yes == True:
            print("yes")
            print(str(minVal) + " " + str(maxIndex))
            yes = False
        elif totalSum % 2 == 0:
            print(str(minVal)+str(1)+" "+str(maxIndex+1))
        else:
            no = True
            print("no")
        totalCount = totalCount - 2
      """
    sum_list = sum(int_numbers)
    #print(sum_list)
    if sum_list %2 != 0:
        print("no")
    ans_strings = []
    while(sum(int_numbers) > 0):
        max_in = int_numbers.index(max(int_numbers))
        #print(posi(int_numbers))
        min_positive_value = min(posi(int_numbers))
        #print("min_positive {}".format(min_positive_value))
        reversed_list = int_numbers[::-1]

        first_index_in_reversed = reversed_list.index(min_positive_value)
        first_index = int_numbers.index(min_positive_value)
        #print(first_index_in_reversed)
        last_index = len(int_numbers) -1 - first_index_in_reversed
        min_in = len(int_numbers) - int_numbers[-1::-1].index(min_positive_value)- 1
        #min_in = len(int_numbers) -1 - first_index
        #print(" max in {} min in {}".format(max_in, min_in))
        if(max_in == min_in):
            print("no")
        else:
            ans_strings.append(str(min_in+1)+" "+str(max_in+1))
            int_numbers[max_in] -= 1
            int_numbers[min_in] -= 1
            
    print("yes")
    for s in ans_strings:
        print(s)
        print("\n")
        
        
        
        
         

if __name__ == "__main__":
    main()