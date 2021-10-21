from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api.v1.sumApi.app import sumApi
from core.configs import settings

if settings.DEBUG:
    app = FastAPI(default_response_class=ORJSONResponse)
else:
    app = FastAPI(default_response_class=ORJSONResponse, docs_url=None, redoc_url=None)

# mount subapis
app.mount("/", sumApi)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )
