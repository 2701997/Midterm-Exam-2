"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here
def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:]) 



def main():
    # Test your function here
    print(getSum([1, 3, 4, 2, 5]))


if __name__ == "__main__":
    main()
