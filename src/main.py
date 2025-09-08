from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from picamera2 import Picamera2

picam = Picamera2()
picam.start()

app = FastAPI()

# Serve static files (frontend)
static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/capture")
def capture():

    # Capture image to memory
    img = picam.capture_array()
    import cv2
    _, buf = cv2.imencode('.jpg', img)
    return Response(content=buf.tobytes(), media_type="image/jpeg")


@app.get("/")
def root():
	return FileResponse(os.path.join(static_dir, "index.html"))
