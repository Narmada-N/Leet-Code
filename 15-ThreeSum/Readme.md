
# 3Sum Problem

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1

- **Input:** 
  - `nums = [-1, 0, 1, 2, -1, -4]`
- **Output:** 
  - `[[-1,-1,2],[-1,0,1]]`
- **Explanation:** 
  - The valid triplets are `[-1, 0, 1]` and `[-1, -1, 2]`. 
  - Notice that the order of the output and the order of the triplets does not matter.

### Example 2

- **Input:** 
  - `nums = [0, 1, 1]`
- **Output:** 
  - `[]`
- **Explanation:** 
  - There is no possible triplet that sums up to 0.

### Example 3

- **Input:** 
  - `nums = [0, 0, 0]`
- **Output:** 
  - `[[0, 0, 0]]`
- **Explanation:** 
  - The only possible triplet sums up to 0.

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`