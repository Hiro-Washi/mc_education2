#!/usr/bin/env python3
#-*-cording:utf-8-*-

# Python��ROS2�N���C�A���g���C�u����
import rclpy
# rclpy��Node�Ƃ����e�N���X�����p
from rclpy.node import Node
# rclpy��Clock�֐����g����rospy.sleep()�݂����Ȃ��Ƃ��ł���悤�ɂ���
from rclpy.clock import Clock
# �A�N�V�����T�[�o�[�𐶐����邽�߂Ɏg��
from rclpy.action import ActionServer

# ���상�b�Z�[�W�̗p��
from fox_test_msgs.msg import MyMessage
# ����T�[�r�X���b�Z�[�W�̗p��
from fox_test_msgs.srv import ServiceTest, Service
# ����A�N�V�������b�Z�[�W�̗p��
from fox_test_msgs.action import ActionTest



# Node��e�N���X�Ƃ��āAFoxCommTmp�Ƃ����q�N���X��錾�i�N���X�p���j
# Node�N���X�̌p���ɂ��ANode�N���X�֗̕��Ȋ֐����q�N���X���ŗ��p�ł���
class FoxCommTmp(Node):
  # �w�薼�̃m�[�h�̐���
  super().__init__('fox_comm_tmp_server')
  # �R���X�g���N�^�̐����i���̃N���X�����s����Ƃ��ɂ������e�����������j
  def __init__(self):
    # ������
    
    # TopicSubscriber�̐錾/����
    
    # ServiceServer
    
    # ActionServer��
    self._acserver = ActionServer(self, ActionTest, 'action_test',
                                  self.actionCallback)
    
    
def actionCallback(self, goal_hundle):
  self.get_logger().info('Executing goal...')
  result = ActionTest.Result()
  return 


def main(args=None):
  rclpy.init(args=args)
  
  fct = FoxCommuTmp()
  # �w��m�[�h���X�s��������i�����A�R�[���o�b�N�̊m�F�Ȃǂ�����j
  rclpy.spin(fox_comm_tmp_server)
  
if __name__=='__main__':
  main()