from fastapi import FastAPI, UploadFile, File
import tempfile

from validator.engine import run_validator

app = FastAPI(title="SAF-T PreCheck Validator")

@app.get("/")
def health():
    return {"status": "SAF-T PreCheck Validator is running"}

@app.post("/validate")
async def validate_saft(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".xml"):
        return {"error": "Fișierul trebuie să fie XML SAF-T"}

    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    results = run_validator(tmp_path)

    return {
        "filename": file.filename,
        "results": results
    }
