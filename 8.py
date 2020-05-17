# Өгөгдсөн тоон дарааллыг буурахаар эрэмбэл.
nums = [int(x) for x in input().split()]
nums.sort()
nums.reverse()
print(nums)
print(sorted(nums, reverse=True))