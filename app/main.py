from fastapi import FastAPI
from contextlib import asynccontextmanager
import grpc
from concurrent import futures

from app.api.v1.router import router as api_v1_router
from protos import item_pb2_grpc
from app.grpc_server.item_servicer import ItemGrpcServicer

def start_grpc_server():
    """Initializes and starts the background gRPC Python server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    item_pb2_grpc.add_ItemGrpcServiceServicer_to_server(ItemGrpcServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    return server

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("Initializing gRPC Server on port 50051...")
    grpc_server = start_grpc_server()
    yield
    # Teardown actions
    print("Shutting down gRPC Server gracefully...")
    grpc_server.stop(0)

# Initialize FastAPI app with lifespan context manager attached!
app = FastAPI(
    title="My FastAPI Microservice (REST + gRPC)",
    description="A scalable, industry-standard FastAPI implementation following layered architecture.",
    version="1.0.0",
    lifespan=lifespan
)

# Connect our REST API routers to the main application
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
