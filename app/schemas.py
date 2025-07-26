from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class CalculationBase(BaseModel):
    operation: str
    operand1: float
    operand2: float
    result: float

class CalculationCreate(CalculationBase):
    pass

class CalculationRead(CalculationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
