#include <cctype>
#include <forward_list>
#include <memory>
#include <string>
#include <iostream>
#include <pcrecpp.h>

/* Mal Types  */

// Overall class
class Mal {
  public:
  int mtype;
  std::forward_list<std::unique_ptr<Mal>> mlist;
  virtual std::string value() {
    return "ouch";
  }
  virtual std::unique_ptr<Mal> first_elem() {
    return std::make_unique<Mal>();
  }
  virtual void del_first() {};
  virtual bool isempty() { return true;};
};

// List of Mal types
class MalList: public Mal {
public:
  std::forward_list<std::unique_ptr<Mal> > mlist;
  MalList() {
    mtype = 1; }
  std::unique_ptr<Mal> first_elem() {
    return std::move(mlist.front());
  }
  void del_first() {
    mlist.pop_front();
  }
  bool isempty() {
    return mlist.empty();
  }
};

// Mal symbol subclass
class MalSymbol: public Mal {
public:
  std::string symbol;
  std::string value() {
    return symbol;
  }
  MalSymbol(std::string input) {
    mtype = 3;
    symbol = input;
  }
};

// Mal number
// Need to implement different constructors or whatever for int and double
// Adds useless zeros for now
class MalNumber: public Mal {
public:
  double number;
  std::string value() {
    return std::to_string(number);
  }
  MalNumber(double input) {
    mtype = 2;
    number = input;
  }
};

// int main(int argc, char *argv[])
// {
//   std::forward_list<std::string> test;
//   test.assign({"fuck", "you", "asshole"});
//   //  static pcrecpp::RE re("\[\\s,]*(~@|\[\[]{}\()\'`~^@]\"\(\?:.|\[^\"])*\"\?|;.*|\[^\\s\[]{}\(\'\"`,;)]*)");
//   // static pcrecpp::RE re("^(\()");
//   //static pcrecpp::RE te("[\\s ,]*(~@|[\\[\\]{}()'`~@]|\"(?:[\\\\].|[^\\\\\"])*\"?|;.*|[^\\s \\[\\]{}()'\"`~@,;]*)");
//   static pcrecpp::RE re("[\\s,]*(~@|[\\[\\]{}()'`~@]|\"(?:\\\\.|[^\\\\\"])*\"?|;.*|[^\\s\\[\\]{}('\"`,;)]*)");

//   MalList lispy;
//   MalNumber mumber(3);
//   MalSymbol msymbol("test");
//   lispy.mlist.assign({mumber, msymbol});
//   int val;
//   std::string var;
//   std::string content = "(+ 3 ( 3)";
//   pcrecpp::StringPiece input(content);
//   //if (te.PartialMatch(input, &var, &val)) {
//   //  std::cout << var << std::endl;
//   // }
//   while (re.FindAndConsume(&input, &var)) {
//     std::cout << var << std::endl;
//   }
//   // for (int i=0; i<10; i++) {
//   //   re.FindAndConsume(&input, &var);
//   //   if (var.empty()) {
//   //     break;
//   //   }
//   //   std::cout << var << std::endl;
//   // }

//   std::cout << test.front() << lispy.mlist.front().mtype << std::endl;
//   lispy.mlist.pop_front();
//   std::cout << lispy.mlist.front().mtype <<std::endl;
//   return 0;
// }

