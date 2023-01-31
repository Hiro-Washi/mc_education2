// ����񂯂���w�K����
// text.test�ɑ���̎���i�[

#include <stdio.h>
#include <stdlib.h>

#define SEED 65535 // �����̃V�[�h
#define ROCK 0
#define SCISSORS 1
#define PAPER 2
#define WIN 1
#define LOSE -1
#define DRAW 0
#define ALPHA 0.01// �w�K�W��

int hand(double rate[]); //�����E�����Ŏ������
double frand(void); //�@0~1�̎�������

int main(){
  int n = 0; //�ΐ�񐔃J�E���^
  int my_hand, opp_hand; // �����Ƒ���̎�
  double rate[3] = {1,1,1}; // �o����̏o������
  int gain; // ���������̌���
  int payoffmatrix[3][3] = {{DRAW, WIN, LOSE},
                            {LOSE, DRAW, WIN},
                            {WIN, LOSE, DRAW}}; //�����s��
  // �ΐ푊��Ɗw�K���J��Ԃ�
  while (scanf("%d", &opp_hand) != EOF){
    // �s���Ȏ�̓���
    if((opp_hand < ROCK)||(opp_hand > PAPER)) continue;
    my_hand = hand(rate); // �o�������Ɋ�Â�����̌���
    gain = payoffmatrix[my_hand][opp_hand]; // ����
    printf("%d %d %d  ", my_hand, opp_hand, gain);
    rate[my_hand] += gain * ALPHA * rate[my_hand]; // �o�������̊w�K
    printf("%lf %lf %lf\n", 
      rate[ROCK], rate[SCISSORS], rate[PAPER]); 
  }
}

int hand(double rate[]){
  double rock, scissors, paper;
  rock = rate[ROCK] * frand();
}