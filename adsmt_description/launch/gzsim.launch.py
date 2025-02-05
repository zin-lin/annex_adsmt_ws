"""
Author: Zin Lin Htun
class: Launch
"""


# import necessaries
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# import descriptions
from launch_ros.actions import Node
import xacro

PKG_SRC = 'adsmt_description'
MODELS_SRC = 'urdf'
WORLDS_SRC = 'worlds'
ROBOT = 'adsmt.xacro'
CONES_TEST_WORLD = 'cones_test.sdf'

def generate_launch_description():
    robot_name = "ads-mt"
    name_package = "adsmt_description"

    # full file path
    robot_file = os.path.join(get_package_share_directory(name_package), PKG_SRC, MODELS_SRC, ROBOT)

    # full world paths
    cones_test_world = os.path.join(get_package_share_directory(name_package), WORLDS_SRC, CONES_TEST_WORLD)

    # gazebo launcher
    gazebo_ros_launch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('ros_gz_sim'),
                                                                   'launch',  'gz_sim.launch.py'))
    # gazebo launch empty world
    gazebo_launch_des = IncludeLaunchDescription(gazebo_ros_launch,
                                                 launch_arguments={'gz_args':[f'-r -v -v4 {cones_test_world}'],
                                                                   'on_exit_shutdown':'true'}.items())
    robot_xml = xacro.process_file(robot_file).toxml()
    # gazebo node
    spawn_model_gazebo = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', robot_name,
            '-topic', 'robot_description'
        ],
        output='screen'
    )

    # use robot state publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_xml,
                     'use_sim_time': True
                     }],
    )

    # get bridge
    bridge_file = os.path.join(get_package_share_directory(name_package),'adsmt_description',"parameters", "bridge_parameters.yaml")

    # bridge command
    gazebo_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=["--ros-args",
                   '-p',f'config_file:={bridge_file}',
                   ],
        output='screen',
    )

    # empty launch_des
    launch_description = LaunchDescription()

    # gazebo launch
    launch_description.add_action(gazebo_launch_des)

    # launch extra components
    launch_description.add_action(spawn_model_gazebo)
    launch_description.add_action(robot_state_publisher)
    launch_description.add_action(gazebo_bridge)

    return launch_description


