class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build the graph, or we don't need graph at all, we compute next node while traverse starting from beginWord
        words = set(wordList)
        if endWord not in words:
            return 0
        words.discard(beginWord)
        q = deque([(beginWord, 1)])
        characters = "abcdefghijklmnopqrstuvwxyz"
        # traverse the graph: bfs
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in characters:
                    nxt = word[:i] + ch + word[i+1:]
                    if nxt in words:
                        words.remove(nxt)
                        q.append((nxt, length + 1))
        return 0
                
            
        
        # return