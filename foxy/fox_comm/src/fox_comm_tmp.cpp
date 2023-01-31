
// 本来はヘッダーファイルの方でクラス、メソッド、変数の宣言をする

// C++11ではenum classという列挙型が新たに導入

#include <memory> // メモリ管理を自動でやってくれるスマートポインタ―というのを使うために
#include <functional> // std::bindを使う。関数の引数を固定化し、限定的な関数を作り出せる
#include <chrono> // 処理時間の計測に使う.C++14の一つの機能
#include <vector> // listの扱いが厄介なため行列のデータ処理にvectorを使うよ
#include <algorithm> // std::find関数を使うため

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "rclcpp/time.hpp"

// カスタムメッセージ
#include "fox_test_msgs/msg/my_message.hpp"
#include "fox_test_msgs/srv/service_test.hpp"
#include "fox_test_msgs/action/action_test.hpp"

using namespace std::chrono_literals; // 時間単位に便利
using std::placeholders::_1;
using std::placeholders::_2;

namespace rclcpp_server_tmp // 他で同じ名前のクラスや関数・変数が定義されていてもそれとの衝突が避けられる
{
// クラスノードの作成
class FoxCommTmpServer : public rclcpp::Node()
{
private: //（本当はヘッダーに書けばいい内容）
  // エイリアス
  using MyMsg = fox_test_msgs::msg::MyMessage;
  using SrvTest = fox_test_msgs::srv::ServiceTest;
  using AcTest = fox_test_msgs::action::ActionTest;
  //using AcTestCGH = rclcpp_action::ClientGoalHandle<AcTest>;

  // サーバー達の宣言---
  // Topic Publisher
  rclcpp::Publisher<MyMsg> mymsg_pub;
  // Service Server
  rclcpp::Service<SrvTest> srv_test;
  // Action Server
  //rclcpp_action::Server<ActionTest> ac_test;
  // -----------------

  void handleService_(
    const std::shared_ptr<MyMsg::Request> request,
    const std::shared_ptr<MyMsg::Response> response
  );

public:
  explicit FoxCommTmpServer(): Node("")

}; // class
} // namespace

//RCLCPP_COMPONENTS_REGISTER_NODE(rclcpp_server_tmp::foxCommTmpServer)

int main(int argc, char* argv[])
{
  // rclcppを初期化
  rclcpp::init(argc, argv);
  // ノード名を指定したノード型へのShared_ptrの生成
  //　明示的にstd::shared_ptr<rclcpp::Node> node = ~<~>("~")でもよし。長いからautoで良いと思う
  // ノード名はクラスのコンストラクタで宣言してるので端折ってる
  auto node = rclcpp::Node::make_shared<rclcpp_server_tmp::FoxCommTmpServer>();
  //　ロギング出力
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready for **fox_comm_tmp_server**");
  // nodeを待機状態に
  // 直接、rclcpp::spin(std::make_shared<FoxCommTmpServer>());のように書いてもよし
  rclcpp::spin(node);
  // ノードを閉じる
  rclcpp::shutdown();
}