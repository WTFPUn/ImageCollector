import cv2
import os
import sys
import pathlib
from typing import TypedDict
from datetime import datetime
import time

import logging

logging.basicConfig(level=logging.DEBUG)


class Config(TypedDict):
    """
    Configuration for the ImageCollector

    path: pathlib.Path
        The directory where images will be stored
        When Program Start to collect, program will create a directory base on the date in `path` directory
    image_polling_interval: int
        The interval in seconds between each image capture. Default is 1 second.
    vcap: cv2.VideoCapture
        The VideoCapture object to capture images from the camera or video stream.
    """

    path: pathlib.Path
    image_polling_interval: int = 1
    vcap: cv2.VideoCapture


class ImageCollector:
    """
    Collects images from a video capture and stores them in a directory.


    """

    def __init__(self, config: Config):
        self.path = config["path"]

        if config["image_polling_interval"] <= 0:
            logging.error("Error: image_polling_interval must be greater than 0.")
            sys.exit()

        self.image_polling_interval = config["image_polling_interval"]

        # test video capture
        if not config["vcap"].isOpened():
            logging.error("Error: Could not open video capture.")
            sys.exit()

        self.vcap = config["vcap"]

        # create the directory if it does not exist (./[path])
        if not os.path.exists(config["path"]):
            os.mkdir(config["path"])

    @staticmethod
    def from_dir(
        path: pathlib.Path, vcap: cv2.VideoCapture, image_polling_interval: int = 1
    ):
        return ImageCollector(
            {
                "path": path,
                "vcap": vcap,
                "image_polling_interval": image_polling_interval,
            }
        )

    def collect(self, duration: int):
        """
        Collect images from the video capture and store them in the directory.

        duration: int
            The duration in seconds to collect images.
        """
        # create a directory for the date with time
        date = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        date_path = self.path / date
        os.mkdir(date_path)

        # wait until user is ready to start
        os.system("pause")

        # collect images
        start_time = time.time()
        while time.time() - start_time < duration:
            ret, frame = self.vcap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            image_path = date_path / f"{time.time()}.jpg"
            cv2.imwrite(str(image_path), frame)
            time.sleep(self.image_polling_interval)
