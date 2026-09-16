# Sentiment Analysis with Hugging Face

This project is a simple beginner example that uses Hugging Face's Transformers library to analyze the sentiment of text.

## What is Hugging Face?

Hugging Face is a popular open-source platform and community for machine learning models, especially for natural language processing (NLP). It provides:

- Pre-trained AI models
- Easy-to-use Python libraries
- Tools for model training and deployment
- A large model hub where developers can share and download models

In simple terms, Hugging Face makes it much easier for developers to use advanced AI models without building everything from scratch.

## How this code relates to Hugging Face

This project uses the `transformers` library from Hugging Face.

The code:

```python
from transformers import pipeline
```

creates a pipeline, which is a Hugging Face helper that makes it easy to use a pre-trained model for a specific task like:

- sentiment analysis
- text generation
- translation
- summarization
- question answering

The line:

```python
classifier = pipeline("sentiment-analysis")
```

loads a model that has already been trained to classify text as positive or negative (and sometimes neutral).

So instead of training a model yourself, you can simply use a ready-made model from the Hugging Face ecosystem.

## What the script does

The file `main.py` sends a few sample sentences to the model:

```python
results = classifier([
    "I absolutely love learning about open-source AI models!",
    "This app is great."
])
```

Then it prints the result like this:

```python
for result in results:
    print(f"Label: {result['label']}, Score: {round(result['score'], 4)}")
```

This prints the predicted sentiment label and how confident the model is.

## Example output

You might see output like:

```text
Label: POSITIVE, Score: 0.9999
Label: POSITIVE, Score: 0.9993
```

The model predicts whether the text is positive or negative, along with a confidence score.

## Prerequisites

Make sure you have Python installed and the Hugging Face Transformers library available in your environment.

Install the dependencies from `requirements.txt` before running the script.

To create a local virtual environment:

```bash
python -m venv hf_env
source hf_env/bin/activate
pip install -r requirements.txt
```

## Run the script

From the project folder, run:

```bash
python main.py
```

## Why this is useful for beginners

This example is a good introduction because it shows:

- how to load a real AI model
- how to pass input text into a model
- how to interpret model output
- how Hugging Face simplifies AI development

## Summary

Hugging Face provides open-source AI models and tools, and this example uses one of those tools, `transformers`, to do sentiment analysis with just a few lines of code. It is a great starting point for learning how modern NLP models work in practice.

## Next steps

Try changing the sample text and experimenting with the results:

```python
"I am excited to learn more about AI"
"This is terrible and confusing"
```

You can also explore other tasks such as:

- text classification
- translation
- summarization
- question answering

This is a beginner-friendly way to learn how Hugging Face powers real-world AI applications.
