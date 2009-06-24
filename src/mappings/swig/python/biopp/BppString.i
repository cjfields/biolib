%{

  /* The following sections ends in the .cxx file */

  using namespace std;   /* Make sure the STL is used */

  #include <Clonable.h>
  #include <BppString.h>

%}

/* Below the actual SWIG inputs */

/* Use STL definitions of swig in /usr/share/swig */

%include std_string.i

using namespace std;

# %naturalvar string;
# %include "/usr/include/c++/4.3/string"

# %include <Clonable.h> 
%include <BppString.h>


