def replaceElements(nums):
    # Initialize the maximum value seen so far to -1 
    # (as the rightmost element must be replaced by -1)
    max_so_far = -1
    
    # Iterate backwards through the array
    for i in range(len(nums) - 1, -1, -1):
        # Store the current element temporarily
        current_val = nums[i]
        
        # Replace the current element with the largest value seen to its right
        nums[i] = max_so_far
        
        # Update the maximum value seen so far
        # Python's built-in max() function can be used to compare the two values
        max_so_far = max(max_so_far, current_val)
        
    return nums

# Test Cases
print(replaceElements([11-13]))          # Output: [3, 3, -1]
print(replaceElements([11, 12, 14-16]))   # Output: [9, 9, 9, 9, -1]