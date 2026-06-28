import os
import shutil


topics = {

    # Basic Data Structures
    "array": "Array",
    "matrix": "Matrix",
    "string": "String",

    "linked-list": "Linked List",
    "linked": "Linked List",

    "stack": "Stack",
    "queue": "Queue",
    "deque": "Deque",

    "hash": "Hash Table",
    "map": "Hash Table",

    "heap": "Heap",
    "priority-queue": "Heap",

    "trie": "Trie",

    # Searching
    "binary-search": "Binary Search",
    "search": "Searching",

    # Sorting
    "sort": "Sorting",
    "sorting": "Sorting",

    # Two pointers / Sliding window
    "two-pointer": "Two Pointers",
    "two-sum": "Two Pointers",

    "sliding-window": "Sliding Window",

    "prefix-sum": "Prefix Sum",

    # Recursion / Backtracking
    "recursion": "Recursion",
    "recursive": "Recursion",

    "backtracking": "Backtracking",
    "permutation": "Backtracking",
    "combination": "Backtracking",
    "subset": "Backtracking",

    # Trees
    "tree": "Trees",
    "binary-tree": "Trees",
    "bst": "Binary Search Tree",
    "binary-search-tree": "Binary Search Tree",

    # Graphs
    "graph": "Graphs",
    "bfs": "Graphs",
    "dfs": "Graphs",
    "topological": "Graphs",
    "shortest-path": "Graphs",

    # Dynamic Programming
    "dynamic-programming": "Dynamic Programming",
    "dp": "Dynamic Programming",
    "memoization": "Dynamic Programming",
    "tabulation": "Dynamic Programming",

    # Greedy
    "greedy": "Greedy",

    # Math
    "math": "Math",
    "mathematical": "Math",
    "number": "Math",
    "prime": "Math",
    "gcd": "Math",
    "lcm": "Math",
    "modulo": "Math",

    # Bit manipulation
    "bit": "Bit Manipulation",
    "xor": "Bit Manipulation",

    # Common patterns
    "palindrome": "String",
    "anagram": "String",
    "substring": "String",
    "subsequence": "String",

    "interval": "Intervals",

    "simulation": "Simulation",

    # Advanced topics
    "union-find": "Disjoint Set Union",
    "disjoint": "Disjoint Set Union",

    "segment-tree": "Segment Tree",

    "fenwick": "Fenwick Tree",

    "divide": "Divide and Conquer",

    "geometry": "Geometry",

    # Fallback
}


def detect_topic(folder):

    name = folder.lower()

    for keyword, topic in topics.items():
        if keyword in name:
            return topic

    return "Others"



for item in os.listdir():

    if os.path.isdir(item) and item[0].isdigit():

        topic = detect_topic(item)

        destination = os.path.join(
            "Topics",
            topic,
            item
        )

        if not os.path.exists(destination):

            os.makedirs(
                os.path.dirname(destination),
                exist_ok=True
            )

            shutil.move(
                item,
                destination
            )

            print(
                f"Added {item} -> {topic}"
            )
