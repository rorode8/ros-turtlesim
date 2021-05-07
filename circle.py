#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
import turtle
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
theta = 0

def poseCallback(pose_message):
    global x
    global y
    global z
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def orientate (xgoal, ygoal):
    
	global x
	global y
	global theta

	velocity_message = Twist()
	cmd_vel_topic = '/turtle1/cmd_vel'

	while(True):
		ka = 1.0
		desired_angle_goal = math.atan2(ygoal-y+0.00001, xgoal-x+0.0001)
		
		
		
	#	if desired_angle_goal < 0:
	#		desired_angle_goal = desired_angle_goal + 2*math.pi
	#		dtheta = desired_angle_goal - theta
			#if dtheta >3.14:
			#	desired_angle_goal = desired_angle_goal + math.pi
			#	dtheta = desired_angle_goal - abs(theta)
				
	#		print ('theta=', dtheta)			
			#print ('new_angle=', desired_angle_goal)
		#else:
			
		desired_angle_goal = desired_angle_goal 
		dtheta = desired_angle_goal - theta	
		#print ('new_angle=', theta)


		#if abs(desired_angle_goal - theta) < abs((desired_angle_goal + 2*math.pi) - theta):	
		#	dtheta = desired_angle_goal - theta
		#	print ('dtheta=', dtheta)
		#else
		#	dtheta = desired_angle_goal + 2*math.pi - theta
		#	print ('dtheta=', dtheta)        
		#
		if (abs(dtheta) < 0.0005):
			print ('angle', theta*360.00/6.2831, 'reached')
			time.sleep(1)
			break
		
		#if dtheta > 3.14:
		#	angular_speed = 0.1 * dtheta
		#else:
		angular_speed = ka * dtheta

		velocity_message.linear.x = 0.0
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y)

        
def go_to_goal (xgoal, ygoal):
	    	
	global x
	global y
	global theta

	velocity_message = Twist()
	cmd_vel_topic = '/turtle1/cmd_vel'

         
	while(True):

		ka = 5.0
		desired_angle_goal = math.atan2(ygoal+0.01-y, xgoal+0.01-x)
		#print ('desired_angle=', desired_angle_goal)

		if (desired_angle_goal < 0.0):	
			desired_angle_goal = desired_angle_goal + 6.2831
			#print ('new_angle=', desired_angle_goal)
		else:
			desired_angle_goal = desired_angle_goal	
			#print ('new_angle=', desired_angle_goal)

		dtheta = desired_angle_goal-theta
		#print ('dtheta=', dtheta)        
		angular_speed = ka * (dtheta)	
		

		if (abs(angular_speed) < 0.5):	
			angular_speed = angular_speed
		else:
			angular_speed = 0.0

		kv = 1.0				
		distance = abs(math.sqrt(((xgoal-x)*2)+((ygoal-y)*2)))
		linear_speed = kv * distance

		if (distance < 0.1):
		    print ('point (', x, ',',  y, ') reached')
		    time.sleep(1)
		    break        

		velocity_message.linear.x = linear_speed
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y)

        

if _name_ == '_main_':
	try:

		rospy.init_node('turtlesim_motion_pose', anonymous = True)

		cmd_vel_topic = '/turtle1/cmd_vel'
		velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

		position_topic = "/turtle1/pose"
		pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)


		n = 40
		for i in range(1, n+1):
			calc_x = math.cos(i*(360/n)*math.pi/180)*5+5
			calc_y = math.sin(i*(360/n)*math.pi/180)*5+5
			print(calc_x)
			print(calc_y)
			orientate(calc_x, calc_y)
			#time.sleep(0.5)
			go_to_goal(calc_x, calc_y)
			#time.sleep(0.5)	
		


	except rospy.ROSInterruptException:        
		pass
