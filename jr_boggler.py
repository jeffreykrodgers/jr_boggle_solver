import sys

class Trie:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 26
        self.isWord = False
        if parent is not None:
            parent.children[ord(value) - 97] = self


def make_trie(dictionary_file):
    dictionary = open(dictionary_file)
    root = Trie(None, '')

    for word in dictionary:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.children[ord(letter) - 97]
                if nextNode is None:
                    nextNode = Trie(curNode, letter)
                curNode = nextNode
        curNode.isWord = True
    return root


def filter_puzzle(puzzle):
    new_puzzle = []

    for i in puzzle:
        if i is not '':
            new_puzzle.append(i)
    return new_puzzle


def solve(puzzle):
    dictionary = make_trie('dictionary.txt')
    puzzle = filter_puzzle(puzzle.lower().splitlines())
    numrows = len(puzzle)
    numcols = len(puzzle[0])
    queue = []
    words = []

    for y in range(numcols):
        for x in range(numrows):
            hit = set()
            letter = puzzle[x][y]
            node = dictionary.children[ord(letter) - 97]

            hit.add((x,y))
            queue.append((x, y, letter, node, hit))

    while queue:
        x, y, combo, node, hit = queue[0]
        word_length = len(combo)

        del queue[0]
        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)):

            x2, y2 = x + dx, y + dy
            if 0 <= x2 < numrows and 0 <= y2 < numcols and (x2,y2) not in hit:
                    combo2 = combo + puzzle[x2][y2]
                    node2 = node.children[ord(puzzle[x2][y2]) - 97]
                    h2 = set()
                    h2.update(hit)
                    if node2 is not None:
                        if node2.isWord and word_length >= 2 and combo2 not in words:
                            words.append(combo2)
                        h2.add((x2,y2))
                        queue.append((x2, y2, combo2, node2, h2))

    return sorted(words)


if __name__ == '__main__':

    rows = sys.stdin.read()
    solution = (solve(rows))


    for word in solution:
        sys.stdout.write(word + "\n")
