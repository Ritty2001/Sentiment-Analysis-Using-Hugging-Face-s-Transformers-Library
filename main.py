from transformers import pipeline

# Load a pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Pass text samples into the classifier
results = classifier([
    "I absolutely love learning about open-source AI models!",
    "This app is great."
])

# Print the model's predictions
for result in results:
    print(f"Label: {result['label']}, Score: {round(result['score'], 4)}")
