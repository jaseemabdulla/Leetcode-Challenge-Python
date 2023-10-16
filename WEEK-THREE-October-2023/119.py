# Pascal's Triangle 

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly


class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
    
        current_row = [1]
    
        for i in range(1, rowIndex + 1):
            next_row = [1]
            for j in range(1, len(current_row)):
                next_element = current_row[j - 1] + current_row[j]
                next_row.append(next_element)
            next_row.append(1)
            current_row = next_row
        
        return current_row