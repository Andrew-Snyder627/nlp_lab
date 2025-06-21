# News Article Text Analysis Lab

This repository contains a Python program and accompanying test suite to perform basic text analysis on a news article. It demonstrates reading files, tokenizing text, counting occurrences, and splitting on paragraphs and sentences.

## Project Structure

    nlp_lab/
    ├── news_article.txt            # Sample article to analyze
    ├── pythonAssessment.py         # Main analysis script
    ├── test_pythonAssessment.py    # pytest suite for all functions
    └── README.md                   # This file

## Prerequisites

- Python 3.7 or higher
- `pytest` for running tests

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/nlp_lab.git
   cd nlp_lab
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate        # Windows
   ```
3. Install pytest:
   ```bash
   pip install pytest
   ```

## Usage

1. Ensure `news_article.txt` contains the article you want to analyze.
2. Run the analysis script:
   ```bash
   python3 pythonAssessment.py
   ```
3. When prompted, enter the word you wish to count. The script will output:
   - The number of times your target word appears
   - The most common word and its count
   - The average word length
   - The number of paragraphs
   - The number of sentences

## Testing

To run the full test suite with pytest:

```bash
pytest -v
```

All tests should pass, verifying each function’s behavior and end-to-end integration on a small sample text.

## Function Summary

- `load_text(filepath)` — Read file contents into a string.
- `tokenize_words(text)` — Split text into lowercase word tokens.
- `count_word(words, target)` — Count exact matches of a target word.
- `most_common_word(words)` — Return the most frequent word and its count.
- `average_word_length(words)` — Compute the average length of tokens.
- `count_paragraphs(text)` — Count blocks separated by blank lines.
- `count_sentences(text)` — Count segments split by `.`, `!`, or `?`.

## Contributing

Feel free to submit issues or pull requests for improvements, edge-case handling, or performance enhancements.

---
