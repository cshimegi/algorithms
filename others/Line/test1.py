def longest_word_chain(n, words):
    # Initialize the chain length
    chain_length = 1  # The first word is always a valid chain by itself.

    # Loop through the sequence starting from the second word
    for i in range(1, n):
        # Check if the current word starts with the last letter of the previous word
        if words[i][0] == words[i - 1][-1]:
            chain_length += 1
        else:
            break  # Stop if the chain breaks

    return chain_length

print(longest_word_chain(4, ["the","eagle","eats","snakes"]))
print(longest_word_chain(4, ["the","aagle","gats","fnakes"]))
print(longest_word_chain(4, ["the","aagle","gats","snakes"]))
print(longest_word_chain(7, ["snakes","seldom","munch","on","the","highland","ducks"]))
print(longest_word_chain(1, ["snakes"]))