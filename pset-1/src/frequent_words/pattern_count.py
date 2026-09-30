"""Count occurrences of a pattern in text."""


from itertools import count
from xml.dom.minidom import Text


def PatternCount(text: str, pattern: str) -> int:
    """Return the number of occurrences of pattern in text.


    Matches are case-sensitive and may overlap. Assume pattern is nonempty.
    Return 0 if pattern is longer than text or text is empty.

    Example:
        PatternCount("AAAA", "AA") returns 3.
    """
    count = 0
    # Loop over all possible starting positions of Pattern in Text
    for i in range(len(text) - len(pattern)+1):
        # Check if the substring of length len(Pattern) starting at index i matches Pattern
        if text[i : i + len(pattern)] == pattern:
            count += 1
    return count
