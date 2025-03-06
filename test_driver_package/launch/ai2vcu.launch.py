import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# import descriptions
from launch_ros.actions import Node


def generate_launch_description():
    # path_planning node
    pp_node = Node(
        package="path_planner_package",
        executable='path_planning',
        output='both',  # both means both log files and terminal
        parameters=[
            {'mode': 1, 'mode_args': 1}
        ],
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
    launch_description.add_action(pp_node)
    launch_description.add_action(vehicle_control_node)
    return launch_description
