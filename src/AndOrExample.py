from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum
from typing import ForwardRef, Union

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
    all_teachers is the name of an audience containing all teachers.
    all_drivers is the name of an audience containing all drivers.
    all_parents is the name of an audience containing all parents.
"""

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            # "content": "give me an audience that are both teachers and drivers but not parents"
            "content": "give me an audience that are teachers and drivers, or parents"
        },
    ],
    response_format=Model,
)

message = completion.choices[0].message

print(message)
