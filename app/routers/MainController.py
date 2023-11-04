from fastapi import FastAPI, Request, Query, APIRouter
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
import os

current_dir = os.getcwd()
path = os.path.join(current_dir, "public\\favicon.gif")

router = APIRouter(
	tags=["Main"]
)

@router.get("/favicon.ico")
async def favicon():
	return FileResponse(path, media_type="image/gif")
	


routers = [router]
