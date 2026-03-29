from fastapi import FastAPI
from app.api.v1.router import router as api_v1_router

# Initialize FastAPI app with descriptive metadata
app = FastAPI(
    title="My FastAPI Microservice",
    description="A scalable, industry-standard FastAPI implementation following layered architecture.",
    version="1.0.0",
)

# Connect our API routers to the main application
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def root():
    """
    Root endpoint primarily used for health checks.
    """
    return {
        "status": "ok", 
        "message": "Microservice is running! Navigate to /docs for Swagger UI.",
        "version": app.version
    }
