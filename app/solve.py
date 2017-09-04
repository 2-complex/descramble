import ospd
import json

s = ospd.ospd()


def wordtest (word, hand):
    """hand is a dictionary defined by and eariler function"""
    target=""
    for letter in word:
        if letter in hand:
            hand[letter]-=1
            if hand[letter]<0:
                if target=="":
                    target=letter
                else:
                    return False, target
        else:
            if target=="":
                target=letter
            else:
                return False, target
    return True, target


def hand_dict(hand):
    """hand is a string of letters"""
    dictionary={}
    for letter in hand:
        dictionary[letter] = dictionary.get(letter,0) + 1
    return dictionary


def compare(item1, item2):
    if item1 == item2:
        return 0
    if item1[0] < item2[0] or (item1[0] == item2[0] and len(item1[1]) > len(item2[1])):
        return -1
    else:
        return 1


def results(hand):
    playable=[]
    for word in s:
        dictionary=hand_dict(hand)
        goodword,needletter=wordtest(word,dictionary)
        if goodword:
            playable.append((needletter, word))
    playable.sort(compare)
    return playable


def json_list(hand):
    l = []
    for letter, word in results(hand):
        if len(letter) > 0:
            l.append({'letter':letter, 'word':word})
        else:
            l.append({'word':word})

    return json.dumps(l)

