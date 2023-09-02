# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

word_list = ['hello', 'nonbiological', 'Kay', 'this-is-a-long-word', 'antidisestablishmentarianism']

def get_long_words(word_list):
    long_words = []
    for word in word_list:
        if word.find('-') == -1:
            if len(word) > 10 and len(word) <= 15:
                long_words.append(word)
            else:
                if len(word) > 15:
                    long_words.append(word[0:15] + "...")
    return long_words

print(get_long_words(word_list))