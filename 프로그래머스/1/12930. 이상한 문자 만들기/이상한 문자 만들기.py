def solution(s):
    s = s.split(" ")
    answer = []

    for word in s:
        new_word = ""
        for idx, ch in enumerate(word):
            if idx % 2 == 0:
                new_word += ch.upper()
            else:
                new_word += ch.lower()
        answer.append(new_word)

    return " ".join(answer)


