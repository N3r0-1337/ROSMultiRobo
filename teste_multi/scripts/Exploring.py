#! /usr/bin/env python3

import ros
import rospy

from AStar import Bot

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

rospy.init_node('movebase_core_client')

bots = [Bot("/robot1/move_base", 1),
        Bot("/robot2/move_base", 2),
        Bot("/robot3/move_base", 3)]

pos : [(float, float)] = [(-6.6, -1.5),
                          (-1.2, 4.3),
                          (6.2, 0.7)
                          ]
for i in range(3):
    bots[i].MoveBaseGoal(pos[i])
