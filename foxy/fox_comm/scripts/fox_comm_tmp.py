#!/usr/bin/env python3
#-*-cording:utf-8-*-

#---------------------------------
# RCLPYの通信構文をまとめたノード
#---------------------------------

import time
# PythonのROS2クライアントライブラリ
import rclpy
# rclpyのNodeという親クラスを引用
from rclpy.node import Node
# rclpyのClock関数を使ってrospy.sleep()みたいなことをできるようにする
from rclpy.clock import Clock
# アクションサーバーを生成するために使う
from rclpy.action import ActionServer, CancelResponse, GoalResponse
# 
from rclpy.callback_groups import ReentrantCallbackGroup
#
from rclpy.duration import Duration
# 同時にゴール処理を実行できるようにするツール（本来アクションは一つのゴール以外の処理はしない）
from rclpy.executors import MultiThreadedExecutor


# 自作メッセージの用意
from fox_test_msgs.msg import MyMessage
# 自作サービスメッセージの用意
from fox_test_msgs.srv import ServiceTest
# 自作アクションメッセージの用意
from fox_test_msgs.action import ActionTest


# "Node"をスーパークラスとして、FoxCommTmpというサブクラスを宣言（クラス継承）
# Nodeクラスの継承により、Nodeクラスの便利な関数をサブクラス内で利用できる
class FoxCommTmp(Node):
  # 指定名のノードの生成
  super().__init__('fox_comm_tmp_server')
  # コンストラクタ処理（定義なし）と必要なものを宣言
  def __init__(self):
    # ROSのロギング機能でログメッセージ出力
    # （ログ メッセージの重大度レベル： DEBUG >INFO >WARN >ERROR, FATAL）
    self.get_logger().info("Ready to **navi_location_server2**")
    # Topicのサブスクライバー/リスナーの宣言/生成
    topic_test_sub = self.create_subscription(MyMessage, # 型
                                              'topic_test', # トピック名
                                              self.topicCallback, # コールバック関数
                                              queue_size = 1 # キュー/バッファの大きさ
                                              )
    # ServiceServerの宣言/生成
    service = self.create_service(ServiceTest, 'service_test',
                                  self.serviceCallback)
    # ActionServerの宣言/生成
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
    
  # トピックTalkerのメッセージ（トピック名： topic_test）を受け取ったときに実行するコールバック関数
  def topicCallback(self, msg):
    self.get_logger().warn('Executing topic-request...')
    self.get_logger().info('Topic message: \n' + 
                           msg.string_message + '\n'+
                           msg.int32_message + '\n'+
                           msg.float64_message + '\n'+
                           msg.bool_message
                           )

  # サービスリクエスト（サービス名： service_test）を受け取ったときに実行するコールバック関数
  def serviceCallback(self, req):
    self.get_logger().warn('Executing service-request...')
    result = ActionTest.Result()
    
    self.get_logger().info('Service resuest: ' + req.srv_request)
    
    return result.srv_response == True

  # アクションゴール（サービス名： action_test）を受け取ったときに実行するコールバック関数
  def asCallback(self, goal_request):


  # アクションを実行する関数
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
      
    # アクションが完了したら
    self.get_logger().info(f'{goal.request.ac_request} succeeded!!')
    goal.succeed()
    result.ac_result = True
    self.get_logger().info('Returning result: {0}'.format(result.ac_result))
    return result
    

  # ゴールを受け付けてアクションを開始する関数
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
    
  # アクションクライアントのキャンセルリクエストを受けいれる関数
  def asCancelCallback(self, goal):
    self.get_logger().info('Received cancel request')
    return CancelResponse.ACCEPT
  
  # アクションを破棄する関数
  def asDestroy(self):
    self.test_as.destroy()
    super().destroy_node()


  def action
  

# メイン関数
def main(args=None):
  # ROS2通信の初期化
  rclpy.init(args=args)
  # FoxCommTmpクラスをインスタンス化
  fct_node = FoxCommTmp()
  mte = MultiThreadedExecutor()
  # ノード終了まで指定ノードをスピン(待機状態)にさせる（逐次、コールバックの確認などをする）
  rclpy.spin(fct_node, executor = mte)
  # ROS通信のシャットダウン
  fct_node.asDestroy()
  rclpy.shutdown()
  
if __name__=='__main__':
  main()