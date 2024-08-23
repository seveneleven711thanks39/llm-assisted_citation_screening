# Large language model-assisted citation screening

This project demonstrates how to load data from an Excel file, generate screening texts based on specific criteria, and integrate with OpenAI's GPT-4o API, Alphabet's Gemini 1.5 Pro, and Anthropic's  Claude 3.5 Sonnet for automated text processing.

## Features

- Data loading and processing with Pandas and Openpyxl.
- Text generation based on predefined criteria.
- Integration with OpenAI's GPT-4 API, Alphabet's Gemini 1.5 Pro, and Anthropic's Claude 3.5 Sonnet for automated decision making.

## Prerequisites

- Python 3.x
- An OpenAI API key with access to GPT-4o.
- An Alphabet API key with access to Gemini 1.5 Pro. 
- An Anthropic API key with access to Claude 3.5 Sonnet.

## Installation

1. Clone the repository:
2. Install the required dependencies:

## Usage

- Update `data_loader.py` with your Excel file's directory and name.
- Define your criteria in `screening_text_generator.py`.
- Set your OpenAI API key in `gpt_integration.py`, Alphabet API key in `gemini_integration.py`, or Anthropic API key in `claude_integration.py`.
- Run the scripts in the following order:
1. `python data_loader.py`
2. `python screening_text_generator.py`
3. `python gpt_integration.py`, `gemini_integration.py`, or `claude_integration.py`.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
