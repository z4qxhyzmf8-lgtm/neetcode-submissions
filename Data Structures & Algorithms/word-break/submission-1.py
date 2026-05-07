class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class pref_tree:
    def __init__(self):
        self.root = TrieNode()
        self.depth = 0
    
    def add(self, word: str) -> None:
        node = self.root
        level = 0
        for char in word:
            level += 1
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
        self.depth = max(self.depth, level)

    def search(self, word: str, i: int , j: int) -> bool:
        node = self.root
        for k in range(i, j + 1):
            if word[k] not in node.children:
                return False
            node = node.children[word[k]]
        return node.end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we add all dictionary words in the trie
        trie = pref_tree()
        for word in wordDict:
            trie.add(word)
        
        #dp[i] = 1 iff s[i:] comes from words in dict
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        
        for i in range(n, -1, -1):
            for j in range(i, min(n, i + trie.depth)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        if dp[0]:
            return True
        return False
        












        