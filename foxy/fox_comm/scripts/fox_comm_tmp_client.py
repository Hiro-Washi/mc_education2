#!/usr/bin/env python3
#-*-cording:utf-8-*-

# RCLPYのクライアント側の通信コード構文をまとめたテンプレート

# ROS2
import time
# PythonのROS2クライアントライブラリ
import rclpy
# rclpyのNodeという親クラスを引用
from rclpy.node import Node
# rclpyのClock関数を使ってrospy.sleep()みたいなことをできるようにする
from rclpy.clock import Clock
# アクションクライアントの生成に使う
from rclpy.action import ActionClient

# 自作メッセージの用意
from fox_test_msgs.msg import MyMessage
# 自作サービスメッセージの用意
from fox_test_msgs.srv import ServiceTest
# 自作アクションメッセージの用意
from fox_test_msgs.action import ActionTest

class FoxCommTmpClient(Node):
  def __init__(self):
    super().__init__('fox_comm_tmp_client')
    self.get_logger().info("**fox_comm_tmp_client**ノードの準備をする")
    
    # トピックのパブリッシャーを宣言
    self.topic_publisher = self.create_publisher(MyMessage, '/current_location', queue_size = 1)
    # サービスのクライアントを宣言
    self.srv_client = self.create_client(ServiceTest, 'service_test')
    # 1秒に1回srv_clientのサービスが利用できるかチェック
    while not self.srv_client.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('service not available, waiting again...')
    self.srv_req = ServiceTest.Request() # リクエストインスタンスの生成。これにリクエストデータが格納される。
    # アクションクライアントを宣言
    self.ac_client = ActionClient(self, ActionTest, 'action_test')
    
  