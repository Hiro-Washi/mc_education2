
// �{���̓w�b�_�[�t�@�C���̕��ŃN���X�A���\�b�h�A�ϐ��̐錾������

#include <memory> // �������Ǘ��������ł���Ă����X�}�[�g�|�C���^�\�Ƃ����̂��g�����߂�
#include <chrono> // �������Ԃ̌v���Ɏg��
#include <vector> // list�̈��������Ȃ��ߍs��̃f�[�^������vector���g����
#include <algorithm> // for std::find

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "rclcpp/time.hpp"

// �J�X�^�����b�Z�[�W
#include "fox_test_msgs/msg/my_message.hpp"
#include "fox_test_msgs/srv/service_test.hpp"
#include "fox_test_msgs/action/action_test.hpp"


class Navi2LocationServer : public rclcpp::Node
{
private:


public:

}