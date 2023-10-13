# Problem 1: Flatten Nested List Iterator (https://leetcode.com/problems/flatten-nested-list-iterator/)
# // Time Complexity : next = O(1), hasNext --> O(1)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.li = []
        self.i = 0
        self.dfs(nestedList)

    def dfs(self, nestedList):
        for ele in nestedList:
            if ele.isInteger():
                self.li.append(ele.getInteger())
            else:
                self.dfs(ele.getList())

    def next(self) -> int:
        re = self.li[self.i]
        self.i += 1
        return re

    def hasNext(self) -> bool:
        if (self.i == len(self.li)):
            return False
        return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
