# External imports
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse, RedirectResponse

# Internal imports
from functions.getGeneratedData import getGeneratedData
from functions.generateData import generate

app = FastAPI()

@app.get("/favicon.ico", status_code=200)
def favicon():
    return None

@app.get('/sanityCheckData')
def sanityCheckData():
    import os

    already_exists = os.path.exists("../data/large_file.json")

    return JSONResponse(
        content={"msg": "Exists" if already_exists == True else "Does not exist"},
        status_code=200
    )

@app.get('/generateData')
def generateData():
    import os

    already_exists = os.path.exists("../data/large_file.json")

    if already_exists == False:
        generate()

    return JSONResponse(
        content={"msg": "Generated"},
        status_code=200
    )

@app.get("/data")
def getData(asBin: str = "false"):
    import os

    already_exists = os.path.exists("../data/large_file.json")

    if already_exists == False:
        return RedirectResponse(
            "/sanityCheckData",
            status_code=301
        )

    encoding = "gzip" if asBin == "true" else "application/json"

    headers = {
        "Content-Encoding": encoding,
    }

    responseContent = getGeneratedData()

    return JSONResponse(
        content=responseContent,
        status_code=200,
        headers=headers
    )

@app.get("/")
def getPlatforms(asBin: str = "false"):
    encoding = "gzip" if asBin == "true" else "application/json"

    headers = {
        "Content-Encoding": encoding,
    }

    return JSONResponse(
        content={"message": "Hello World"},
        status_code=200,
        headers=headers
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000, headers=[("server", "firstproject")])