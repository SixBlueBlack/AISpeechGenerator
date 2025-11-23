from fastapi import FastAPI
import uvicorn

from routers.model_api import router as model_router
from routers.styles_api import router as style_router

app = FastAPI(
    title="Speech Generation API",
    description="API для генерации речей для выступлений",
)

app.include_router(model_router, prefix="/api/model")
app.include_router(style_router, prefix="/api/styles")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
