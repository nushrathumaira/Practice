# kadane's maximum subarray problem
## from wiki (https://en.wikipedia.org/wiki/Maximum_subarray_problem)
def kadane(a):
    max_ending_here = max_so_far = a[0]
    for i in a[1:]:
        max_ending_here = max(i, max_ending_here+i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    
 
# first input is N, number of commercial breaks    
p = int(input().split()[1]) #price of one commercial break
#ith value in list indicates how many students listening to ith commercial break
# at most 2000 students listening
# transform each input by -p
price_list = list(map(lambda x: int(x)-p, input().split()))  
print(kadane(price_list))  

