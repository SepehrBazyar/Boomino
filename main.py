from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from api.v1.sumApi.app import sumApi
from api.v1.sumApi.sum.views import limiter
# from core.utils import startup
from core.configs import settings
from core.database import connect_mongodb, close_mongodb

if settings.DEBUG:
    app = FastAPI(default_response_class=ORJSONResponse)
else:
    app = FastAPI(default_response_class=ORJSONResponse, docs_url=None, redoc_url=None)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# startup event handler
# app.add_event_handler('startup', startup)
app.add_event_handler('startup', connect_mongodb)

# shutdown event handler
app.add_event_handler('shutdown', close_mongodb)

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
