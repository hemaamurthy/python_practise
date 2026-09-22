#Write a function average(*nums) that returns the average of any amount of numbers passed to it.
def average(*nums):
    return (sum(nums)/len(nums))
avg = average(89,77,56,89)
print(avg)