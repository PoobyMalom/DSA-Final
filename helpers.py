def insertionSort(nums):
	# Traverse through 1 to len(nums)
    for i in range(1, len(nums)):
        j = i - 1
        # As long as we are in-bounds
        while j >= 0 and nums[j + 1] < nums[j]:
            # nums[j] and nums[j + 1] are out of order so swap them 
            tmp = nums[j + 1]
            nums[j + 1] = nums[j]
            nums[j] = tmp
            j -= 1
    return nums
