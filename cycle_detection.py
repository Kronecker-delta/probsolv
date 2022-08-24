

def floyd1(nums):
    """
The general strategy is as follows,
If we see the array as a function from a finite set [0,n] to [1,n],
and define x_{k+1} = f(x_{k}) then the problem is of cycle detection, 
that is finding smallest i such that for some v we have x_{i} = x_{i+v}.  
Note that for any j>= i x_{j} = x_{j+ku} for some smallest period u and 
any integer k. Now if it so happens that x_{j} = x_{2j} then it must be 
the case 2j = j = j+ku and so j = ku. Conversely if j = ku for some j>=i 
then 2j = j+ku. Now it must be the case that for some sufficiently large 
k, ku >= i and so there must exist a j >= i such that j = 2j (mod u). The 
algorithm first finds this j, but this j is also some multiple of the 
smallest period. Once we know the period we run through each term of the 
sequence from the beginning looking for the first value k for which 
x_{k} = x_{k+j} for we must have k = j.
    """
    slow, fast = 0,0
    period = 0
    check = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        period += 1
        if slow == fast:
            break
    while True:
        val = check
        for count in range(period):
            val = nums[val]
        
        if val == check:
            return val
        check = nums[check]


def floyd2(nums):
    """
    This improvement relies on the fact that the number steps needed 
    to get back to i from j is just i.
    """
    slow,fast = 0,0
    period,start = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            while start != fast:
                start = nums[start]
                fast = nums[fast]
            
            return start

