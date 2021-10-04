from random import choice

with open("../buzzwords.txt", "r") as f:
    word_list = f.readlines()

    for i in range(10):
        word1 = choice(word_list).strip()
        word2 = choice(word_list).strip()
        print(f"Hey bro, check out my {word1} {word2}")
