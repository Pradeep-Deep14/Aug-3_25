import textblob

def spelling_checker():
    while True:
        word = input("Please enter a word: ")
        blob = textblob.TextBlob(word)
        corrected_word = str(blob.correct())
        if corrected_word != word:
            response = input(f"Did you mean '{corrected_word}'? (yes/no): ")
            if response.lower() == "yes":
                return corrected_word
            else:
                print("Please try entering the word again.")
        else:
            return word

# Example usage:
if __name__ == "__main__":
    result = spelling_checker()
    print(f"Final word: {result}")