from fastapi import FastAPI
from app.routes import auth_routes
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
# Registrar rutas
app.include_router(auth_routes, prefix="/auth", tags=["Authentication"])
