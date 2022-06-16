import fastapi
import requests

app = fastapi.FastAPI()

@app.get("/{webhook_data}/{webhook_url}")
async def webhook_call(webhook_data, webhook_url):
  return requests.post(webhook_url, webhook_data)