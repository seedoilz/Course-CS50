from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave, AKnight),
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(AKnave, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(BKnave, BKnight),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(AKnave, And(AKnave, BKnave)),
    Or(Not(AKnave), Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(BKnave, BKnight),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(AKnave, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Or(Not(AKnave), Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    Or(And(AKnave, BKnave), Not(And(AKnight, BKnight)), And(AKnight, BKnight), Not(And(AKnave, BKnave))),
    Or(Not(BKnight), Or(And(AKnave, BKnight), And(AKnight, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(BKnave, BKnight),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(CKnave, CKnight),
    Or(And(CKnight, Not(CKnave)), And(CKnave, Not(CKnight))),
    # A
    Implication(BKnight, CKnave),
    Implication(BKnave, And(Implication(AKnight, AKnave), Implication(AKnave, AKnight))),
    Implication(BKnave, Not(CKnave)),
    Implication(BKnave, And(
      # A then said 'I am a Knight', A may be a Knight or a Knave:
      Implication(AKnight, AKnight),
      Implication(AKnave, Not(AKnight))
    )),
    # If C is a knight, A is a knight:
    Implication(CKnight, AKnight),
    # If C is a knave, A is not a knight:
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
