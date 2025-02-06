# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

from random import randint

class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.list_elements = []

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.index_map[val] = len(self.list_elements)
            self.list_elements.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            remove_index = self.index_map[val]
            last_element = self.list_elements[-1]
            self.list_elements[remove_index] = last_element
            self.index_map[last_element] = remove_index
            self.list_elements.pop()
            del self.index_map[val]
            return True
        return False

    def getRandom(self) -> int:
        random_index = randint(0, len(self.list_elements) - 1)
        return self.list_elements[random_index]
