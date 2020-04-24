import os

import pytest
import numpy as np
import cv2

from pupil_detectors import Detector2D

test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")


class TestPupilDetectors:

    @pytest.fixture()
    def detector_2d(self):
        """ 2D detector instance. """
        return Detector2D()

    @pytest.fixture()
    def gray_img(self):
        """ Gray eye image. """
        img = cv2.imread(os.path.join(test_data_dir, "eye.png"))
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def test_detector_2d(self, detector_2d, gray_img):
        """ Test 2D detector. """
        result = detector_2d.detect(gray_img)

        np.testing.assert_allclose(result["confidence"], 0.99)
        np.testing.assert_allclose(result["diameter"], 45.361183)
        np.testing.assert_allclose(result["location"], (123.453926, 69.000359))
