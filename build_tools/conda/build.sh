echo "Building"

export OPENCV_INCLUDE_DIR="${PREFIX}/include/opencv4"
export OPENCV_LIBRARY_DIR="${PREFIX}/lib"
export EIGEN_INCLUDE_DIR="${PREFIX}/include/eigen3"
export CERES_INCLUDE_DIR="${PREFIX}/include"

$PYTHON setup.py install --single-version-externally-managed --record=record.txt  # Python command to install the script.
