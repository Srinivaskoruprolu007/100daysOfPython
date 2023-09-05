def rev_sentence(sentence: str):
    # first split the sentence into words
    words = sentence.split(' ')[::-1]
    result = []
    for i in words:
        result.append(i)

    print(" ".join(result))


sen = input("Enter the sentence to reverse ")
print(rev_sentence(sen))


# my favourite and good approach
