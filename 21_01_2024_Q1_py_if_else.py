# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird

if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    elif n%2==0 and 2<=n<=5:
        print("Not Weird")
    elif n%2==0 and 6<=n<=20: 
        print("Weird")
    else:
        print("Not Weird")
