# agtech-IoT-camera-demo
A demonstration of an IoT camera, built using a Raspberry Pi

## Materials:
- Raspberry Pi (model [4](https://core-electronics.com.au/raspberry-pi-4-model-b-1gb.html), [5](https://core-electronics.com.au/raspberry-pi-5-model-b-2gb.html) or [Zero 2W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)). 
- [Raspberry pi camera module](https://core-electronics.com.au/raspberry-pi-camera-3.html)
- [Raspberry pi camera cable](https://core-electronics.com.au/flex-cable-for-raspberry-pi-camera-300mm-12.html)

## Setup Instructions

1. **Update your Raspberry Pi OS:**
   ```sh
   sudo apt update
   sudo apt upgrade
   ```

2. **Install system dependencies:**
   ```sh
   sudo apt install python3-picamera2 python3-libcamera python3-pip libcamera-apps
   ```

3. **Clone this repository and enter the folder:**
   ```sh
   git clone <repo-url>
   cd agtech-IoT-camera-demo
   ```

4. **(Optional) Install Python dependencies:**
   If you want to use pip for FastAPI and other packages:
   ```sh
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Running the Server

To run on Raspberry Pi:
```sh
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Then open your browser and go to:
```
http://<raspberrypi-ip>:8000/
```

Press the button to take a photo and view it in the browser.

---
