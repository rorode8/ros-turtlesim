#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

PI = 3.1415926535897


class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(100)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    
    def move2goal(self):
        """Moves the turtle to the goal."""
        goal_pose = Pose()

        # Get the input from the user.
        goal_pose.x = float(input("Set your x goal: "))
        goal_pose.y = float(input("Set your y goal: "))

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = input("Set your tolerance: ")

        vel_msg = Twist()

        

        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        
        

        #rotate
        angular_speed = 30*2*PI/360
        

        print(self.pose.theta)

        vel_msg.angular.z = abs(angular_speed)

        ang = 0
        if(self.pose.y > goal_pose.y):
            ang =  -PI/2
        else:
            ang = PI/2

        while(abs(self.pose.theta - ang)>distance_tolerance):
            print(1)
            print(self.pose.theta)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            

        #stop
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        vel_msg.linear.x = abs(1.5)

        while abs (self.pose.y - goal_pose.y)>distance_tolerance:
            print(2)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        
        

        clockwise = True

        if clockwise:
            vel_msg.angular.z = -abs(angular_speed)
        else:
            vel_msg.angular.z = abs(angular_speed)

        
        if(self.pose.x >= goal_pose.x):
            ang = PI
        else:
            ang = 0

        while(abs(self.pose.theta - ang)>distance_tolerance):
            print(3)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


        #Forcing our robot to stop
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        

        #y axis
        vel_msg.linear.x = abs(1.5)

        while abs(self.pose.x - goal_pose.x)>distance_tolerance:
            dis = abs(self.pose.x - goal_pose.x)

            print(4)
            print(str(dis))

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


        

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        

        # If we press control + C, the node will stop.
        #rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass