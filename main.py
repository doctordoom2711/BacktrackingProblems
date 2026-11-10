def subset_sum(numbers, target):
    def backtrack(index, current_sum):
        if current_sum == target:
            return True
        if current_sum > target or index == len(numbers):
            return False
        
        if backtrack(index + 1, current_sum + numbers[index]):
            return True
            
        if backtrack(index + 1, current_sum):
            return True
            
        return False

    return backtrack(0, 0)

nums = (3, 34, 4, 12, 5, 2)
target_value = 9

print(subset_sum(nums, target_value))
