import openai
#from dotenv.main import load_dotenv
import os

#load_dotenv(".env")
on["OPENAI_API_KEY"] = "YOUR_APIKEY_HERE"

# Create OpenAI API instance
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define your prompt
prompt = "Hello, I'm a chatbot. What can I help you with today?"

while True:
        user_input = input("You: ")

        # Generate a response from the OpenAI API
        prompt = user_input
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
        #object: "model-id-2",
        )

        # Print the response
        print(response.choices[0].text.strip())
