class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        okx, oky, okz = False, False, False
        useful = []
        for triple in triplets:
            a, b, c = triple
            if a <= x and b <= y and c <= z:
                useful.append([a, b, c])
                if a == x:
                    okx = True
                if b == y:
                    oky = True
                if c == z:
                    okz = True

        if useful and okx and oky and okz:
            return True
        return False
        