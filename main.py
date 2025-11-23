from fastapi import FastAPI
import uvicorn

from routers.api import router as api_router

app = FastAPI(
    title="Speech Generation API",
    description="API для генерации речей для выступлений",
)

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
