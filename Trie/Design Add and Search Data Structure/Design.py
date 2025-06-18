class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for chars in cur.children.values():
                        if dfs(i + 1, chars):
                            return True
                    return False   
                elif char not in cur.children:
                    return False
                cur = cur.children[char]

            return cur.isWord == True

        return dfs(0,self.root)

