from pydantic import BaseModel, Field, EmailStr


class UserBaseSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)


class UserRegisterSchema(UserBaseSchema):
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "name",
                "last_name": "surname",
                "email": "user@example.com",
                "password": "any"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "any"
            }
        }


class UserSchema(UserBaseSchema):
    id: int = Field(...)

    class Config:
        from_attributes = True
        
        schema_extra = {
            "example": {
                "id": 0,
                "first_name": "name",
                "last_name": "surname",
                "email": "user@example.com",
            }
        }


class TokenSchema(BaseModel):
    access_token: str

    class Config:
        schema_extra = {
            'example': {'token': 'super_secret_jwt_token'}
        }