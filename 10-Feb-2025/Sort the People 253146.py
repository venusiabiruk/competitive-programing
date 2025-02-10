# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Step 1: Determine the maximum height to define the range of the counting array
        max_height = max(heights)
        
        # Step 2: Create a counting array to store the index positions of each height
        count = [0] * (max_height + 1)  # +1 because height values start from 1
        for height in heights:
            count[height] += 1
        
        # Step 3: Accumulate the count array to determine the positions of heights in the sorted order
        # The count array now holds the number of elements less than or equal to each height
        for i in range(max_height - 1, -1, -1):
            count[i] += count[i + 1]
        
        # Step 4: Create the output array to store names in sorted order
        sorted_names = ["" for _ in names]
        
        # Step 5: Place names into the sorted_names array based on the heights
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            position = count[height] - 1
            sorted_names[position] = names[i]
            count[height] -= 1
        
        return sorted_names

        