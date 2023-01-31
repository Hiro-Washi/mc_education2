#!/usr/bin/env python3
#-*-cording:utf-8-*-

# RCLPY�̃N���C�A���g���̒ʐM�R�[�h�\�����܂Ƃ߂��e���v���[�g

# ROS2
import time
# Python��ROS2�N���C�A���g���C�u����
import rclpy
# rclpy��Node�Ƃ����e�N���X�����p
from rclpy.node import Node
# rclpy��Clock�֐����g����rospy.sleep()�݂����Ȃ��Ƃ��ł���悤�ɂ���
from rclpy.clock import Clock
# �A�N�V�����N���C�A���g�̐����Ɏg��
from rclpy.action import ActionClient

# ���상�b�Z�[�W�̗p��
from fox_test_msgs.msg import MyMessage
# ����T�[�r�X���b�Z�[�W�̗p��
from fox_test_msgs.srv import ServiceTest
# ����A�N�V�������b�Z�[�W�̗p��
from fox_test_msgs.action import ActionTest

class FoxCommTmpClient(Node):
  def __init__(self):
    super().__init__('fox_comm_tmp_client')
    self.get_logger().info("**fox_comm_tmp_client**�m�[�h�̏���������")
    
    # �g�s�b�N�̃p�u���b�V���[��錾
    self.topic_publisher = self.create_publisher(MyMessage, '/current_location', queue_size = 1)
    # �T�[�r�X�̃N���C�A���g��錾
    self.srv_client = self.create_client(ServiceTest, 'service_test')
    # 1�b��1��srv_client�̃T�[�r�X�����p�ł��邩�`�F�b�N
    while not self.srv_client.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('service not available, waiting again...')
    self.srv_req = ServiceTest.Request() # ���N�G�X�g�C���X�^���X�̐����B����Ƀ��N�G�X�g�f�[�^���i�[�����B
    # �A�N�V�����N���C�A���g��錾
    self.ac_client = ActionClient(self, ActionTest, 'action_test')
    
  