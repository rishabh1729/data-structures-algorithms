class Node:
    def __init__(self, value, isWord = False) -> None:
        self.value = value
        self.characters = {}
        self.isWord = isWord

class Trie:
    def __init__(self) -> None:
        self.root = Node('')

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.characters:
                current.characters[ch] = Node(ch)
            current = current.characters.get(ch)
        current.isWord = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.characters:
                return False
            current = current.characters.get(ch)
        return current.isWord
    
    def startsWith(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.characters:
                return False
            current = current.characters.get(ch)
        return True

trie = Trie()
print("Inserting word 'apple'")
trie.insert('apple')
print("Word 'app' found: ", trie.search('app'))
print("Word 'apple' found: ", trie.search('apple'))
print("Prefix 'app' found: ", trie.startsWith('app'))
print("Inserting word 'app'")
trie.insert('app')
print("Word 'app' found: ", trie.search('app'))