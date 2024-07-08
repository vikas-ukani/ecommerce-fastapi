from pydantic import BaseModel, Field, EmailStr
from app.schema.user_schema import UserBaseSchema
from app.schema.user_schema import UserModel

class LoginModel(BaseModel): 
    success: bool
    token: str
    user: UserModel | None

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {"email": "vikas@gmail.com", "password": "password"}
        }
    }


class SignUpSchema(UserBaseSchema):
    name: str = Field()
    email: EmailStr = Field()
    password: str = Field()
    confirm_password: str = Field()

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Vikas Ukani",
                "email": "vikasukani5@gmail.com",
                "password": "password",
                "confirm_password": "password",
            }
        }
    }
