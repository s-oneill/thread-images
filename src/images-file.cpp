
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream instream;
ofstream outstream;

//------------------------------------------------------------------------

/*
// initialize ifstream with proper file
void init_instream(char * infile){
    
    instream.open(argv[1]);
    
}

// initialize ofstream with proper output file
void init_outstream(char * outfile){
    
}
*/

//------------------------------------------------------------------------
int main(int argc, char** argv)
{
    char c;

    instream.open(argv[1]);
    outstream.open(argv[2]);

    if (instream.fail()){
        cout << "failed to open file" << endl;
        exit(1);
    }
  
    while (instream.good()) {
        instream >> c;
        outstream << c << endl;
    }  
    
  
    instream.close();
    outstream.close();
  
    return 0;
}



//----------------------------------------------------------------------------
//----------------------------------------------------------------------------

