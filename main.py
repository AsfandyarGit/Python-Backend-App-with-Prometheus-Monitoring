from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from prometheus_client import Counter

app = FastAPI()

# Instrument the FastAPI app
Instrumentator().instrument(app).expose(app)

http_requests_total = Counter("http_requests_total", "Total number of HTTP requests")

# Define your routes
@app.get("/")
async def read_root():
    # Increment the http_requests_total counter
    http_requests_total.inc()
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    # Increment the http_requests_total counter
    http_requests_total.inc()
    return {"item_id": item_id, "q": q}