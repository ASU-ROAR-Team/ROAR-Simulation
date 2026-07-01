import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():

    pkg = get_package_share_directory('erc_panel_sim')
    plate_pkg = get_package_share_directory('plate_description')
    
    panel_urdf_path = os.path.join(pkg, 'urdf', 'panel.urdf.xacro')
    plate_urdf_path = os.path.join(plate_pkg, 'urdf', 'plate.xacro')

    panel_desc = xacro.process_file(panel_urdf_path).toxml()
    plate_desc = xacro.process_file(plate_urdf_path).toxml()

    return LaunchDescription([

        # 1. Start Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
            ),
            launch_arguments={'gz_args': '-r empty.sdf'}.items()
        ),

        # 2. Panel State Publisher only — RViz uses this
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': panel_desc}],
            output='screen'
        ),

        # 3. Joint State Publisher
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        # 4. RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),

        # 5. Spawn Panel
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-topic', 'robot_description',
                '-name', 'panel',
                '-z', '0.5'
            ],
            output='screen'
        ),

        # 6. Spawn Plate directly — no state publisher needed
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-string', plate_desc,
                '-name', 'free_plate',
                '-x', '0.055', '-y', '-0.1', '-z', '0.6'
            ],
            output='screen'
        )
    ])