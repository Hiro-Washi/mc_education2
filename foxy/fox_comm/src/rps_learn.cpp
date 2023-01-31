// じゃんけんを学習する
// text.testに相手の手を格納

#include <stdio.h>
#include <stdlib.h>

#define SEED 65535 // 乱数のシード
#define ROCK 0
#define SCISSORS 1
#define PAPER 2
#define WIN 1
#define LOSE -1
#define DRAW 0
#define ALPHA 0.01// 学習係数

int hand(double rate[]); //乱数・引数で手を決定
double frand(void); //　0~1の実数乱数

int main(){
  int n = 0; //対戦回数カウンタ
  int my_hand, opp_hand; // 自分と相手の手
  double rate[3] = {1,1,1}; // 出し手の出現割合
  int gain; // 勝ち負けの結果
  int payoffmatrix[3][3] = {{DRAW, WIN, LOSE},
                            {LOSE, DRAW, WIN},
                            {WIN, LOSE, DRAW}}; //利得行列
  // 対戦相手と学習を繰り返す
  while (scanf("%d", &opp_hand) != EOF){
    // 不正な手の入力
    if((opp_hand < ROCK)||(opp_hand > PAPER)) continue;
    my_hand = hand(rate); // 出現割合に基づいた手の決定
    gain = payoffmatrix[my_hand][opp_hand]; // 結果
    printf("%d %d %d  ", my_hand, opp_hand, gain);
    rate[my_hand] += gain * ALPHA * rate[my_hand]; // 出現割合の学習
    printf("%lf %lf %lf\n", 
      rate[ROCK], rate[SCISSORS], rate[PAPER]); 
  }
}

int hand(double rate[]){
  double rock, scissors, paper;
  rock = rate[ROCK] * frand();
}