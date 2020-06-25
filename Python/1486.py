from functools import reduce

def xorOperation(n, start):
    nums = []
    for i in range(n):
        nums.append(start + 2*i)
    return(reduce(lambda x,y: x ^ y, nums))

if __name__ == "__main__":
    n = 10
    start = 5
    print(xorOperation(n, start))
