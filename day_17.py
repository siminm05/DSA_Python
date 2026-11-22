'''
day 17 - array questions
Q1. find elements > n/3 times
Q2. LeetCode Question 11 - Container with Most Water
'''

#Given an integer array nums, find all elements that appear more than n/3 times
nums = [1, 2, 3, 3, 2, 2, 3, 2, 1] #9//3 = 3
#nums = [0,0,0,0,0,0,1,1,1,1,1]
ans = []
n = len(nums)//3

for i in range(0, len(nums)):
    count = 0
    if nums[i] not in ans:
        for j in range(0, len(nums)):
            if nums[j] == nums[i]:
                count += 1
        if count > n:
            ans.append(nums[i])
print("Q1. Elements that appear > n/3 times:",ans)


#leetcode Question
'''
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
height = [1,8,6,2,5,4,8,3,7]
ans = 0
G_i = height[0]
#49024602
for i in range(0, len(height)):
    if height[i] > G_i:
        for j in range(0, len(height)):
                width = j-i
                if height[i] < height[j]:
                    w_height = height[i]
                else:
                    w_height = height[j]
                water = width*w_height
                if ans < water:
                    ans = water
                    G_i = height[i]

print("Q2. Container with most water:",ans)
