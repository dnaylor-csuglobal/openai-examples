from openai import OpenAI
client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "What is the numeric country code for Algeria."
        }
    ]
)

print(completion.choices[0].message)