// Shane O'Neill
// Lab1 - CISC220 - 
// Modified wordbyword to remove punction except for apostrophe's using a temporary file


#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream instream;
ofstream outstream;

//------------------------------------------------------------------------

// initialize ifstream with proper file
void init_instream(int argc, char ** argv){
    
    if (argc < 2){
        cout << "please specify a URL within the bash script" << endl; 
        exit(1);
    }
    
    instream.open(argv[1]);
}

// initialize ofstream with proper output file
void init_outstream(char **argv){
// ...
}

//------------------------------------------------------------------------
int main(int argc, char** argv)
{
    string s;


    // get ready to write to TEMP file
  
    outstream.open("temp.txt");
 
    // write the words to a temp file and remove the punctuation
  
    while (instream >> s) {
    
        outstream << s << " ";

    }  
    
  
    // close and reopen the newly created modified file as well as the echo file
    instream.close();
    outstream.close();
  
    return 0;
}



//----------------------------------------------------------------------------
//----------------------------------------------------------------------------

