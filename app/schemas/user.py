from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    

class CreateUserSchema(UserBaseSchema):
    name: str = Field()
    email: EmailStr = Field()

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Vikas Ukani",
                "email": "vikasukani5@gmail.com",
                "password": "password",
            }
        }
    }

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
