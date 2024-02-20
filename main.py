from fastapi import FastAPI

from router.group_router import router

app = FastAPI(title="Cluster Manager API")

app.include_router(router, prefix="/v1/group", tags=["group"])


