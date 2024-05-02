#!/usr/bin/python3
'''Module tries to find keys corresponding to their boxes'''


def canUnlockAll(boxes):
    '''Returns True or False: all boxes can be unlocked or not'''
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
