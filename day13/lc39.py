class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(index, target, path):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break

                path.append(candidates[i])       
                dfs(i, target - candidates[i], path)
                path.pop()                       

        dfs(0, target, [])

        return res 