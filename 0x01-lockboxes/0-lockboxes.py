#!/usr/bin/python3
'''Module tries to find keys corresponding to their boxes'''


def canUnlockAll(boxes):
    '''Returns True or False: all boxes can be unlocked or not'''
    unlockedboxes = [False] * len(boxes)
    unlockedboxes[0] = True
    koh = [0]

    while koh:
        new_koh = koh.pop()
        for k in boxes[new_koh]:
            if k < len(boxes) and not unlockedboxes[k]:
                koh.append(k)
                unlockedboxes[k] = True

    return all(unlockedboxes)
