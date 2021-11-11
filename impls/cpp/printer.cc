#include <memory>
#include <string>
#include <typeinfo>
#include <utility>

// Iterate through a Mal data structure and return a string representation of it
std::string pr_str(std::unique_ptr<Mal> sexp) {
  std::string output = "";
  switch(sexp->mtype) {
  case 3:
    return sexp->value();
  case 2:
    return sexp->value();
  case 1:
    output.append("(");
    while(!sexp->isempty()) {
      output.append(pr_str(std::move(sexp->first_elem())));
      output.append(" ");
      sexp->del_first();
    }
    output.append(")");
    return output;
  }
  return output;
}


