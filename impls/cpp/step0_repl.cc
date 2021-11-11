#include "linenoise.hpp"
#include <iostream>
#include <pcrecpp.h>
#include <string>

std::string READ(std::string input) { return input; };

std::string EVAL(std::string input) { return input; };

std::string PRINT(std::string input) { return input; };

std::string rep(std::string input) {
  auto inp = READ(input);
  auto evp = EVAL(inp);
  return PRINT(evp);
}

int main(int argc, char *argv[])
{
  linenoise::SetHistoryMaxLen(10);
  while(1) {
    std::string line;
    auto quit = linenoise::Readline("user> ", line);
    if (quit) {
      break;
    } 
    std::cout << rep(line) << std::endl;
    linenoise::AddHistory(line.c_str());
  }
  return 0;
}

