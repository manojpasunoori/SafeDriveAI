from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging  # noqa: F401
from app.core.errors import UpstreamError, upstream_error_handler
from app.routes.predict import router as predict_router

app = FastAPI(title="SafeDriveAI API", version="0.2.0")

# CORS for local dev; tighten later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(predict_router)
app.add_exception_handler(UpstreamError, upstream_error_handler)
