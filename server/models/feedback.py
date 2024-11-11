from pydantic import BaseModel

class Feedback(BaseModel):
    id: int
    name: str
    description: str | None = None