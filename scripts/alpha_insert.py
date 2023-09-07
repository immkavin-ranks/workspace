# Create the initial list of words
word_list = ["aardvark", "aargu", "abacus", "blowfish", "caper"]

# Insert the word "ablone" into the list in alphabetical order
word_to_insert = "ablone"
index_to_insert = 0  # Initialize the index

# Find the correct index to insert the word alphabetically
for i, word in enumerate(word_list):
    if word > word_to_insert:
        index_to_insert = i
        break

# Insert the word at the determined index
word_list.insert(index_to_insert, word_to_insert)

# Print the updated list
print(word_list)
