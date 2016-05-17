text_input = raw_input('Type Your Text Here:').lower().split()
something = {}
for x in text_input:
    something[x] = something.pop(x, 0) + 1
print something
#Add replace!
