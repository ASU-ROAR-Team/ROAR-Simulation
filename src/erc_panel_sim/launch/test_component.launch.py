# ═══════════════════════════════════════════════════════════
# test_component.launch.py
#
# PURPOSE:
#   Launch a single URDF component in isolation so you can
#   visualize and verify it in RViz before assembling the
#   full panel. Use this for every component we build.
#
# WHAT IT STARTS:
#   1. robot_state_publisher  — reads the URDF and publishes
#                               the TF transform tree so RViz
#                               knows where every link is
#   2. joint_state_publisher_gui — gives you sliders to move
#                               any revolute joints manually
#   3. rviz2                  — 3D visualizer
#
# HOW TO USE:
#   ros2 launch erc_panel_sim test_component.launch.py
# ═══════════════════════════════════════════════════════════

import os

# LaunchDescription is the container that holds all the nodes
# we want to start. Every launch file must return one.
from launch import LaunchDescription

# Node is how we tell ROS 2 to start a single executable
from launch_ros.actions import Node

# get_package_share_directory resolves the path to our
# installed package — works regardless of where the
# workspace lives on disk
from ament_index_python.packages import get_package_share_directory

# xacro processes our .urdf.xacro file and expands all
# macros and properties into a plain URDF XML string
import xacro


def generate_launch_description():

    # ── STEP 1: Find the package ─────────────────────────
    # pkg will be something like:
    # /home/misara/panel3_ws/install/erc_panel_sim/share/erc_panel_sim
    pkg = get_package_share_directory('erc_panel_sim')

    # ── STEP 2: Process the xacro file ───────────────────
    # Build the full path to the component we want to test.
    # Change 'panel_base.urdf.xacro' here to test other components later (e.g. 'lever_switch.urdf.xacro')
    urdf_file = os.path.join(
        pkg,
        'urdf',
        # 'components',
        'panel.urdf.xacro'
    )
    # This was changed by chatgpt

    # process_file() runs xacro and returns the expanded URDF.
    # toxml() converts it to a string that ROS 2 can read.
    robot_desc = xacro.process_file(urdf_file).toxml() #had an error here, reading the file directly "as string" instead of using process_file() caused the error, fixed now

    # ── STEP 3: Define the nodes to launch ───────────────
    return LaunchDescription([

        # NODE 1: robot_state_publisher
        # Reads robot_description and publishes /tf and /tf_static.
        # /tf is the transform tree — it tells every other node
        # where each link is in 3D space relative to the world.
        # Without this, RViz cannot draw the model.
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                # Pass the URDF string as a parameter.
                # robot_state_publisher reads this on startup.
                'robot_description': robot_desc
            }]
        ),

        # NODE 2: joint_state_publisher_gui
        # Opens a window with sliders for every revolute joint.
        # When you move a slider it publishes to /joint_states,
        # which robot_state_publisher uses to update the TF tree.
        # For panel_base this has no effect (all joints are fixed)
        # but it becomes useful once we add lever and rotary joints.
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        # NODE 3: rviz2
        # The 3D visualizer. Reads /tf and /robot_description
        # to draw the model. Opens with a blank config —
        # you need to set Fixed Frame and add RobotModel
        # display manually the first time.
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),

    ])