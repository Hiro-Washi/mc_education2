
// 本来はヘッダーファイルの方でクラス、メソッド、変数の宣言をする

#include <memory> // メモリ管理を自動でやってくれるスマートポインタ―というのを使うために
#include <chrono> // 処理時間の計測に使う
#include <vector> // listの扱いが厄介なため行列のデータ処理にvectorを使うよ
#include <algorithm> // for std::find

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "rclcpp/time.hpp"

// カスタムメッセージ
#include "fox_test_msgs/msg/my_message.hpp"
#include "fox_test_msgs/srv/service_test.hpp"
#include "fox_test_msgs/action/action_test.hpp"


class Navi2LocationServer : public rclcpp::Node
{
private:


public:

}