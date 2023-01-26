#!/usr/bin/env python3
#-*-cording:utf-8-*-

# PythonのROS2クライアントライブラリ
import rclpy
# rclpyのNodeという親クラスを引用
from rclpy.node import Node
# rclpyのClock関数を使ってrospy.sleep()みたいなことをできるようにする
from rclpy.clock import Clock
# アクションサーバーを生成するために使う
from rclpy.action import ActionServer

# 自作メッセージの用意
from fox_test_msgs.msg import MyMessage
# 自作サービスメッセージの用意
from fox_test_msgs.srv import ServiceTest, Service
# 自作アクションメッセージの用意
from fox_test_msgs.action import ActionTest



# Nodeを親クラスとして、FoxCommTmpという子クラスを宣言（クラス継承）
# Nodeクラスの継承により、Nodeクラスの便利な関数を子クラス内で利用できる
class FoxCommTmp(Node):
  # 指定名のノードの生成
  super().__init__('fox_comm_tmp_server')
  # コンストラクタの生成（このクラスを実行するときにここ内容が生成される）
  def __init__(self):
    # 初期化
    
    # TopicSubscriberの宣言/生成
    
    # ServiceServer
    
    # ActionServerの
    self._acserver = ActionServer(self, ActionTest, 'action_test',
                                  self.actionCallback)
    
    
def actionCallback(self, goal_hundle):
  self.get_logger().info('Executing goal...')
  result = ActionTest.Result()
  return 


def main(args=None):
  rclpy.init(args=args)
  
  fct = FoxCommuTmp()
  # 指定ノードをスピンさせる（逐次、コールバックの確認などをする）
  rclpy.spin(fox_comm_tmp_server)
  
if __name__=='__main__':
  main()