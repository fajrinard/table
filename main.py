from fastapi import FastAPI
from fastapi.responses import FileResponse,RedirectResponse
from table import *
import uvicorn, json

app = FastAPI(title='Ardx Togel API', version='1.3')

msg = "Table scraped by Ard. coded with <3"

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def read_root():
    data = {
        'message': "Welcome to Ardx Togel API"
    }
    return data

@app.get("/table-cam/")
def read_items():
    data = refresh_result_cam()
    return {'result': data, 'message': msg}

@app.get("/table-sgp/")
def read_items():
    data = refresh_result_sgp()
    return {'result': data, 'message': msg}

@app.get("/table-hk/")
def read_items():
    data = refresh_result_hk()
    return {'result': data, 'message': msg}

@app.get("/table-sdy/")
def read_items():
    data = refresh_result_sdy()
    return {'result': data, 'message': msg}

@app.get("/table-tw/")
def read_items():
    data = refresh_result_tw()
    return {'result': data, 'message': msg}

@app.get("/table-chn/")
def read_items():
    data = refresh_result_chn()
    return {'result': data, 'message': msg}

@app.get("/table-macau/")
def read_items():
    data = refresh_result_macau()
    return {'result': data, 'message': msg}

@app.get("/live-draw-sgp/")
def read_items():
    data = refresh_livedraw_sgp()
    return {'result': data, 'message': msg}

@app.get("/live-draw-hk/")
def read_items():
    data = refresh_livedraw_hk()
    return {'result': data, 'message': msg}

@app.get("/prediksi-sgp/")
def read_items():
    data = refresh_prediksi_sgp()
    return {'result': data, 'message': msg}

@app.get("/prediksi-hk/")
def read_items():
    data = refresh_prediksi_hk()
    return {'result': data, 'message': msg}

@app.get("/prediksi-sdy/")
def read_items():
    data = refresh_prediksi_sdy()
    return {'result': data, 'message': msg}

@app.get("/togel-hari-ini/")
def read_items():
    data = refresh_result_hariini()
    return {'result': data, 'message': msg}

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
