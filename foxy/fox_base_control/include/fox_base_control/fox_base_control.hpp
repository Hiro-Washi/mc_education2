
#paragma once

#include <memory> // メモリ管理を自動でやってくれるスマートポインタ―というのを使うために
#include <functional> // std::bindを使う。関数の引数を固定化し、限定的な関数を作り出せる
#include <chrono> // 処理時間の計測の時間単位で便利
#include <vector> // listの扱いが厄介なため行列のデータ処理にvectorを使うよ
//#include <algorithm> // std::find関数を使うため
#include <math.h>

#include "rclcpp/rclcpp.hpp"
#include "rclcpp/qos.hpp"
#include "rclcpp/time.hpp"
#include "tf2.hpp" //!!!
#include "std_msgs/msg/float64.hpp"
#include "nav_msgs/msg/odometry.hpp"
#include "geometry_msgs/msg/twist.hpp"

// namespase
// 他で同じ名前のクラスや関数・変数が定義されていてもそれとの衝突が避けられる
// 大規模なパッケージ作成で使うといいかも
namespace fox_base_control
{
// クラスノード
class FoxBaseControl : public rclcpp::Node
{
private:
  // 型のエイリアス
  using Float64 = std_msgs::msg::Float64;
  using Twist = geometry_msgs::msg::Twist;
  using Odometry = Geometry_msgs::msg::Odometry;

  rclcpp::Qos twist_qos(1);
  // Topic Publisher
  rclcpp::Publisher<Twist>::SharedPtr twist_pub; //!! .cppでautoでよくね
  // Topic Subsctiber
  rclcpp::Subscription<Odometry>::SharedPtr odom_sub;
  // Custom Sub
  rclcpp::Subscription<Float64>::SharedPtr translate_sub;
  rclcpp::Subscription<Float64>::SharedPtr rotate_sub;
  

public:
  //MINIMAL_COMP_PUBLIC

  explicit FoxBaseControl();

  // variables
  double target_time = 0.0;
  double current_deg = 0.0;
  double target_deg = 0.0;
  double sub_target_deg = 0.0;
  double remain_deg = 0.0;
  Twist twist_value = 0.0;
  std::vector<double> quaternion[4];
  std::vector<double> current_euler[3];
  //rclcpp::Rate loop_rate

  // functions
  void createSubs();
  //void dist(const std::shared_ptr<Float64> msg);
  //void rotateSrv(const std::shared_ptr<Float64> msg);
  void odomCB(const Odometry::SharedPtr msg);
  void pubTwist();
  void translateDist(Float64 dist, Float64 speed = 0.2);
  void rotateAngle(Float64 deg, Float64 speed = 0.2);


}; // class
} // namespace

//RCLCPP_COMPONENTS_REGISTER_NODE(rclcpp_server_tmp::foxCommTmpServer)

