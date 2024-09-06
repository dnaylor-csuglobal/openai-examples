from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum
from typing import ForwardRef, Union
import json

client = OpenAI()


class JoinOperator(str, Enum):
    OR = "or"
    AND = "and",
    NOT = "not"

class AudienceType(str, Enum):
    AUDIENCE = "audience"


JoinExpression = ForwardRef('JoinExpression')


class Audience(BaseModel):
    name: str
    type: AudienceType


class JoinExpression(BaseModel):
    left: Union[Audience, JoinExpression]
    right: Union[Audience, JoinExpression]
    type: JoinOperator


class Model(BaseModel):
    value: Union[Audience, JoinExpression]


system_prompt = """
An audience is a list of people.
all_teachers is the name of an audience containing teachers.
all_drivers is the name of an audience containing drivers.
all_parents is the name of an audience containing parents.
audiences may be combined using set operators such as "or", "and", and "not"
"""

while (True):
    print("Please type an prompt:")
    prompt = input()
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": prompt
            },
        ],
        response_format=Model,
    )
    json_data = completion.choices[0].message.content
    obj = json.loads(json_data)
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)



