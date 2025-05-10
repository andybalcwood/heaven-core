from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Heaven Core is Live"}

@app.post("/boot")
def boot_host():
    subprocess.call(["bash", "host_boot.sh"])
    return {"message": "Host boot sequence initiated."}
