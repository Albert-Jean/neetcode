class TrieNode:
    def __init__(self):
        self.word=False
        self.children={}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word=True


    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(index, node):
            # We have processed the entire search word
            if index == len(word):
                return node.word

            c = word[index]

            if c == ".":
                # Try matching '.' with every possible letter
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            # Normal character lookup
            if c not in node.children:
                return False

            return dfs(index + 1, node.children[c])
        return dfs(0, self.root)
            
