#1
def max_value(integer):
    for x in range(1,integer+1):
        print x
print range(1,8)

#2
list1 = [4,5,15,11,23,42]
list2 = [1,8,7,16,7,35]

def compare_lists(list1,list2):
    for x in list1:
        if x >list2[list1.index(x)]:
            print x
        else:
            print list2[list1.index(x)]

# 3
def swapping_stars():
    for y in range(1,7):
        something = ""
        for x in range(1, 7):
            if (x + y) % 2 == 0:
                something = something + "* "
            else:
                something = something + "- "
        print something
swapping_stars()
