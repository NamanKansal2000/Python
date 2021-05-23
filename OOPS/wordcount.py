class Wordcloud:
    def __init__(self, name):
        self.fname = name


def generate_from_frequencies(name):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    counts = {}
    fhand = open(name)
    for line in fhand:
        line = line.strip()
        words = line.split(' ')
        # print(words)
        for word in words:
            word = word.lower()
            # remove punctuation from the string
            no_punct = ""
            for char in word:
                if char not in punctuations:
                    no_punct = no_punct + char

            # print(type(word))
            #     if word.isalpha():
            #         break
            #     elif punct in word:
            #         word = word.split(punct)
            if no_punct not in uninteresting_words:
                counts[no_punct] = counts.get(no_punct, 0) + 1
            # print(no_punct)

    return counts


def largest_frequency(counts):
    bigword = None
    bigcount = None
    for key, value in counts.items():
        if bigword is None or value > bigcount:
            bigword = key
            bigcount = value
    print("Largest occuring word in file: " + bigword)
    print("No of times its occurance in file: " + str(bigcount))
    # return bigword, bigcount


name = input('Enter the filename: ')
dictionary = generate_from_frequencies(name)
print(dictionary)
print()
largest_frequency(dictionary)
