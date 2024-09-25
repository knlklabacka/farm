from fastapi import FastAPI, Request, Header

app = FastAPI()

@app.get("/")
async def raw_request(request: Request):
  return {
    "message": request.base_url,
    "all": dir(request)
  }

@app.get("/headers")
async def read_headers(user_agent: str | None = Header(None)):
  return {"User-Agent": user_agent }