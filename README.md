# Panel Simulation Workspace (`panel3_ws`)

A ROS 2 Humble workspace containing the 3D meshes, URDF/XACRO descriptions, and simulation setups for a control panel assembly and its associated rotary switches.

---

## 📂 Workspace Structure

This workspace is split into distinct, modular packages:

* **`panel_body_description`**: Contains the primary 3D meshes, materials, and XACRO configuration files for the main panel housing structure.
* **`switch_description`**: Contains the URDF, meshes, and definitions for the modular rotary controls and switches mounted on the panel.
* **`erc_panel_sim`**: The main simulation package responsible for orchestration, launching environments, and tying the descriptions together.

---

## 🛠️ Prerequisites & Dependencies

Before building, ensure you have the core ROS 2 Humble desktop packages and joint state tools installed:

```bash
sudo apt update
sudo apt install ros-humble-desktop ros-humble-joint-state-publisher-gui ros-humble-xacro

```

---

## 🚀 Building the Workspace

To compile the packages, navigate to your workspace root and build using `colcon`:

### Build Everything

```bash
cd ~/panel3_ws
colcon build

```

### Build a Specific Package (e.g., Panel Body)

If you are iteratively tweaking meshes or URDF offsets, you can speed up build times by targeting just that package:

```bash
colcon build --packages-select panel_body_description

```

---

## 📊 Launching & Simulation

Always remember to source the workspace environment after building to register the packages and nodes.

### To Launch the Full Panel Simulation Component:

```bash
source /opt/ros/humble/setup.bash
source ~/panel3_ws/install/setup.bash
ros2 launch erc_panel_sim test_component.launch.py

```

```

```