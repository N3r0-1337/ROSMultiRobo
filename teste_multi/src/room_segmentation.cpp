#include <ros/ros.h>
#include <ros/package.h>

#include <string>
#include <vector>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <cv_bridge/cv_bridge.h>

#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <ipa_building_msgs/MapSegmentationAction.h>

#include <ipa_room_segmentation/dynamic_reconfigure_client.h>


int main(int argc, char **argv){
  ros::init(argc, argv, "client_segmentation_bridge");
  ros::NodeHandle nodeHandle;
}
