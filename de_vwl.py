list = ['a', 'e', 'i', 'o', 'u']
def d_vwl(some_string):
    for n in some_string:
        if n in list:
            some_string = some_string.replace(n,"")
    print some_string
d_vwl("Hello")
