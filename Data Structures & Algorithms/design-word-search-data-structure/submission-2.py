class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        n = len(word)
        def back(node, i):
            nonlocal n
            curr = node
            for j in range(i, n):
                char = word[j]
                if char == '.':
                    for child in curr.children.values():
                        if back(child, j + 1):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end
        return back(self.root, 0)
            

           


