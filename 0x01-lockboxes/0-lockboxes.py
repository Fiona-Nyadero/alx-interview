#!/usr/bin/python3
''''''


def canUnlockAll(boxes):
    ''''''
    n = len(boxes)
    unlockedboxes = set()
    koh = set([0])

    while koh:
        new_koh = set()
        for k in koh:
            unlockedboxes.add(k)
            new_koh.update(set(boxes[k]) - unlockedboxes)

    if len(unlockedboxes) == n:
        return True

    koh = new_koh

    return len(unlockedboxes) == n
