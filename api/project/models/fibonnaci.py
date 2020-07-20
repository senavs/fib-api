from pydantic import BaseModel


class GenerateFibonacciSequence(BaseModel):
    n: int
