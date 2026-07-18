class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur[:])
                return

            # Out of bounds or exceeded target
            if i >= len(candidates) or total > target:
                return

            # Choose current number
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])   # Stay at same index

            # Undo choice
            cur.pop()

            # Skip current number
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res