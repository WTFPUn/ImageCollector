# Data Collector

## Description
This is a simple data collector from ip-camera or other camera device

## Installation

1. Install python3 with pip
2. create virtual environment by running the following command
```bash
python -m venv venv
```
3. activate virtual environment by running the following command
```bash
.\venv\Scripts\activate
```
4. install library with pip by running the following command
```bash
pip install -r requirements.txt
```

## Setup
to use this program, you need to connect your camera device to your computer. 
**Note**: if you are not using ip camera. program will use your default camera.
<br>
for everytime when use this program, you need to activate virtual environment by running the following command
```bash
.\venv\Scripts\activate
```
or check virtual environment is activated by checking `(venv)` in the terminal
```bash
(venv) C:\Users\user\path\to\project>
```



## Usage
To use this program, you can run the following command
```bash
python main.py <outputfolder> <number_of_images> --videro_stream <video_stream> --interval <interval>
```

### program arguments
| Argument | Description | Example |
| --- | --- | --- |
| outputfolder | folder to save the images, add `.` to save in current directory. program will create directory if is does not exist | `./images` |
| duration | duration to collect images(seconds) | `100` |
| video_stream(optional) | video stream url(rtsp) | `rtsp://<username>:<pass>@<ip>:<port>/path` |
| interval(optional) | interval to collect images(seconds) default is `1` | `5` |

### Example
```bash
python main.py ./images 100 --video_stream rtsp://admin:admin@
```

the program will check directory `./images` and create if it does not exist. then program will collect image for 100 seconds and save in `./images` directory.But if we put `--interval 10` program will collect image every 10 seconds instead of 1 second.
