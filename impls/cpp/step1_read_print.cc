#include "linenoise.hpp"
#include <iostream>
#include <memory>
#include <string>

#include "types.cc"
#include "reader.cc"
#include "printer.cc"

std::unique_ptr<Mal> READ(std::string input) {
  return read_str(input);
}

std::unique_ptr<Mal> EVAL(std::unique_ptr<Mal> input) { return std::move(input); };

std::string PRINT(std::unique_ptr<Mal> input) {
  return pr_str(std::move(input));
}

std::string rep(std::string input) {
  return PRINT(EVAL(READ(input)));
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
    Reader rdr(line);
    rdr.testprint();
    std::cout << rep(line) << std::endl;
    linenoise::AddHistory(line.c_str());
  }
  return 0;
}

