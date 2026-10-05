class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(node, index):

            if index == len(word):
                return node.isEnd
            
            char = word[index]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                
                return False
            
            if char not in node.children:
                return False
            
            return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)
        
