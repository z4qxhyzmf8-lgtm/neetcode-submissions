class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def f(e: List[int]) -> int:
            return e[0]
        n = len(position)
        v = [[position[i], speed[i]] for i in range(n)]
        v.sort(reverse = True, key = f)
        stack = []
        ans = 1
        for i in range(n):
            t = (target - v[i][0]) / v[i][1]
            if stack and t > stack[-1]:
                while stack:
                    stack.pop()
                ans += 1
            if stack and t < stack[-1]:
                continue
            stack.append(t)
        return ans


        

        

        
        

        