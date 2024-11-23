import openai
import os

# Set your OpenAI API key here (or use environment variables)
openai.api_key = "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"  # Replace with your actual OpenAI API key

def get_gpt_response(prompt):
    try:
        # Make a request to the OpenAI API for chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use 'gpt-4' if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the response content from the API response
        bot_response = response['choices'][0]['message']['content']
        
        return bot_response

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
user_input = "What is the capital of France?"
bot_reply = get_gpt_response(user_input)
print("Bot Response:", bot_reply)