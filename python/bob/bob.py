"""Hey Bob"""


BOB_RESPONSES = {
    "yelling": "Whoa, chill out!",
    "yelling_question": "Calm down, I know what I'm doing!",
    "question": "Sure.",
    "empty": "Fine. Be that way!",
    "other": "Whatever.",
}


def response(hey_bob: str):
    """Return Bob's response to `hey_bob`"""
    is_question = hey_bob.strip().endswith("?")
    is_yelling = hey_bob.isupper()
    is_empty = len(hey_bob.strip()) == 0

    if is_empty:
        return BOB_RESPONSES["empty"]

    if is_question and is_yelling:
        return BOB_RESPONSES["yelling_question"]

    if is_question:
        return BOB_RESPONSES["question"]

    if is_yelling:
        return BOB_RESPONSES["yelling"]

    return BOB_RESPONSES["other"]
