from fastapi import FastAPI

app=FastAPI()

import uvicorn

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()