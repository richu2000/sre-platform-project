from fastapi import FastAPI
from app.config import APP_NAME,APP_VERSION
app = FastAPI(title=APP_NAME)

@app.get("/")
def root():
  return {
     "message":"SRE platform is running"
  }

@app.get("/health")
def health():
  return {
     "status":"healthy"
  }

@app.get("/version")
def version():
  return {
     "version": APP_VERSION
  }

#__main__ means "run this part only when this file is executed directly.
if __name__ == "__main__":
   import uvicorn
   uvicorn.run(
     "app.main:app",
     host = "0.0.0.0",
     port = 8000,
     reload = True
   )
