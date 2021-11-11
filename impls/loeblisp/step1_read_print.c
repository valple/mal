#include <stdio.h>
#include <stdlib.h>

#include <pcreposix.h>

static char buffer[2048];

char* READ(char* input) {
    return input;
}

char* EVAL(char* input) {
    return input;
}

char* PRINT(char* input) {
    return input;
}

char* rep(char* input) {
    return PRINT(EVAL(READ(input)));
}

int main(int argc, char *argv[]) {
    while (1) {
        fputs("user> ", stdout);
        fgets(buffer, 2048, stdin);
        if (feof(stdin)) { break; };
        printf("%s", rep(buffer));
    }
    return 0;
}
