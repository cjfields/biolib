%{
  
  using namespace std;   /* Make sure the STL is used */

  #include <Clonable.h>
  #include <BppString.h>

%}



%include std_string.i

# %include <string>
%include <Clonable.h>

# %rename(string) std::string;
# %naturalvar string;

%include <BppString.h>


