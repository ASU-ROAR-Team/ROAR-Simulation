cmake_minimum_required(VERSION 2.8.3)

project(roar_simulation)

find_package(catkin REQUIRED
	message_generation
	roscpp
	rospy
	std_msgs
	geometry_msgs
	urdf
	xacro
)


catkin_package(
CATKIN_DEPENDS
	geometry_msgs
	roscpp
	rospy
	std_msgs
)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
