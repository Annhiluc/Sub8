/**
 * Author: Patrick Emami
 * Date: 9/29/15
 *
 */
#ifndef SUB8_TGEN_COMMON_H_
#define SUB8_TGEN_COMMON_H_

#include <string>
#include <Eigen/Dense>

using std::string;
using namespace Eigen;

namespace sub8 {

namespace trajectory_generator {

// Encodes the different planners
// supported by the TGEN with an integer
enum PlannerType { PDST = 1, RRT };

// Number of dimensions in the control space.
// Corresponds to num thrusters used for motion planning
const static int _CSPACE_DIMS = 6;
const static int _SSPACE_DIMS = 13;

// typedef for control vector
typedef Matrix<double, _CSPACE_DIMS, 1> VectorCd;

// typedef for sspace vector
typedef Matrix<double, _SSPACE_DIMS, 1> VectorSd;

// Strings used for logging statements in the TGEN
class Sub8TGenMsgs {
 public:
  // PlannerStatus responses
  static constexpr const char* INVALID_START =
      "Invalid start state or no start state specified";
  static constexpr const char* INVALID_GOAL = "Invalid goal state";
  static constexpr const char* UNRECOGNIZED_GOAL_TYPE =
      "The goal is of a type that a planner does not "
      "recognize";
  static constexpr const char* TIMEOUT =
      "The planner failed to find a solution";
  static constexpr const char* APPROXIMATE_SOLUTION =
      "The planner found an approximate solution";
  static constexpr const char* EXACT_SOLUTION =
      "The planner found an exact solution";
  static constexpr const char* CRASH = "The planner crashed!";

  // Trajectory Validation
  static constexpr const char* REPLAN_FAILED =
      "Current trajectory is blocked-- starting naive replan";
  static constexpr const char* TRAJECTORY_VALIDATED =
      "Current trajectory successfully validated against new traversability "
      "map.";
};
}
}
#endif /* SUB8_TGEN_COMMON */