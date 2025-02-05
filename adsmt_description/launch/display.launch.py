import os
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg = get_package_share_directory('adsmt_description')
    urdf_file = os.path.join(pkg, 'urdf', 'adsmt.xacro')
    config = os.path.join(pkg, 'rviz', 'config.rviz')

    # Declare the robot_state_publisher node
    robot_pub_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': open(urdf_file).read()
        }]
    )

    # Declare the joint_state_publisher_gui node
    joint_pub_node = launch_ros.actions.Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # Declare the rviz2 node
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
    )

    # Return the launch description
    return launch.LaunchDescription([

        robot_pub_node,
        joint_pub_node,
        rviz_node
    ])
