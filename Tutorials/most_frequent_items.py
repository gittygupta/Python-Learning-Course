
# converting a text into a list

from collections import Counter

texts = "The domain name info is a generic top-level domain in the Domain Name System of the Internet."\
        "The name is derived from information, though registration requirements do not prescribe any particular theme."
text_cap = texts.capitalize()

words = text_cap.split()       # It basically splits the string into a list of words
print(words)

counter = Counter(words)                # It always takes in a list

# suppose we wanna print a certain number of most common items

top_three = counter.most_common(3)              # It takes in the number of top most common items we wanna print
print("Top 3 common words:", top_three)                        # It shows the top 3 occurring items, with the number of occurences

# REMEMBER: This is a case sensitive function
