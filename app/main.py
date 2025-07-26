from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.database import Base, engine
from app.routes import users, calculations, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Mount frontend folder to serve static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Route to serve register.html
@app.get("/register")
def serve_register():
    return FileResponse(os.path.join("frontend", "register.html"))

# Route to serve login.html
@app.get("/login")
def serve_login():
    return FileResponse(os.path.join("frontend", "login.html"))

# Include API routers
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(calculations.router, prefix="/api", tags=["Calculations"])
app.include_router(auth.router, prefix="/api", tags=["Auth"])
