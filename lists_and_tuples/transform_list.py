def transform(list_one, list_two, r1, r2):
    """ This function allows for transfer between multiple lists while
    rearranging their order. For instance, say that list1 = [1,2,3,4,5,6,7,8,9]
    and you wish to add the numbers in the index range 4:7 of list1 to another
    list, list2, in reverse order while simultaneously removing them from list1. If
    list2 = [100,200], the result will be list2 = [100,200,7,6,5]. Write a
    function named transform that takes as arguments list1, list2, r1, and r2,
    that removes items from list1 in the slice r1:r2, appends them onto list2 in
    reverse order, and returns the resulting list. For example, in this case, the function call
    will be transform(list1, list2, 4,7)."""
    try:
        li = list_one[r1:r2]
        li.reverse()
        list_two.extend(li)
        return print(list_two)
    finally:
        exit()

a=[1,2,3,4,5,6,7,8,9]
b=[100,90]
transform(a,b,4,7)
