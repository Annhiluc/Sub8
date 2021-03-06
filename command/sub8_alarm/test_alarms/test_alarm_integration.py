#!/usr/bin/env python

PKG = 'sub8_alarm'
NAME = 'test_alarm'

import sys
import rospy
import rostest
import unittest
import numpy as np
from sub8_msgs.msg import Thrust, ThrusterCmd
from sub8_msgs.srv import FailThruster
from geometry_msgs.msg import WrenchStamped, Wrench, Vector3
from sub8_ros_tools import wait_for_subscriber
import time


class TestAlarmIntegration(unittest.TestCase):
    def setUp(self):
        self.last_thrust_cmd = None
        self.called = False

    def thrust_callback(self, msg):
        self.called = True
        self.last_thrust_cmd = msg

    def test_lose_thruster(self):
        '''Trigger a thruster loss and verify that it is no
            longer used'''
        rospy.Subscriber("/thrusters/thrust", Thrust, self.thrust_callback)
        wrench_pub = rospy.Publisher('/wrench', WrenchStamped, queue_size=1, latch=True)

        thruster_to_fail = 'BRV'

        # TODO: Compress this anymore
        subscribed = wait_for_subscriber('thruster_mapper', 'wrench')
        self.assertTrue(
            subscribed,
            "{} did not not come up in time".format('thruster_mapper')
        )

        # Fail a thruster
        # TODO: Raise if waiting fails
        rospy.wait_for_service('fail_thruster', timeout=5.0)
        fail_thruster_proxy = rospy.ServiceProxy('fail_thruster', FailThruster)
        fail_thruster_proxy(thruster_to_fail)

        time.sleep(0.1)
        wrench_pub.publish(WrenchStamped(
            # The actual force/torque is irrelevant, we still send a 0 command for every active thruster
            wrench=Wrench(
                force=Vector3(10.0, 10.0, 10.0),
                torque=Vector3(10.0, 10.0, 10.0)
            )
        ))

        time.sleep(0.1)
        self.assertTrue(self.called)
        self.assertIsNotNone(self.last_thrust_cmd, msg="Never got thrust command after issuing wrench")
        names = []
        for cmd in self.last_thrust_cmd.thruster_commands:
            names.append(cmd.name)

        self.assertNotIn(thruster_to_fail, names,
            msg="Thruster mapper continued to issue commands to {} after thruster loss alarm".format(thruster_to_fail))

    @unittest.skip("Not ready")
    def test_kill(self):
        '''Test a 'kill' alarm'''
        pass

    def test_unkill(self):
        '''Test an unkill alarm'''
        pass


if __name__ == '__main__':
    rospy.init_node(NAME, anonymous=True)
    rostest.rosrun(PKG, NAME, TestAlarmIntegration, sys.argv)