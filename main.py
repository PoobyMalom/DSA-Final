def block_sort(input_arr, block_size):
    blocks = [] # nested lists to store blocks

    # Break input_arr into blocks
    temp_block = []
    for num in input_arr:
        if len(temp_block) == block_size:
            temp_block.sort()
            blocks.append(temp_block)
            temp_block = []
        temp_block.append(num)
    temp_block.sort()
    blocks.append(temp_block)


test_arr = [3,5,6,3,2,1,5,6]
block_sort(test_arr, 3)