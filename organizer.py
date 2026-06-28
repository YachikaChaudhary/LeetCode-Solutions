import os
import shutil


topics = {
    "array": "Array",
    "two-sum": "Array",

    "hash": "Hash Table",

    "binary-search": "Binary Search",

    "linked-list": "Linked List",
    "linked": "Linked List",

    "stack": "Stack",
    "queue": "Queue",

    "tree": "Trees",
    "binary-tree": "Trees",

    "graph": "Graphs",

    "dynamic-programming": "Dynamic Programming",
    "dynamic": "Dynamic Programming",
    "dp": "Dynamic Programming",

    "backtracking": "Backtracking",

    "greedy": "Greedy",

    "sliding-window": "Sliding Window",

    "heap": "Heap",
    "priority-queue": "Heap",

    "recursion": "Recursion",

    "trie": "Trie",

    "bit": "Bit Manipulation"
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

            shutil.copytree(
                item,
                destination
            )

            print(
                f"Added {item} -> {topic}"
            )
