from pydantic import BaseModel, Field, field_validator

words = ["кринж", "рофл", "вайб"]

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def check(cls, value):
        for word in words:
            if word in value.lower():
                raise ValueError("Использование недопустимых слов")
        return value
