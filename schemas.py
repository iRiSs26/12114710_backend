from pydantic import BaseModel
from typing import List, Optional

class TaskBase(BaseModel):
    title: str
    is_completed: Optional[bool] = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

class TaskList(BaseModel):
    tasks: List[Task]
