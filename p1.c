#include<assert.h>

int main() {
    int i = 0;
    do {
        assert(i <= 10);
        i = i+2;
    } while(i<5);
    return 0;
}

/*
https://wisesciencewise.wordpress.com/2022/10/03/steps-to-generate-llvm-call-flow-graphcfg/

https://llvm.org/docs/CommandGuide/opt.html
*/