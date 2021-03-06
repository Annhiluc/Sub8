cmake_minimum_required(VERSION 2.8.3)
project(sub8_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  message_runtime
  rospy
  std_msgs
)

add_message_files(
  DIRECTORY msg
  FILES
  Alarm.msg
  Thrust.msg
  ThrusterCmd.msg
  ThrusterStatus.msg
  Waypoint.msg
  Trajectory.msg
  VelocityMeasurement.msg
  VelocityMeasurements.msg
)

add_service_files(
  DIRECTORY srv
  FILES
  ThrusterInfo.srv
  MotionPlan.srv
  UpdateThrusterLayout.srv
  FailThruster.srv
)

# add_action_files(
#   FILES
#   Action1.action
# )

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)

catkin_package(
    CATKIN_DEPENDS geometry_msgs message_generation rospy std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
