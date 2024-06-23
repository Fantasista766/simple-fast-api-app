from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional


class STaskAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100,
                      description="The task name")
    description: Optional[str] = Field(
        None, max_length=500, description="The task description")

    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('Name must not be empty')
        return value


class STask(STaskAdd):
    id: int = Field(..., description="The unique identifier of the task")
    model_config = ConfigDict(from_attributes=True)


class STaskID(BaseModel):
    ok: bool = Field(
        True, description="Indicates if the operation was successful")
    task_id: int = Field(..., description="The unique identifier of the task")
