# Author: Nishanth Amuluru

# Logic: Since all we want is only the first 10
# digits, we don't have to consider all the 
# digits in each number. 11-12 digits should do

# Assuming the numbers are in a file nums.txt
nums = [int(l[:12]) for l in open("nums.txt")]
print str(sum(nums))[:10]
