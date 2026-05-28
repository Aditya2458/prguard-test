from fastapi import FastAPI, Request
from github_service import process_pull_request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PRGuard AI Running"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    event = request.headers.get("X-GitHub-Event")

    if event == "pull_request":
        process_pull_request(payload)

    return {"status": "success"}
