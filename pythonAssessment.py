import re
from collections import Counter


def load_text(filepath):
    """Read the entire file and return its contents as one string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def tokenize_words(text):
    """Return a list of all word tokens (Letters, digits, underscore)."""
    lower = text.lower()
    # Regex to find sequences of word characters
    return re.findall(r"\b\w+\b", lower)


def count_word(words, target):
    """Count exact matches of target in the word list."""
    t = target.lower()
    return sum(1 for w in words if w == t)


def most_common_word(words):
    """Return the (word, count) pair for the most frequent word."""
    if not words:
        return (None, 0)
    freqs = Counter(words)
    # most_common(1) will return a list like so [(word, count)], will access via bracket notation
    return freqs.most_common(1)[0]


def average_word_length(words):
    """Compute average length of words."""
    if not words:
        return 0
    total_chars = sum(len(w) for w in words)
    return total_chars / len(words)


def count_paragraphs(text):
    """Paragraphs defined as blocks separated by one or more blank lines."""
    # Split on one or more blank lines regex
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    return len(paras)


def count_sentences(text):
    """
    Sentences defined by splitting on . ! or ?.
    We will count only non-empty segments.
    """
    segments = [s for s in re.split(r"[\.\!\?]+", text) if s.strip()]
    return len(segments)


def main():
    """Main script to prep article, determine target word, & display results"""
    # 1. Load article text
    filepath = 'news-article.txt'
    text = load_text(filepath)

    # 2. Tokenize words one time
    words = tokenize_words(text)

    # 3. Prompt the user what word to count
    target = input("Enter the word you want to count: ")

    # 4. Perform analysis
    target_count = count_word(words, target)
    common_word, common_count = most_common_word(words)
    avg_len = average_word_length(words)
    para_count = count_paragraphs(text)
    sent_count = count_sentences(text)

    # 5. Display Results
    print("\n --- Text Analysis Results ---")
    print(f"1) '{target}' appears {target_count} time(s).")
    print(f"2) Most common word: '{common_word}' ({common_count} occurences).")
    print(f"3) Average word length: {avg_len:.2f} characters.")
    print(f"4) Number of paragraphs: {para_count}")
    print(f"5) Number of sentences: {sent_count}")


if __name__ == '__main__':
    main()
