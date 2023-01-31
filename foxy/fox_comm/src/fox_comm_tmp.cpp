
// �{���̓w�b�_�[�t�@�C���̕��ŃN���X�A���\�b�h�A�ϐ��̐錾������

// C++11�ł�enum class�Ƃ����񋓌^���V���ɓ���

#include <memory> // �������Ǘ��������ł���Ă����X�}�[�g�|�C���^�\�Ƃ����̂��g�����߂�
#include <functional> // std::bind���g���B�֐��̈������Œ艻���A����I�Ȋ֐������o����
#include <chrono> // �������Ԃ̌v���Ɏg��.C++14�̈�̋@�\
#include <vector> // list�̈��������Ȃ��ߍs��̃f�[�^������vector���g����
#include <algorithm> // std::find�֐����g������

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "rclcpp/time.hpp"

// �J�X�^�����b�Z�[�W
#include "fox_test_msgs/msg/my_message.hpp"
#include "fox_test_msgs/srv/service_test.hpp"
#include "fox_test_msgs/action/action_test.hpp"

using namespace std::chrono_literals; // ���ԒP�ʂɕ֗�
using std::placeholders::_1;
using std::placeholders::_2;

namespace rclcpp_server_tmp // ���œ������O�̃N���X��֐��E�ϐ�����`����Ă��Ă�����Ƃ̏Փ˂���������
{
// �N���X�m�[�h�̍쐬
class FoxCommTmpServer : public rclcpp::Node()
{
private: //�i�{���̓w�b�_�[�ɏ����΂������e�j
  // �G�C���A�X
  using MyMsg = fox_test_msgs::msg::MyMessage;
  using SrvTest = fox_test_msgs::srv::ServiceTest;
  using AcTest = fox_test_msgs::action::ActionTest;
  //using AcTestCGH = rclcpp_action::ClientGoalHandle<AcTest>;

  // �T�[�o�[�B�̐錾---
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
  // rclcpp��������
  rclcpp::init(argc, argv);
  // �m�[�h�����w�肵���m�[�h�^�ւ�Shared_ptr�̐���
  //�@�����I��std::shared_ptr<rclcpp::Node> node = ~<~>("~")�ł��悵�B��������auto�ŗǂ��Ǝv��
  // �m�[�h���̓N���X�̃R���X�g���N�^�Ő錾���Ă�̂Œ[�܂��Ă�
  auto node = rclcpp::Node::make_shared<rclcpp_server_tmp::FoxCommTmpServer>();
  //�@���M���O�o��
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready for **fox_comm_tmp_server**");
  // node��ҋ@��Ԃ�
  // ���ځArclcpp::spin(std::make_shared<FoxCommTmpServer>());�̂悤�ɏ����Ă��悵
  rclcpp::spin(node);
  // �m�[�h�����
  rclcpp::shutdown();
}