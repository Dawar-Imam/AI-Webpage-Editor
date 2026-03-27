from pydantic import BaseModel


class DemoRequest(BaseModel):
    """Pydantic model for demo request."""
    text: str
