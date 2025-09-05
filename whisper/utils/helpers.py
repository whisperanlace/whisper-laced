# utils/helpers.py

def chunk_list(lst: list, n: int):
    """Split list into chunks of size n"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
