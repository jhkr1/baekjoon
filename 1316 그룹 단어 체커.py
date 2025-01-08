def is_group(word):
    seen = set()
    prev_char = None

    for char in word:
        if char in seen and char != prev_char:
            return False
        seen.add(char)
        prev_char = char
    return True

n = int(input())
words = [input().strip() for _ in range(n)]
cnt = sum(is_group(word) for word in words)
print(cnt)