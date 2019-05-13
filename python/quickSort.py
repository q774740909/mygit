def quickSort(my_list, left, right):
    if left >= right:
        return
    else:
        base = left
        originleft = left
        originright = right
        while left < right:
            while my_list[right] >= my_list[base] and left < right:
                right -= 1
            while my_list[left] <= my_list[base] and left < right:
                left += 1
            my_list[left], my_list[right] = my_list[right], my_list[left]
        my_list[base], my_list[left] = my_list[left], my_list[base]
    quickSort(my_list, originleft , left - 1)
    quickSort(my_list, right + 1, originright)
    return my_list


my_list = [7,8,5,4,6,1,3,2,9,9,7]
print(my_list)
plist = quickSort(my_list, 0, len(my_list) - 1)
print('after sorting:{}'.format(plist))
