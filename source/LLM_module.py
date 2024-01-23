import openai
from openai import OpenAI


def generate_profile():
    # prompt = ", ".join(keywords)
    prompt = "Generate user profiles for 20 users as a 50-word unique description, " \
             "ages of these users follow Gaussian distribution, gender is half and half." \
             "Listed your response by user id." \
             "Based on this example: User ID 15: Benjamin is a 48-year-old male who is a history enthusiast. He enjoys reading historical books and visiting museums to learn about different eras and civilizations."
    print(prompt)

    api_key = "YOUR_API_KEY"
    client = OpenAI(api_key=api_key)

    parameters = {
        'model': 'gpt-3.5-turbo',  # Model name or ID
        'messages': [{"role": "user", "content": prompt}],
        'max_tokens': 4000,  # Maximum number of tokens to generate
        'temperature': 0.8,  # Controls the randomness of the output
        'n': 1,  # Number of responses to return
        'stop': None  # Token at which to stop the generated text
    }

    response = client.chat.completions.create(**parameters)

    generated_text = response.choices[0].message.content
    return generated_text


def generate_information(received, profile):
    # prompt = ", ".join(keywords)
    prompt = f"You are a social media user with a profile '{profile}', " \
              f"generate one piece of information to spread your received information '{received}' " \
              f"based on your preference. In the first person aspect with no more than 50 words."

    api_key = "YOUR_API_KEY"
    client = OpenAI(api_key=api_key)

    parameters = {
        'model': 'gpt-3.5-turbo',  # Model name or ID
        'messages': [{"role": "user", "content": prompt}],
        'max_tokens': 500,  # Maximum number of tokens to generate
        'temperature': 0.8,  # Controls the randomness of the output
        'n': 1,  # Number of responses to return
        'stop': None  # Token at which to stop the generated text
    }

    response = client.chat.completions.create(**parameters)

    generated_text = response.choices[0].message.content
    return generated_text


if __name__ == "__main__":
    # Generate text
    text = generate_profile()

    print("Generated Text:\n", text)
    with open("../data/input/user_profile_small.txt", "w") as file:
        file.write(text)
