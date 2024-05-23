from fastapi import FastAPI
from routers.organization import organization_router
from routers.contractors import contractors_router
from routers.auth import authentication_router
from utils.auth.dependencies import require_role
from fastapi import Depends


app = FastAPI(
    docs_url="/docs",
    redoc_url=None,
    title="Procure Chain",
    description="A blockchain based system for governments to manage procurement requests",
    summary="Procure Chain WebApp Swagger APIs",
    version="0.0.1",
    contact={"name": "Maaz & Ali"},
    swagger_ui_parameters={"syntaxHighlight": False},
)

app.include_router(organization_router)
app.include_router(contractors_router)
app.include_router(authentication_router)


@app.get("/hello")
async def hello(token: str = Depends(require_role("admin"))):
    return {"success": True}
