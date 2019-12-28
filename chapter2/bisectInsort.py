import bisect
import random

SIZE = 7

random.seed(1729)

''' insort(seq,item) put item into list 'seq', and keep seq ascending'''

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)