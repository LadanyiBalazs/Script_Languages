#!/usr/bin/env python3

TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

repl = {'á': 'a', 'ű': 'u', 'ő': 'o', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ú': 'u', 'ü': 'u'}

def main():
    for w in TEXT.split():
        vege = ''.join([repl[c] if c in repl else c for c in w])
        print(vege, end=" ")

if __name__ == "__main__":
    main()