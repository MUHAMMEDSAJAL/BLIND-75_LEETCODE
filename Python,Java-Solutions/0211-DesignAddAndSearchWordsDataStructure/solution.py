class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False

        def backtrack(self, word: str, i: int) -> bool:
            c = word[i]
            if i == len(word) - 1:
                return c == '.' and any(child.end for child in self.children.values()) \
                    or c in self.children and self.children[c].end
            elif c == '.':
                return any(child.backtrack(word, i + 1) for child in self.children.values())
            elif c in self.children:
                child = self.children[c]
                return child.backtrack(word, i + 1)
            else:
                return False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for i in range(len(word) - 1):
            c = word[i]
            if c not in ptr.children:
                ptr.children[c] = self.TrieNode()
            ptr = ptr.children[c]
        c = word[-1]
        if c not in ptr.children:
            ptr.children[c] = self.TrieNode()
        ptr.children[c].end = True

    def search(self, word: str) -> bool:
        return self.root.backtrack(word, 0)


if __name__ == "__main__":
    s = Solution()

