# Program: Pages Word Counter
# Description: This program calculates the total number of words in a document
# based on the number of pages and the number of words per page.

# Take input from the user for number of pages
pages = int(input("Enter number of pages: "))

# Take input from the user for words per page
word_per_page = int(input("Enter words per page: "))

# Calculate total words
total_words = pages * word_per_page

# Display the number of pages
print(f"Pages = {pages}")

# Display the words per page
print(f"Words per page = {word_per_page}")

# Display the total number of words
print(f"Total words = {total_words}")
