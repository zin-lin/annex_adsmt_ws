import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# import descriptions
from launch_ros.actions import Node


def generate_launch_description():
    # terminal node
    gui_app_node = Node(
        package='control_package',
        executable='app',
        output='screen',

    )

    # vehicle control node
    vehicle_control_node = Node(
        package='vehicle_control_package',
        executable='vehicle_control',
        output='screen',

    )
    # empty launch_des
    launch_description = LaunchDescription()

    # gazebo launch
    launch_description.add_action(gui_app_node)
    launch_description.add_action(vehicle_control_node)
    return launch_description
