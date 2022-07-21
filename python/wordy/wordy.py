"""Wordy"""
import operator
import re

INT_RE = re.compile(r"-?[0-9]+(th)?")
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow,
}
VALID_OPERATORS = operations.keys()


def answer(question):
    """Return the value of the requested operations"""

    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    if INT_RE.search(question) is None:
        # the question is missing operands
        raise ValueError("syntax error")

    words = (
        question.removeprefix("What is")
        .removesuffix("?")
        .replace("plus", "+")
        .replace("minus", "-")
        .replace("multiplied by", "*")
        .replace("divided by", "/")
        .replace("raised to the", "**")
    )

    operands = []
    operation = None
    for word in words.split():
        if INT_RE.fullmatch(word):
            operands.append(int(word.strip("th")))

        elif word in VALID_OPERATORS:
            if operation is not None or not operands:
                # Too many operators in a row or no operands yet
                raise ValueError("syntax error")
            operation = operations[word]

        else:
            # The word is not recognized
            raise ValueError("unknown operation")

        if len(operands) == 2:
            if operation is None:
                # No operator between operands
                raise ValueError("syntax error")
            operands = [operation(operands[0], operands[1])]
            operation = None

    if operation is not None:
        # Missing operand
        raise ValueError("syntax error")

    return operands[0]
