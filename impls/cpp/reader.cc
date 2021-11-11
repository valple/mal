#include <cstdlib>
#include <iostream>
#include <memory>
#include <pcrecpp.h>
#include <string>
#include <forward_list>
#include <stdio.h>

class Reader {
public:
  std::forward_list<std::string> tokens;
  // Do I really need a position argument?
  // Never need to go back
  // Saves memory to use forward lists
  //  int position;
  std::string peek() {
    return tokens.front();
  }
  std::string next() {
    std::string token = tokens.front();
    tokens.pop_front();
    return token;
  }
  void testprint () {
    while (!tokens.empty()) {
      std::cout << next() << std::endl;
    }
  }
  // Construct Reader object from string
  Reader(std::string input) {
    pcrecpp::StringPiece content(input);
    static pcrecpp::RE re(
        "[\\s,]*(~@|[\\[\\]{}()'`~@]|\"(?:\\\\.|[^\\\\\"])*\"?|"
        ";.*|[^\\s\\[\\]{}('\"`,;)]*)");
    std::string var;
    re.FindAndConsume(&content, &var);
    while (!var.empty()) {
      tokens.push_front(var);
      re.FindAndConsume(&content, &var);
    }
    tokens.reverse();
  }
};

// read atom
std::unique_ptr<Mal> read_atom(Reader rdr) {
  std::string token = rdr.peek();
  char* p;
  const char* tok = token.c_str();
  double converted = strtod(tok, &p);
  if (*p) {
    return std::make_unique<MalSymbol>(token);
  } else {
    return std::make_unique<MalNumber>(converted);
  }
}

// forward declaration to allow calling between read_form and read_list
std::unique_ptr<Mal> read_form(Reader rdr);

// Read list
// Clusterfuck of ugly stuff
std::unique_ptr<Mal> read_list(Reader rdr) {
  auto malexp = std::make_unique<MalList>();
  std::string token = rdr.next();
  token = rdr.peek();
  while(!(token == ")")) {
    malexp->mlist.push_front(std::move(read_form(rdr)));
    // Error handling here later
    if (rdr.tokens.empty()) {
      break;
    }
    token = rdr.next();
    token = rdr.peek();
  }
  malexp->mlist.reverse();
  return std::move(malexp);
}

// Read form
std::unique_ptr<Mal> read_form(Reader rdr) {
  std::string token = rdr.peek();
  if (token == "(") {
    return read_list(rdr);
  } else {
    return read_atom(rdr);
  }
}

// Read a string to get a mal datastructure
std::unique_ptr<Mal> read_str(std::string input) {
  Reader rdr(input);
  return read_form(rdr);
}
