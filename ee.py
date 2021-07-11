#!/usr/bin/python3

# ee-brightbox default password generator
# created by puz00

def load_dictionary():
    # loads words from a given dictionary txt file
    dictionary_file = open("engmix_2.txt")
    for word in dictionary_file.read().split("\n"):
        words.append(word)
    dictionary_file.close()

def populate_words(length, list):
    # finds words in the word list created from the dictionary txt file
    # the length of these words and the list to store them in are passed as parameters
    for word in words:
        if len(word) == length:
            list.append(word)

def get_words(first, second, third):
    # uses some nasty nested loops to create possible passwords
    # the possible passwords are words of different lengths separated by -
    # the order of word lengths is specified in main by passing them as parameters
    for i in range(len(first)):
        word_one = first[i]
        for j in range(len(second)):
            word_two = second[j]
            for k in range(len(third)):
                word_three = third[k]
                test_password = "{}-{}-{}".format(word_one, word_two, word_three)
                passwords.append(test_password)

# main
three = []
four = []
five = []
words = []

# load the dictionary and slice the first 1000 words into the list called words
# the first 1000 words are chosen to keep things fast as this is a proof of concept program
load_dictionary()
words = words[:1000]

# three lists are populated with words originally from the dictionary
# these will be the words with 3, 4 and 5 letters
# ee-brightbox routers use words with 3, 4 and 5 letters for their default password
populate_words(3, three)
populate_words(4, four)
populate_words(5, five)

# create a list for possible passwords
# then fill it with combinations of words with different lengths separated by -
# this is how ee-brightbox default passwords are created e.g. one-spent-face
passwords = []
get_words(three, four, five)
get_words(three, five, four)
get_words(four, three, five)
get_words(four, five, three)
get_words(five, three, four)
get_words(five, four, three)

# write each possible password into a file called passes.txt
with open("passes.txt", "w") as f:
    for item in passwords:
        f.write("{} \n".format(item))