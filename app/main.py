from fastapi import FastAPI

app = FastAPI(title="sre platform demo")

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
     "version":"1.0.0"
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
