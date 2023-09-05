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
def rev_sen(sentence:str):
    stack = []
    for word in sentence.split():
        stack.append(word)
    reverse_list = []
    while stack:
        reverse_list.append(stack.pop())

    return " ".join(reverse_list)


print(rev_sen(sen))
