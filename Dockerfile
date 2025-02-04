# Author: Zin Lin Htun
# Use Ubuntu 24 Image
FROM ubuntu:latest

# Set environment variables
ENV ROS_DISTRO jazzy
ENV DEBIAN_FRONTEND noninteractive

# Install required system dependencies
RUN apt update && apt install -y \
    curl \
    gnupg2 \
    lsb-release \
    software-properties-common

# Add ROS 2 repository and key
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | tee /usr/share/keyrings/ros-archive-keyring.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null && \
    apt update

# Install ROS 2 and development tools
RUN apt install -y \
    ros-jazzy-ros-base \
    python3-vcstool \
    python3-colcon-common-extensions \
    build-essential\
    git

# Set up entire workspace
WORKDIR /annex-asdmt-ws
COPY . /annex-asdmt-ws

# Remove any existing CMake cache files before building -> Docker issues locally
RUN rm -rf build/ install/ log/

# Import ROS dependencies (if ros2.repos exists)
RUN if [ -f ros2.repos ]; then vcs import src < ros2.repos; fi

# Fix for sourcing ROS before colcon build
SHELL ["/bin/bash", "-c"]

# Source ROS and build the workspace
RUN source /opt/ros/jazzy/setup.bash && colcon build --symlink-install --event-handlers console_direct+

# Set up entrypoint
CMD ["bash", "-c", "source install/setup.bash && exec bash"]