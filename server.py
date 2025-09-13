import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

FOLDER = "skladiste"
os.makedirs(FOLDER, exist_ok=True)

@app.post("/otpremi")
async def otpremi_fajl(fajl: UploadFile = File(...)):
    putanja = os.path.join(FOLDER, fajl.filename)
    with open(putanja, "wb") as f:
        sadrzaj = await fajl.read()
        f.write(sadrzaj)
    return {"poruka": f"Fajl '{fajl.filename}' je uspešno sačuvan."}

@app.get("/preuzmi")
def preuzmi_fajl(ime: str):
    putanja = os.path.join(FOLDER, ime)
    if not os.path.exists(putanja):
        raise HTTPException(status_code=404, detail="Fajl ne postoji")
    return FileResponse(putanja, filename=ime)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
