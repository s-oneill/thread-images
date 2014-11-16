#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//Global Constants
string IMG_MARKER = "href=\"//i.4cdn.org/";
string URL_START  = "\"//";

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

//Extracts the URL from an inputted string
string extractURL(string input);

//------------------------------------------------------------------------
int main(int argc, char** argv)
{
    string str;

    instream.open(argv[1]);
    outstream.open(argv[2]);

    if (instream.fail()){
        cout << "failed to open file" << endl;
        exit(1);
    }
  
    while (instream.good()) {
        instream >> str;
        if(str.find(IMG_MARKER) != string::npos)
            outstream << extractURL(str) << endl;
    }  
    
    instream.close();
    outstream.close();
  
    return 0;
}

//----------------------------------------------------------------------------

string extractURL(string input)
{
    string extractedURL = "";
    size_t index = input.find(URL_START) + URL_START.size();
    for(size_t i = index; i < input.size() - 1; i++) { //-1 is for ending "
        extractedURL.push_back(input[i]);
    }
    return extractedURL;
}

//----------------------------------------------------------------------------
