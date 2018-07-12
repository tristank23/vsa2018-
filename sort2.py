import time
import random
total_time = 0


for i in range(100):

    start_time = time.clock()

    list_len = 1000
    list1 = []
    for i in range(list_len):

        list1.append(random.randint(0, 100))

    sorted_list = []

    while len(list1) > 0:

        lowest = min(list1)
        index = list1.index(lowest)
        sorted_list.append(lowest)
        del list1[index]
    total_time += (time.clock() - start_time)
print total_time / 100



