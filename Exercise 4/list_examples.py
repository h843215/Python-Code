import random

"""
This program consists of few simple functions which demonstrate operations on lists.

[!] marks places which need taking care of (either changing or adding new code).

A correct result of this program is in file 'list_examples_out.txt' 
"""

def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False # All numbers are odd  [!]
                # Change this function so that it still has only one line of code
   
#
# Functions below count something on lists
#

def sum_1(lst):
    """
    Sums elements of the list
    """
    
    result = 0
    for elem in lst:
        result += elem
        
    return result
   
def sum_2(lst): #[!]
    """
    Sums elements of the list, uses indices. There is a small mistake in 
    this function
    
    points: 0.5
    """
    
    result = 0
    for i in range(len(lst)):
        result += lst[i]
        
    return result
   
def sum_even(lst): #[!]
    """
    Sums even numbers from the list. There is a small mistake in this 
    function. You should use function is_even
    
    points: 0.5
    """

    
    result = 0
    for elem in lst:
        if is_even(elem):
            result += elem
        
    return result
   
#
# Functions below do something with lists, but do not modify them
#

def add_spaces(n,k):
    """
    If number 'n' has less than 'k' characters, the function adds spaces
    to the end until the string has 'k' characters 
    
    points: 0.5
    """
    
    s = str(n)
    while len(s) < k: #[!]
        s += " "
    return s  

def histogram(lst):
    """
    returns a string representing a vertical histogram for the given list,
    where both the frequency and label are the number at the list index.
    There should be a space between the label (number) and stars representing
    frequency. The stars should start in the fourth column. 

    For example:

    Given the list [1, 1, 2, 10, 3] should generate:

    1  *
    1  *
    2  **
    10 **********
    3  ***

    Hint: use function add_spaces
    points: 0.5
    """

    h = ""
    for nr in lst:
        h += add_spaces(nr,3)
        h += ("*" * nr + "\n") #[!]    
    return h

#
# Functions below modify the argument lists
#

def increase_all(lst):
    """
    Increases by 1 all the elements of the list. It does not return anything

    points: 0.5
    """

    for i in range(len(lst)):
        lst[i] += 1

   

def normalize_list(lst):
    """
    Subtracts from every element from the list the average of all the
    elements from the list

    points: 1
    """
    a = sum(lst)/len(lst)
    for i in range(len(lst)):
        lst[i] -= a
        
    
    # hmmm... not always [!]
    # you have to still modify the lst [!]


def reverse_list(lst):
    """
    Reverses the order of a list.  Doesn't return anything

    points: 1
    """
    
    for i in range(int(len(lst)/2)):
        temp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = temp
    

def reverse_sentence(sentence):
    """
    Reverses the words in a sentence.  Returns the reversed sentence.
    Assume there's a space between all words

    points: 1
    """
    # first is -1 that means start from last element 
    # second argument is empty that means move to end of list 
    # third arguments is difference of steps
    words = sentence.split(" ")
    words = words[-1::-1]
    return " ".join(words) # [!]

###################################################################################
# The code starts here, you do not have to change anything below
###################################################################################
if __name__ == '__main__':
    
    lst = [1,2,3,4,5]

    print("For list " + str(lst) + " sum of the elements is:")
    print("sum_1 = ", sum_1(lst))
    print("sum_2 = ", sum_2(lst))
    print("If we sum only even numbers we will get:")
    print("sum_even = ", sum_even(lst))
    print()         

    H = [1,2,3,4,5,6,7,4,8,4,8,2,2,1,10]
    print("Histogram for list " + str(H))
    print(histogram(H))
    print()         

    print("Let's start with list " + str(lst) + " and increase it 4 times")

    increase_all(lst)
    print(lst)
    increase_all(lst)
    print(lst)
    increase_all(lst)
    print(lst)
    increase_all(lst)
    print(lst)
    print()


    lst = [1,2,3,4,5]
    print("Let's start with " + str(lst) + " and normalize it three times")

    normalize_list(lst)
    print(lst)
    normalize_list(lst)
    print(lst)
    normalize_list(lst)
    print(lst)

    print("\nWhy it is always the same?")

    print("Oh, it's because the list's sum is now %d" % sum_2(lst))

    sent = "I do not like them Sam I am"
    print("\nForwards:")
    print(sent)
    print("Backwards:")
    print(reverse_sentence(sent))
