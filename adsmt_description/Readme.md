# Hardware Directory

- use `designs` under `adsmt_description/urdf` for simulation
- use `designs-raw` for printing

## Set up
- `ROS2 Jazzy` is required refer to [ROS2 Jazzy Jalisco installation](https://docs.ros.org/en/jazzy/Installation.html)
- `Gazebo Harmonic` binary version is needed, refer to [Gazebo Harmonic binary installation](https://gazebosim.org/docs/harmonic/install_ubuntu/) for standalone cases
- use gazebo harmonics ros installation  
    ```shell
    sudo apt update
    sudo apt ros-jazzy-ros-gz
    ```

## Building
- jazzy builds upon `colcon`
  - ```shell
    colcon build --packages-select adsmt_description --symlink-install
    ```
    - Use `--symlink-install` for dealing with autonomous sourcing
- source
  - ```shell
    source install/local_setup.bash
    ```
  - Using `symlink` one needs to only source once, if needs rebuilding one can just run the program directly after build without the need of sourcing again.

## Running RVIZ
- `RviZ` is used as a markup viewer
  - ```shell
    ros2 launch adsmt_description display.launch.py
    ```
    
## Running Gazebo Simulation Endpoint
- `Gazebo` is a realistic simulation with mass, inertia and material forces added.
  - ```shell
    ros2 launch adsmt_description gzsim.launch.py
    ```

## Changelog
- `[Feb 1, 2025]` added RVIZ viewing capabilities
- `[Feb 3, 2025]` added Gazebo simulation successfully
