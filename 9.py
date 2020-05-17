# Тоон дарааллын хамгийн их болон багын байрыг соль.
nums = [int(x) for x in input().split()]
max_ = max(nums)
min_ = min(nums)
index_max = nums.index(max_)
index_min = nums.index(min_)
nums[index_max]=min_
nums[index_min]=max_
print(nums)