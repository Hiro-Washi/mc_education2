#!/usr/bin/env python3
#-*-cording:utf-8-*-

#---------------------------------
# RCLPY�̒ʐM�\�����܂Ƃ߂��m�[�h
#---------------------------------

import time
# Python��ROS2�N���C�A���g���C�u����
import rclpy
# rclpy��Node�Ƃ����e�N���X�����p
from rclpy.node import Node
# rclpy��Clock�֐����g����rospy.sleep()�݂����Ȃ��Ƃ��ł���悤�ɂ���
from rclpy.clock import Clock
# �A�N�V�����T�[�o�[�𐶐����邽�߂Ɏg��
from rclpy.action import ActionServer, CancelResponse, GoalResponse
# 
from rclpy.callback_groups import ReentrantCallbackGroup
#
from rclpy.duration import Duration
# �����ɃS�[�����������s�ł���悤�ɂ���c�[���i�{���A�N�V�����͈�̃S�[���ȊO�̏����͂��Ȃ��j
from rclpy.executors import MultiThreadedExecutor


# ���상�b�Z�[�W�̗p��
from fox_test_msgs.msg import MyMessage
# ����T�[�r�X���b�Z�[�W�̗p��
from fox_test_msgs.srv import ServiceTest
# ����A�N�V�������b�Z�[�W�̗p��
from fox_test_msgs.action import ActionTest


# "Node"���X�[�p�[�N���X�Ƃ��āAFoxCommTmp�Ƃ����T�u�N���X��錾�i�N���X�p���j
# Node�N���X�̌p���ɂ��ANode�N���X�֗̕��Ȋ֐����T�u�N���X���ŗ��p�ł���
class FoxCommTmp(Node):
  # �w�薼�̃m�[�h�̐���
  super().__init__('fox_comm_tmp_server')
  # �R���X�g���N�^�����i��`�Ȃ��j�ƕK�v�Ȃ��̂�錾
  def __init__(self):
    # ROS�̃��M���O�@�\�Ń��O���b�Z�[�W�o��
    # �i���O ���b�Z�[�W�̏d��x���x���F DEBUG >INFO >WARN >ERROR, FATAL�j
    self.get_logger().info("Ready to **navi_location_server2**")
    # Topic�̃T�u�X�N���C�o�[/���X�i�[�̐錾/����
    topic_test_sub = self.create_subscription(MyMessage, # �^
                                              'topic_test', # �g�s�b�N��
                                              self.topicCallback, # �R�[���o�b�N�֐�
                                              queue_size = 1 # �L���[/�o�b�t�@�̑傫��
                                              )
    # ServiceServer�̐錾/����
    service = self.create_service(ServiceTest, 'service_test',
                                  self.serviceCallback)
    # ActionServer�̐錾/����
    self.test_as = ActionServer(self, 
                            ActionTest,
                            'action_test',
                            self.asCallback,
                            execute_callback=self.asExecuteCallback,
                            goal_callback=self.asGoalCallback,
                            handle_accepted_callback=self.handleAcceptedCallback,
                            cancel_callback=self.asCancelCallback,
                            callback_group=ReentrantCallbackGroup()
                            )
    self.get_logger().info("ActionTest action server has been initialised.")
    # 
    self.ac_goal = ActionTest.Goal()
    
  # �g�s�b�NTalker�̃��b�Z�[�W�i�g�s�b�N���F topic_test�j���󂯎�����Ƃ��Ɏ��s����R�[���o�b�N�֐�
  def topicCallback(self, msg):
    self.get_logger().warn('Executing topic-request...')
    self.get_logger().info('Topic message: \n' + 
                           msg.string_message + '\n'+
                           msg.int32_message + '\n'+
                           msg.float64_message + '\n'+
                           msg.bool_message
                           )

  # �T�[�r�X���N�G�X�g�i�T�[�r�X���F service_test�j���󂯎�����Ƃ��Ɏ��s����R�[���o�b�N�֐�
  def serviceCallback(self, req):
    self.get_logger().warn('Executing service-request...')
    result = ActionTest.Result()
    
    self.get_logger().info('Service resuest: ' + req.srv_request)
    
    return result.srv_response == True

  # �A�N�V�����S�[���i�T�[�r�X���F action_test�j���󂯎�����Ƃ��Ɏ��s����R�[���o�b�N�֐�
  def asCallback(self, goal_request):


  # �A�N�V���������s����֐�
  async def asExecuteCallback(self, goal):
    self.get_logger().info('Executing action goal...')
    #ac_num = 0
    result = ActionTest.Result()
    fb_msg = ActionTest.Feedback()
    start_time = self.get_clock().now()
    
    for i in range(goal.request.ac_request):
      ac_num = goal.request.ac_request
      print('action count: ' + ac_num)
      ac_num =- 1
      time.sleep(1.0)
      goal.publish_feedback(fb_msg)
      
    # �A�N�V����������������
    self.get_logger().info(f'{goal.request.ac_request} succeeded!!')
    goal.succeed()
    result.ac_result = True
    self.get_logger().info('Returning result: {0}'.format(result.ac_result))
    return result
    

  # �S�[�����󂯕t���ăA�N�V�������J�n����֐�
  def asGoalCallback(self, goal_request):
    self.get_logger().info('Received goal request')
    self.goal = goal_request
    return GoalResponse.ACCEPT
  
  # 
  def handleAcceptedCallback(self, goal_handle):
      with self._goal_lock:
        # This server only allows one goal at a time
        if self._goal_handle is not None and self._goal_handle.is_active:
          # Abort the existing goal
          self._goal_handle.abort()
        self._goal_handle = goal_handle
      goal_handle.execute()
    
  # �A�N�V�����N���C�A���g�̃L�����Z�����N�G�X�g���󂯂����֐�
  def asCancelCallback(self, goal):
    self.get_logger().info('Received cancel request')
    return CancelResponse.ACCEPT
  
  # �A�N�V������j������֐�
  def asDestroy(self):
    self.test_as.destroy()
    super().destroy_node()


  def action
  

# ���C���֐�
def main(args=None):
  # ROS2�ʐM�̏�����
  rclpy.init(args=args)
  # FoxCommTmp�N���X���C���X�^���X��
  fct_node = FoxCommTmp()
  mte = MultiThreadedExecutor()
  # �m�[�h�I���܂Ŏw��m�[�h���X�s��(�ҋ@���)�ɂ�����i�����A�R�[���o�b�N�̊m�F�Ȃǂ�����j
  rclpy.spin(fct_node, executor = mte)
  # ROS�ʐM�̃V���b�g�_�E��
  fct_node.asDestroy()
  rclpy.shutdown()
  
if __name__=='__main__':
  main()