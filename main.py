import openai
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR API KEY HERE"

# Create OpenAI API instance
openai.api_key = os.environ["OPENAI_API_KEY"]

# Load your dataset from a text file
dataset_file = "my_dataset.txt"

def load_dataset():
    with open(dataset_file, "r") as f:
        return f.read()

def save_dataset(dataset_text):
    with open(dataset_file, "w") as f:
        f.write(dataset_text)

# Load the existing dataset
dataset_text = load_dataset()

# Read the set of journals
journals_file = "journals.txt"

def load_journals():
    with open(journals_file, "r") as f:
        return f.readlines()

journals = load_journals()

# Define your prompt and append the dataset text
prompt = f"Hello, I'm a chatbot. What can I help you with today?\n{dataset_text}"

while True:
    user_input = input("You: ")

    # Check if the user input matches any journal
    if any(journal.strip().lower() in user_input.lower() for journal in journals):
        # Perform actions for reading a journal
        # Example: Fetch the journal content and provide a response
        response = "Sure! Let me fetch the journal for you."

    else:
        # Generate a response using the prompt
        prompt = f"{prompt}\nYou: {user_input}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Get the chatbot's response
        response_text = response.choices[0].text.strip()

        # Append the user input and chatbot response to the dataset
        dataset_text += f"\nUser: {user_input}\nChatbot: {response_text}"
        save_dataset(dataset_text)

        # Print the chatbot's response
        print(f"Chatbot: {response_text}")
