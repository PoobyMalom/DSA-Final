from helpers import insertionSort
import random

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
    temp_block.sort()
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
        


test_arr = list(range(1, 100000))
random.shuffle(test_arr)
r = block_sort(test_arr, 1000)
print(r)