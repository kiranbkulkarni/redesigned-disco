from pprint import pprint

sentence = "This is a common interview question"

char_freq = {}

for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

pprint(char_freq, width=1)

# What if you want to sort the dictionary

char_frq_sorted = sorted(char_freq.items(),
                         key=lambda kv: kv[1],
                         reverse=True)

print(char_frq_sorted)
