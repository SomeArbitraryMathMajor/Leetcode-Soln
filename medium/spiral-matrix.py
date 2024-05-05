class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recursive(matrix):
            if not matrix:
                return []
            head = matrix[0]
            if not head:
                return []
            if len(matrix) == 1:
                return head
            if len(head) == 1:
                return sum(matrix,[])
            tail = matrix[-1][::-1]
            if len(matrix) == 2:
                return head+tail
            cut = matrix[1:-1]
            right = [sublist[-1] for sublist in cut]
            left = [sublist[0] for sublist in cut][::-1]
            submat = [sublist[1:-1] for sublist in cut]
            return head + right + tail + left + recursive(submat)
        return recursive(matrix)
