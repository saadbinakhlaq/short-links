from fastapi import FastAPI
from short_links.links import router as links_router
from short_links.redirections import router as redirection_router

app = FastAPI(title="Short Link", version="0.0.1")

app.include_router(links_router.router)
app.include_router(redirection_router.router)
