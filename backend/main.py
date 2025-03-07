from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.session import engine, Base
from api.v1.endpoints import auth
from api.v1.endpoints import connections

app = FastAPI()

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Adjust for your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(connections.router, prefix="/connections", tags=["Connections"])

# ✅ Root Route
@app.get("/")
def root():
    return {"message": "Welcome to UHub Backend!"}