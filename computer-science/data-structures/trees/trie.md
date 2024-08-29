## Trie

Trie is a type of k-ary search tree used for storing and searching a specific key from a set. It is a multi-way tree data structure used for storing strings over an alphabet. It is used to store a large amount of strings. Use cases include autocomplete and spellchecker.

Unlike a binary search tree, nodes in the trie do not store their associated key. Instead, a node's position in the trie defines the key with which it is associated. This distributes the value of each key across the data structure, and means that not every node necessarily has an associated value.

**All the children of a node have a common prefix** of the string associated with that parent node, and the root is associated with the empty string. This task of storing data accessible by its prefix can be accomplished in a memory-optimized way by employing a **radix tree**.

If we store keys in a BST, a well-balanced BST will ned O(M \* logN), where M is the maximum string length and N is the number of keys in the tree. With Trie, the key can be searched in **O(M)** time.

<img src="../../assets/tries.png">

### Strengths

- If you are storing many words that start with similar patterns, Tries may reduce the overall storage cost and hence, can be space-efficient
- Tries can quickly answer queries about words with shared prefixes i.e. how many words start with "choco"

### Structure

Every node of Trie consists of multiple branches. Each branch represents a possible character of keys. Mark the last node of every key as the end of the word node with isEndOfWord field.

```java
class TrieNode {
    boolean isWord;
    Map<Character, TrieNode> children;
    TrieNode() {
        this.children = new HashMap<>();
    }
}
```

## Example

```py
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            node = node.addLetter(word[i])
            if i == len(word) - 1:
                node.complete()

    def search(self, word: str) -> bool:
        node = self.root
        for x in word:
            node = node.findLetter(x)
            if node is None: return False
        return node.wordExists()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            node = node.findLetter(x)
            if node is None: return False
        return True

class Node:
    def __init__(self):
        # key maps to either another node or an arbitrary value
        # arbitrary value refers to a complete word
        # all children of a node have a common prefix i.e. ancestor
        self.children = {}
        self.isComplete = False

    def complete(self):
        self.isComplete = True

    def wordExists(self):
        return self.isComplete

    def addLetter(self, v):
        if v not in self.children: self.children[v] = Node()
        return self.children[v]

    def findLetter(self, v):
        if v not in self.children: return None
        return self.children[v]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
