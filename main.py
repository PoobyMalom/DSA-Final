from helpers import insertionSort
import random
import time
import matplotlib.pyplot as plt

def block_sort(input_arr, block_size):
    blocks = [] # nested lists to store blocks

    # Break input_arr into blocks
    temp_block = []
    for num in input_arr:
        if len(temp_block) == block_size:
            temp_block = insertionSort(temp_block)
            blocks.append(temp_block)
            temp_block = []
        temp_block.append(num)

    blocks.append(temp_block)

    result = []

    while blocks:
        min_index = 0
        for i in range(1, len(blocks)):
            if blocks[i][0] < blocks[min_index][0]:
                min_index = i

        result.append(blocks[min_index].pop(0))

        if len(blocks[min_index]) == 0:
            blocks.pop(min_index)

    return result
        


test_arr = [3, 2, 1]
print(len(test_arr))
r = block_sort(test_arr, 64)
print(r)
# test_arr = list(range(1, 100000))
# random.shuffle(test_arr)
# r = block_sort(test_arr, 1000)
# print(r)

# def benchmark(min, max, step, num_trials):
#     times = []
#     for i in range(min, max, step):
#         trial_times = 0
#         for j in range(num_trials):
#             test_arr = list(range(1, i))
#             random.shuffle(test_arr)
#             start = time.time()
#             block_sort(test_arr, 64)
#             trial_times += time.time() - start
#         times.append((i, trial_times/num_trials))
#         print(f"Sorting {i} elements done")
#     return times

# b = benchmark(20, 10000, 1, 20)
# print(b)

# # Example array of tuples

# # Split into x and y coordinates
# x, y = zip(*b)

# # Plot
# plt.plot(x, y, marker='o')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Plot from Tuples')
# plt.grid(True)
# plt.show()
