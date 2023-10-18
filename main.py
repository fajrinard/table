from fastapi import FastAPI
from fastapi.responses import FileResponse
from table import *
import uvicorn

app = FastAPI(title='Ardx Togel API', version='1.0.0')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def read_root():
    data = {
        'message': "Welcome to Ardx Togel API"
    }
    return data

@app.get("/table-sgp/")
def read_items():
    data = refresh_sgp()
    return {'result': data, 'message': 'Table scraped by Ardmosphere. Made with <3'}

@app.get("/table-hk/")
def read_items():
    data = refresh_hk()
    return {'result': data, 'message': 'Table scraped by Ardmosphere. Made with <3'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
