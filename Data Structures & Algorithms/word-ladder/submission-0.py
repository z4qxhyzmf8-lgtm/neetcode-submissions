class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nbs = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '@' + word[j + 1:]
                nbs[pattern].append(word)
        
        level = 1
        q = deque()
        vis = set()
        q.append(beginWord)
        vis.add(beginWord)
        while q:
            k = len(q)
            for i in range(k):
                word = q.popleft()
                if word == endWord:
                    return level
                for j in range(len(word)):
                    pattern = word[:j] + '@' + word[j + 1:]
                    for nb in nbs[pattern]:
                        if nb not in vis:
                            q.append(nb)
                            vis.add(nb)
            level += 1
        return 0

        