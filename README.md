# Threaded Screen Recorder (Python)

A high-performance screen recording utility built with Python. This project utilizes the `mss` library for fast frame grabbing and `threading` to ensure smooth recording at 60 FPS without lagging the live preview.

## 🚀 Features
* **Multi-threaded Capture:** Separates the screen grabbing logic from the video writing process to maintain consistent frame rates.
* **Live Preview:** Real-time window showing what is being recorded (scaled for performance).
* **High Performance:** Uses `mss`, which is significantly faster than standard PIL or PyAutoGUI methods.
* **XVID Encoding:** Saves recordings in `.avi` format.

## 🛠️ Prerequisites
Before running the script, ensure you have Python 3.x installed. 

## 📦 Installation

1. Clone the repository:
```bash
git clone [https://github.com/DakshNamdev/python-screen-recorder.git](https://github.com/DakshNamdev/python-screen-recorder.git)
cd screen-recorder
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🖥️ Usage

Simply run the main script:

```bash
python main.py
```

* **Live Preview:** A window named "Live" will appear.
* **Stop Recording:** Press the **'q'** key while the preview window is focused to stop recording and save the file.
* **Output:** The recorded file will be saved as `Recording.avi` in the project directory.

## ⚙️ Configuration

You can adjust the following constants in the code to match your monitor setup:

* `WIDTH` & `HEIGHT`: Set these to your monitor's resolution (default is 1920x1080).
* `fps`: Target frames per second (default is 60.0).
