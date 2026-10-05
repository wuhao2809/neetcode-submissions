class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        # use a trie, if dot, call the helper
        # within the helper, traverse every children to find all possiblities
        def helper(word_idx, node):
            # base case
            if not node:
                return False

            if word_idx == len(word):
                return node.end
            
            # recursive steps
            curr_char = word[word_idx]
            curr_node = node
            if curr_char in curr_node.children:
                curr_node = curr_node.children[curr_char]
                word_idx += 1
                return helper(word_idx, curr_node)
            elif curr_char == ".":
                for key in curr_node.children:
                    if helper(word_idx + 1, curr_node.children[key]):
                        return True
                return False
            else:
                return False
        return helper(0, self.root)
            
            
            
