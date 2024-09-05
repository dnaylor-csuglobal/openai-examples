from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content":
                """A country code type is country_code. 
                what is the numeric country code for Algeria."""
        },
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "country_code",
            "schema": {
                "type": "object",
                "id": "country_code",
                "properties": {
                    "name": {"type": "string"},
                    "code": {"type": "string"},
                    "type": {"type": "string"}
                },
                "required": ["name", "code", "type"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
)

print(completion.choices[0].message)
