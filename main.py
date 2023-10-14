from fastapi import FastAPI
from fastapi.responses import FileResponse
from table import *
import uvicorn

app = FastAPI(title='Ardx Lyrics API', version='1.0.0')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def read_root():
    data = {
        'message': "Welcome to Ardx Lyrics API"
    }
    return data

@app.get("/table/")
def read_items():
    data = refresh()
    return {'result': data, 'message': 'Table scraped by Ardmosphere. Made with <3'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)