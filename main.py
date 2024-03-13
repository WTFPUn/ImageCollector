import argparse
from datacollector import ImageCollector
import pathlib
import cv2

# get sys args
argparser = argparse.ArgumentParser()
argparser.add_argument(
    "path", type=str, help="The path to the directory to store images."
)
argparser.add_argument(
    "duration", type=int, help="The duration in seconds to collect images."
)
# add optional video stream argument
argparser.add_argument("--video_stream", type=str, help="The video stream URL.")

argparser.add_argument("--interval", type=int, help="The image polling interval.")

# example usage: python main.py /path/to/store/images 10 --video_stream rtsp://admin:punkengmak7745@ip/Streaming/Channels/1

args = argparser.parse_args()


imageCollector = ImageCollector.from_dir(
    pathlib.Path(args.path),
    cv2.VideoCapture(args.video_stream if args.video_stream else 0),
    args.interval if args.interval else 1,
)


imageCollector.collect(args.duration)
