import os
import re

def formatdick(dick: str) -> int:
    x = re.match("8(=*)D", dick)
    if not x:
        raise ValueError("Invalid dick supplied")
    return len(x.group(1))

def ensureHand(hand) -> None:
    if hand is not None:
        return
    else:
        raise ValueError("Nothing in hand")

def runDicklang(filename: os.PathLike):
    in_hand = None
    vars_ = {}

    with open(filename, 'r') as buffer:
        for line in buffer:
            keyword, *args = line.strip('\n').split(" ")
            match keyword:
                case "DICK":
                    vars_[args[0]] = formatdick(args[1])
                case "GRAB":
                    try:
                        in_hand = [args[0], vars_[args[0]]]
                    except KeyError:
                        raise KeyError("No variable with that name found!")
                case "RELEASE":
                    ensureHand(in_hand)
                    vars_[args[0]] = in_hand[1]
                    in_hand = None
                case "LONGDICK":
                    ensureHand(in_hand)
                    in_hand[1] += formatdick(args[0])
                case "SMALLDICK":
                    ensureHand(in_hand)
                    in_hand[1] -= formatdick(args[0])
                case "HUGEDICK":
                    ensureHand(in_hand)
                    in_hand[1] *= formatdick(args[0])
                case "TINYDICK":
                    ensureHand(in_hand)
                    divisor = formatdick(args[0])
                    if divisor == 0:
                        raise ZeroDivisionError("You're really enjoying yourself aren't you?")
                    in_hand[1] //= divisor
                case "PEE":
                    ensureHand(in_hand)
                    print(f"PEE: 8{'='*int(in_hand[1])}D")
                case "WEE":
                    ensureHand(in_hand)
                    print(f"WEE: {chr(int(in_hand[1]))}")

