history, total = [], 0

async def cache(a: int, b: int) -> int:
    """
    Sample Cache Input
    """

    global total
    result = a + b
    history.append({
        'a': a,
        'b': b,
    })
    total += result
    return result

async def login():
    """
    
    """

    pass
