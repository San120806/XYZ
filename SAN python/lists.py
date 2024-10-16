#Write a Python program to remove duplicates from a list.
def remove_duplicates(maxy):
    return list(set(maxy))


da_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(da_list))

#Write a Python function that takes two lists and returns True if they have at least one common member.
def common_num(list1, list2):
    return bool(set(list1) & set(list2))


m = [1, 2, 3]
n = [3, 4, 5]
print(common_num(m,n))