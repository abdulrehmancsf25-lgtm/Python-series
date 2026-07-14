def create_bag_of_words(documents):
    """
    Creates a Bag of Words representation from a list of strings.
    """
    # Step 1: Build the vocabulary
    vocabulary = {}
    for doc in documents:
        # Convert to lowercase and split by spaces (simple tokenization)
        words = doc.lower().split()
        for word in words:
            # Strip simple punctuation to clean the tokens
            word = word.strip(".,!?\"'")
            if word not in vocabulary:
                # Assign a unique index to each new word
                vocabulary[word] = len(vocabulary)
                
    # Step 2: Create the frequency vectors
    bow_matrix = []
    for doc in documents:
        # Initialize a vector of zeros for the length of our vocabulary
        vector = [0] * len(vocabulary)
        words = doc.lower().split()
        for word in words:
            word = word.strip(".,!?\"'")
            if word in vocabulary:
                # Increment the count at the word's specific index
                vector[vocabulary[word]] += 1
        bow_matrix.append(vector)
        
    return vocabulary, bow_matrix

# --- Example Usage ---
corpus = [
    "The quick brown fox jumps.",
    "The quick brown dog barks.",
    "The fox jumps and the dog barks."
]

vocab, matrix = create_bag_of_words(corpus)

print("Vocabulary Dictionary (Word -> Index):")
print(vocab)
print("\nBag of Words Matrix:")
for row in matrix:
    print(row)