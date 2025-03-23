from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
import os
import uvicorn
from sim import StartupSimulation
import asyncio
import base64

app = FastAPI(title="AI Startup Simulator")

# Set up static files and templates
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/simulate", response_class=HTMLResponse)
async def simulate(request: Request, product: str = Form(...)):
    # Run simulation
    simulation = StartupSimulation(product)
    simulation.run()
    
    # Get paths to generated visualizations
    metrics_path = "startup_metrics.png"
    graph_path = "agent_relationships.png"
    
    # Read images for display
    with open(metrics_path, "rb") as f:
        metrics_img = base64.b64encode(f.read()).decode()
    
    with open(graph_path, "rb") as f:
        graph_img = base64.b64encode(f.read()).decode()
    
    return templates.TemplateResponse(
        "results.html", 
        {
            "request": request,
            "product": product,
            "metrics_img": metrics_img,
            "graph_img": graph_img
        }
    )

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)