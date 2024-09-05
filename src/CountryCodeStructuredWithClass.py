from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()


# Note that it doesn't seem possible to set additional fields such as type = "country_code"
class CountryCode(BaseModel):
    name: str
    code: str
    type: str


completion = client.beta.chat.completions.parse(
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
    response_format=CountryCode,
)

print(completion.choices[0].message)
