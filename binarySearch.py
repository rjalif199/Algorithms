def binaryHelper(lst, order, elt, left, right):

    if left > right:
        return
    elif 0 <= left <= right < len(p):
        if order == "Asc" or "asc":
            lst.sort()
            print(lst)

            mid = (left + right) // 2
            if lst[mid] == elt:
                return mid
            elif lst[mid] < elt:
                return binaryHelper(lst, order, elt, mid + 1, right)
            elif lst[mid] > elt:
                return binaryHelper(lst, order, elt, left, mid - 1)

        elif order == "Desc" or "desc":
            lst.sort(reverse=True)
            print(lst)
            mid = (left + right) // 2
            if lst[mid] == elt:
                return mid
            elif lst[mid] > elt:
                return binaryHelper(lst, order, elt, mid + 1, right)
            elif lst[mid] < elt:
                return binaryHelper(lst, order, elt, left, mid - 1)


def binarySearch(lst, elt, order):
    return binaryHelper(lst, order, elt, 0, len(lst) - 1)


print("Put a ',' between the numbers. \n")
p = list(map(int, input("please input numbers:").split(",")))
ord = str(input("Enter sort order: Asc/Desc :"))
num = int(input("Enter search element\n"))

#def binarySearch(lst,elt,order):

out = binarySearch(p, num, ord)
pos = str(out)
if p[0] == p[-1]:
    if p[0] == num:
        print(str(num) + " is the only number in the list")
    else:
        print("The elemnet doesn't belong to the list.")
elif p[0] != p[-1]:
    print("The number is at index " + pos + " of the list")
else:
    print("The elemnet doesn't belong to the list.")
