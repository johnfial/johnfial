# help: https://www.youtube.com/watch?v=zIjfhVPRZCg
# pronounced 'try'

# NOTE optimize:
# store state information by either 
# A) keeping current state within the trie
# B) returning a reference to the node to the caller, then taking that in each time, default=root


class Trie():
    class Node():
        def __init__(self, data):
            self.data = data
            self.is_complete_word = False
            self.children = {
                # 'character': node,
            }

    def __init__(self, init_data):
        for character in init_data:
            self.Node(character)
        self.data = None

    def __repr__(self) -> str:
        return str(self.data)

trie1 = Trie(['a', 't', 'o', 'm',])
print(trie1)

