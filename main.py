from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
from config import API_TITLE, API_VERSION, API_DESCRIPTION
from routes import orders, paper_types, admin

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION,
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    create_tables()
    print("Database tables created successfully")

app.include_router(orders.router)
app.include_router(paper_types.router)
app.include_router(admin.router)

@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint for PrintFlow API"""
    return {
        "message": "Welcome to PrintFlow API",
        "version": API_VERSION,
        "description": API_DESCRIPTION,
        "endpoints": {
            "orders": "/orders",
            "paper_types": "/paper-types",
            "admin": "/admin",
            "documentation": "/api/docs"
        }
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)