from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

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

# @TASK: Complete this exercise.

def check_that_these_are_equal(result, expected):
  if result == expected:
      print("Test passed!")
  else:
      print(f"Test failed: expected {expected}, but got {result}")

print("")
print("Function: report_long_words")

def report_long_words(words):
    long_words = []
  # loop through each word in the list
    for word in words: 
  # words longer than 10 characters and don't contain a hyphen
        if len(word) > 10 and '-' not in word:
  # If the word is longer than 15 characters, shorten and add an ellipsis 
            if len(word) > 15:
                word = word[:15] + '...'
  # Add the word to the list of long words 
            long_words.append(word)
  # join the list of long words into a string, separated by commas 
    long_words_str = ", ".join(long_words) 
  # If there are no long words, return the base string 
    if long_words_str: 
        return f"These words are quite long: {long_words_str}"
    else:
        return f"These words are quite long: "


check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)
