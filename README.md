# Large language model-assisted citation screening

This project demonstrates how to load data from an Excel file, generate screening texts based on specific criteria, and integrate with OpenAI's GPT-4o API, Alphabet's Gemini 1.5 Pro, Anthropic's  Claude 3.5 Sonnet, and Meta's Llama 3.3 70B for automated text processing.

## Features

- Data loading and processing with Pandas and Openpyxl.
- Text generation based on predefined criteria.
- Integration with OpenAI's GPT-4 API, Alphabet's Gemini 1.5 Pro, Anthropic's Claude 3.5 Sonnet, and Meta's Llama 3.3 70B for automated decision making.

## Prerequisites

- Python 3.x (Python's virtual environment or (mini)conda)
- An OpenAI API key with access to GPT-4o.
- An Alphabet API key with access to Gemini 1.5 Pro. 
- An Anthropic API key with access to Claude 3.5 Sonnet.
- A Hugging face API key with access to Llama 3.3 70B.

## Installation

1. Clone the repository:
2. Install the required dependencies:

## Usage

- Update `data_loader.py` with your Excel file's directory and name. 
- Define your screening criteria in `screening_text_generator.py`.
- Set your API keys as needed:
 - OpenAI API in `gpt_integration.py`
 - Alphabet API key in `gemini_integration.py`
 - Anthropic API key in `claude_integration.py`
 - Hugging face API key in `llama_integration.py`. Alternatively, you can download LLaMA 3.3 70B locally and configure your own environment for offline inference.
- Run the scripts in the following order:
 - `python data_loader.py`
 - `python screening_text_generator.py`
 - `python gpt_integration.py`, `gemini_integration.py`, `claude_integration.py`, or `llama_integration.py`.

You can run the scripts using the sample file and an Alphabet API key at no cost (charges may apply if you exceed the free usage limit) by following these steps
1. Place the `sample_data.xlsx` file in your working directory. 
2. Set your an Alphabet API key in `gemini_integration.py`.
3. Run `run_example.py`

## Data availability

The datasets used and analyzed in our study are stored in the repository (CQ1_data.csv, CQ2_data.csv, CQ3_data.csv, CQ4_data.csv, CQ5_data.csv, and reference_standard.xlsx). Each file is locked with a passcode "oami2025". 

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
