# 1. Find the Longest Consecutive Sequence in an Unsorted List
nums = [100, 4, 200, 1, 3, 2, 2]
nums = set(nums)
longest_streak = 0
for num in nums:
    if num - 1 not in nums:
        current_num = num
        current_streak = 1
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
print(longest_streak)

# 2. Calculate Minimum Number of Platforms for Train Scheduling
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
arrivals.sort()
departures.sort()
platforms = max_platforms = 0
i = j = 0
while i < len(arrivals) and j < len(departures):
    if arrivals[i] < departures[j]:
        platforms += 1
        i += 1
        max_platforms = max(max_platforms, platforms)
    else:
        platforms -= 1
        j += 1
print(max_platforms)

# 3. Implement Merge Intervals
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda x: x[0])
merged = []
for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
print(merged)

# 4. Find Kth Smallest Element Using QuickSelect
import random
def quick_select(arr, k):
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k <= len(lows):
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots))
nums = [7, 10, 4, 3, 20, 15]
k = 3
print(quick_select(nums, k))

# 5. Trapping Rain Water Problem
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left, right = 0, len(heights) - 1
left_max = right_max = water = 0
while left < right:
    if heights[left] < heights[right]:
        if heights[left] >= left_max:
            left_max = heights[left]
        else:
            water += left_max - heights[left]
        left += 1
    else:
        if heights[right] >= right_max:
            right_max = heights[right]
        else:
            water += right_max - heights[right]
        right -= 1
print(water)
