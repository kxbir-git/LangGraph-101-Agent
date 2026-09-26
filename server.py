from fastapi import FastAPI
from langserve import add_routes
from fastapi.responses import RedirectResponse
import uvicorn
from dotenv import load_dotenv

# Environment variables load karein (.env se)
load_dotenv(".env")

# Apne Research Agent ko import karein
from agents.researcher.graph import graph

# FastAPI app initialize karein
app = FastAPI(
    title="Research Agent API",
    version="1.0",
    description="A production-ready API server for the LangGraph Research Agent"
)

# Root URL pe aane wale users ko documentation pe redirect karein
@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

# LangServe ke through Agent ka route banayein
add_routes(
    app,
    graph,
    path="/research-agent",
)

if __name__ == "__main__":
    print("Server is starting... You can access the API docs at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
