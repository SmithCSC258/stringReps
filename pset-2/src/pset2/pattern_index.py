def patternIndex(text: str, pattern: str) -> list[int]:
    res:list[int] = []
    for i in range(0, len(text) - len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            res.append( i)
    
    return res