from fastapi import FastAPI
from app.database.database  import Base, engine
from app.api.assets_endpoints import router as assets_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Asset Management API",
    description="A REST API for managing assets and generating PDF reports",
    version="1.0.0"
)

# Include routers
app.include_router(assets_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)