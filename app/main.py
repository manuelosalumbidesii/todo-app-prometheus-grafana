# app/main.py

from fastapi import FastAPI
from prometheus_client import make_asgi_app
from app.routes import router as todo_router

app = FastAPI()
app.include_router(todo_router)

# Mount Prometheus /metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
