import nltk
from collections import Counter
from nltk.tokenize import WhitespaceTokenizer
import string
from pathlib import Path
import os

# Ensure necessary NLTK package is available
nltk.download('punkt_tab')
# Check NLTK data path
# print(nltk.data.path)

class BigramProbabilityCalculator:
    def __init__(self):
        """
        Initialize calculator (no text initially).
        """
        self.tokenizer = WhitespaceTokenizer()
        self.bigram_counts = Counter()
        self.total_bigrams = 0
        self.previous_token = None

    def tokenize(self, text: str) -> list[str]:
        return self.tokenizer.tokenize(text)

    @staticmethod
    def remove_punctuation(tokens: list[str]):
        """
        Tokenize text and remove punctuation.
        """
        cleaned_tokens = []
        for token in tokens:
            # remove punctuation
            cleaned_token = token.translate(str.maketrans('', '', string.punctuation))
            # if the token is not empty after removing punctuation
            if cleaned_token:
                cleaned_tokens.append(cleaned_token)
        return cleaned_tokens

    def process_chunk(self, chunk):
        """
        Process a chunk of text.
        """
        tokens = self.tokenize(chunk)
        cleaned_tokens = self.remove_punctuation(tokens)
        bigrams = zip(cleaned_tokens, cleaned_tokens[1:], cleaned_tokens[2:])
        self.bigram_counts.update(bigrams)
        self.total_bigrams += len(cleaned_tokens) - 1

    def compute_trigram_probability(self):
        pass

    def compute_bigram_probability(self):
        """
        Compute the bi-gram probability
        """
        bigram_probabilities = 1
        k = 0
        for bigram, count in self.bigram_counts.items():
            prob = count
            # Same bigram needs to be calculated
            for _ in range(count):
                bigram_probabilities *= prob
            k += count

        # Compute the final probability using the k-th root formula
        computed_prob = bigram_probabilities ** (1 / k)

        return round(computed_prob, 5), k

    @staticmethod
    def load_text_from_file(file_path: str):
        """
        Load test from give file path

        """
        chunk_size = 1024*1024  # TODO: how to chunk correctly

        with open(file_path, "r") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break  # End of file
                yield chunk

    def report_to_file(self, file_path: str, bigram_prob: float, k_value: int):
        """
        Report to file
        """
        with open(file_path, "w") as f:
            f.write(f"Bigram Probability: {bigram_prob}\n")
            f.write(f"Value of k: {k_value}\n")


def main(file_path: str):
    try:
        # Initialize calculator
        calculator = BigramProbabilityCalculator()

        # Process loaded chunked text
        for chunk in calculator.load_text_from_file(file_path):
            calculator.process_chunk(chunk)

        # Calculate bigram probability and k value
        bigram_prob, k_value = calculator.compute_bigram_probability()

        # Save results to a file
        filename = os.path.splitext(os.path.basename(file_path))[0]
        calculator.report_to_file(f"{filename}_report.txt", bigram_prob, k_value)
    except Exception as e:
        print(f"Something bad happened: {repr(e)}")
        exit(1)


if __name__ == "__main__":
    file_path = input("Enter the file path: ")

    if not file_path:
        print("Please enter a valid file path.")
        exit(1)
    elif not Path(file_path).is_file():
        print("File not found.")
        exit(1)

    main(file_path)
