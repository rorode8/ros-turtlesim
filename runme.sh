cd ~/catkin_ws/src
pause
catkin_create_pkg turtlesim_cleaner geometry_msgs rospy
pause
cd ~/catkin_ws
pause
catkin_make
cd ~/catkin_ws/src/turtlesim_cleaner
pause
mkdir src
pause
cd ~/catkin_ws
pause
catkin_make
pause
chmod u+x ~/catkin_ws/src/turtlesim_cleaner/src/move.py
pause



roscore
pause
rosrun turtlesim turtlesim_node
pause



