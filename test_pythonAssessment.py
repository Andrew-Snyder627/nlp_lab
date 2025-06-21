import pytest

# Import functions
from pythonAssessment import (
    load_text,
    tokenize_words,
    count_word,
    most_common_word,
    average_word_length,
    count_paragraphs,
    count_sentences,
)


def test_load_text(tmp_path):
    sample = "Line one\nLine two\n"
    p = tmp_path / "sample.txt"
    p.write_text(sample, encoding="utf-8")
    # This should return exactly what I wrote
    assert load_text(str(p)) == sample


def test_tokenize_words():
    text = "Hello, world! 123 _underscore_"
    # expecting lowercase, digits & underscore separated
    assert tokenize_words(text) == ["hello", "world", "123", "_underscore_"]


def test_count_word_with_adjacent_punctuation():
    text = "word, word. word! WORD?"
    words = tokenize_words(text)
    assert count_word(words, "word") == 4


def test_count_word_and_most_common():
    words = ["apple", "pie", "apple", "chicken"]
    assert count_word(words, "apple") == 2
    assert count_word(words, "chicken") == 1
    # most common should be apple
    common, frequency = most_common_word(words)
    assert common == "apple" and frequency == 2


def test_count_word_case_insensitive():
    words = tokenize_words("Apple apple APPLE")
    assert count_word(words, "apple") == 3


def test_most_common_empty():
    assert most_common_word([]) == (None, 0)


def test_average_word_length():
    words = ["a", "bb", "ccc"]  # lengths 1, 2, & 3. avg = 2.0
    assert average_word_length(words) == pytest.approx(2.0)


def test_average_word_length_empty():
    assert average_word_length([]) == 0


def test_count_paragraphs():
    text = "Paragraph one line\nstill paragraph 1.\n\nParagraph two starts here.\n\n\nParagraph three."
    # splits on one or more blank lines.
    assert count_paragraphs(text) == 3


def test_single_paragraph_no_blank_lines():
    text = "Just one paragraph here, no blank line."
    assert count_paragraphs(text) == 1


def test_count_sentences():
    text = "Hello hello. Is this working? Yes! Trailing..."
    # splits on . ! ?. will not count empty segments
    assert count_sentences(text) == 4


def test_single_sentence_no_delimiters():
    text = "This is a sentence without punctuation"
    assert count_sentences(text) == 1


def test_empty_text_paras_and_sents():
    text = ""
    assert count_paragraphs(text) == 0
    assert count_sentences(text) == 0


def test_full_integration_on_small_text(tmp_path):
    sample = (
        "Apple apple pie.\n\n"
        "Best apple pie recipes? Yes!\n"
    )
    p = tmp_path / "mini.txt"
    p.write_text(sample, encoding="utf-8")

    text = load_text(str(p))
    words = tokenize_words(text)
    # count_word
    assert count_word(words, "apple") == 3
    # most common
    common, frequency = most_common_word(words)
    assert common == "apple" and frequency == 3
    # avg length > 0
    assert average_word_length(words) > 0
    # paragraphs, 2 blocks
    assert count_paragraphs(text) == 2
    # sentences, 3 sentences
    assert count_sentences(text) == 3
