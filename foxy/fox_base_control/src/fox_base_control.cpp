
#include "fox_base_control.hpp"

using namespace std::chrono_literals; // 時間単位に便利
using namespace fox_base_control;
using std::placeholders::_1;
using std::placeholders::_2;

FoxBaseControl::FoxBaseControl(): Node("fox_base_control"){
  twist_pub = this->create_publisher<geometry_msgs::msg::Twist>(
    "/cmd_vel", twist_qos
  )
  odom_sub = this->create_subscription<nav_msgs::msg::Odometry>(
    "/odom", std::bind(&FoxBaseControl::odomCB, this, _1)
  )
}

FoxBaseControl::createNodes(){
  this->create_subscription<Float64>(
    "/teleop2/translate", std::bind(&FoxBaseControl::translateDist, this, _1)
  )
  this->create_subscription<Fl 5vmjnoat64>(
    "/teleop2/ratate", std::bind(&FoxBaseControl::rotateDist, this, _1)
  )
}

FoxBaseControl::odomCB(const Odometry::SharedPtr msg){
  quaternion = {
    msg->pose.pose.orientation.x,
    msg->pose.pose.orientation.y,
    msg->pose.pose.orientation.z,
    msg->pose.pose.orientation.w
  }
  current_euler = 
    tf2.transformations.euler_from_quaternion(quaternion)
    
}


int main(int argc, char* argv[])
{
  // rclcppを初期化
  rclcpp::init(argc, argv);
  // ノード名を指定したノード型へのShared_ptrの生成
  auto node = rclcpp::Node::make_shared<FoxBaseControl>();
  //　ロギング出力
  RCLCPP_INFO(rclcpp::get_logger(), "Ready for **fox_base_control**");
  // nodeを待機状態に
  rclcpp::spin(node);
  // ノードを閉じる
  rclcpp::shutdown();
}