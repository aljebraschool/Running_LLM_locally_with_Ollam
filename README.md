# Running an LLM Locally with Ollama
This repository demonstrates how to run an open-source model locally using [Ollama](https://ollama.com/search). Ollama allows you to easily download and run large language models (LLMs) on your local machine, so you can develop and test locally without relying on cloud-based APIs.

## **Below is a demonstration of the app's interface:**


## Prerequisites
1. Ollama Installed
 - You must have [Ollama](https://github.com/ollama/ollama) installed on your system. 
 - Refer to the official [Ollama](https://github.com/ollama/ollama) docs for instructions on installing it for your OS.
2. Model Downloaded
 - You need to have your chosen model pulled locally via Ollama. For example, if you want to use a model called llama2, you might run:

``` bash

ollama pull llama2

```
- Ensure the model name in your code matches what you’ve pulled locally.

## Setup
1. Clone the Repository
   ``` bash
  git clone https://github.com/aljebraschool/running-llm-locally-with-ollama.git
  cd running-llm-locally-with-ollama
   ```

2. Create and activate a virtual environment (optional but recommended)
   ``` bash
    # On macOS/Linux
    python3 -m venv env
    source env/bin/activate
    
    # On Windows
    python -m venv env
    env\Scripts\activate
   ```

3. Install dependencies
   ``` bash
   pip install -r requirements.txt
   ```

## Usage
 1. Start the Application
  run:
``` bash
streamlit run app.py

```
The script will connect to your local Ollama installation and load the locally installed model.

2. Interact with the Model

  - Enter prompts/questions in the provided text box or command-line interface (depending on your UI).
  - The script will use your locally installed model through Ollama to generate responses.

## Notes
 - Model Name: Make sure the model name in your code (for example, "llama2") matches the one you’ve downloaded via ollama pull.
 - Performance: Large models can be resource-intensive. Ensure your machine has enough memory (RAM) and compute power to run the chosen model effectively.
 - Compatibility: Ollama primarily targets macOS on Apple Silicon. Check the [Ollama repo](https://github.com/ollama/ollama) for updates on Linux or Windows support.

## Troubleshooting
 - Model Not Found: If you see an error indicating the model isn’t found, confirm you ran ollama pull <model-name> with the correct name.
 - High Memory Usage: If you experience slowdowns or crashes, try a smaller model or reduce context lengths.

## Contributing
Pull requests are welcome! Feel free to open an issue or submit improvements if you have ideas for additional features or better documentation.

