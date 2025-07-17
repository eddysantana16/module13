from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, calculations

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(calculations.router, prefix="/api", tags=["Calculations"])
