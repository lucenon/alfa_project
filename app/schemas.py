from pydantic import BaseModel, Field


class Input(BaseModel):
    text: str = Field(..., description="Input text")


class Output(BaseModel):
    class_: str = Field(..., description="Class name")
    label: int = Field(..., description="Class label")
    model_bypassed: bool = Field(..., description="True if the input was skipped as neutral (empty, numbers, or symbols only)")

