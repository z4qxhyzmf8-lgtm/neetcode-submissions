class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.index = -1 #index of word in dictionary if word end here, -1 otherwise
        self.refs = 0 #nbr of words in dictionary through this node

class pref_tree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, i):
        node = self.root
        node.refs += 1
        for char in word:
            ind = ord(char) - ord('a')
            if not node.children[ind]:
                node.children[ind] = TrieNode()
            node = node.children[ind]
            node.refs += 1
        node.index = i
    
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = pref_tree()
        for i in range(len(words)):
            trie.add(words[i], i)
        
        sol = []
        n = len(board) #nr of rows
        m = len(board[0]) #nr of cols

        def back(i, j, node):
            nonlocal trie
            nonlocal sol
            nonlocal n
            nonlocal m
            
            #out of bounds
            if i < 0 or j < 0 or i >= n or j >= m:
                return

            #visited node alread
            char = board[i][j]
            if char == '#':
                return

            #node has no children 
            index = ord(char) - ord('a')
            if not node.children[index]:
                return
            
            #move to child
            prev = node
            node = node.children[index]
            board[i][j] = '#'
            
            #if i'm at the end of a word we add it to sol
            if node.index != -1:
                sol.append(words[node.index])
                node.index = -1
                node.refs -= 1

                #if there are no more words through this node we cut it out 
                if not node.refs:
                    prev.children[index] = None
                    node = None
                    board[i][j] = char
                    return
            
            #move to all possible states
            back(i + 1, j, node)
            back(i - 1, j, node)
            back(i, j - 1, node)
            back(i, j + 1, node)

            #restore board
            board[i][j] = char
            
        for i in range(n):
            for j in range(m):
                back(i, j, trie.root)
        return sol
        