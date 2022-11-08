
def order(sentence):
    result = sentence.split()
    result.reverse()
    forditott = " ".join(result)
    return forditott

print(order("How are you"))