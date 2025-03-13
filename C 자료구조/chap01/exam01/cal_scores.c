// 최고 성적을 구하는 프로그램

#include <stdio.h>
#define MAX_ELEMENTS 100
int scores[MAX_ELEMENTS];

int get_max_score(int n)
{
    int i, largest;

    largest = scores[0];
    for(i = 0; i < n; i++){
        if(scores[i] > largest){
            largest = scores[i];
        }
    }

    return largest;
}

int main(){

    scores[0] = 95;
    scores[1] = 78;
    scores[2] = 332;

    printf("Largest score : %d\n", get_max_score(3));

    return 0;
}