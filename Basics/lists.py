numbers = [1, 2, 3, 4, 5]
words = ["forest", "tree", "pinecone", "leaf"]

print(numbers[2])

words.append("mushroom")
print(words[-1])

forestTerms = words.copy()
print(forestTerms[0:6])

def remove_item_from_list(wordList, item):
    wordList.remove(item)
    return wordList

print(remove_item_from_list(forestTerms, "forest"))

def get_index_of_items(wordList, item):
    try:
        return wordList.index(item)
    except:
        return "Item doesn't exist"

print(get_index_of_items(forestTerms, "tree"))

def reverse_list(wordList):
    wordList.reverse()
    return wordList

print(reverse_list(forestTerms))