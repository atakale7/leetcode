import random

def findNumbers(nums):
    evens = 0
    for num in range(len(nums)):
        if len(str(nums[num])) % 2 == 0:
            evens += 1
    return evens

if __name__ == "__main__":
    num = random.randint(1,500)
    nums = []
    for i in range(num):
        nums.append(random.randint(1,100000))
    print(findNumbers(nums))
