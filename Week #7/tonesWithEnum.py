#!/usr/bin/env python3
from enum import Enum

DEEP_TONE = 'aáoóuú'
HIGH_TONE = 'eéiíöőüű'

class Tone(Enum):
    DEEP = 1
    HIGH = 2
    MIXED = 3
    NONE = 4

    def tone(s):
        deep = False
        high = False
        for c in s:
            if deep and high:
                return Tone.MIXED.name
            elif c in DEEP_TONE and not deep:
                deep = True
            elif c in HIGH_TONE and not high:
                high = True
        if deep and not high:
            return Tone.DEEP.name
        elif not deep and high:
            return Tone.HIGH.name
        elif not deep and not high:
            return Tone.NONE.name


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pffff"]
    for x in words:
        print("{}: This word is {} toned!".format(x, Tone.tone(x)))


if __name__ == "__main__":
    main()