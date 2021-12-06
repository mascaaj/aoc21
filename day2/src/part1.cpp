#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<string> data;
int count;

int readFile(string filename, vector<string>& vec)
{
    string line;
    int i, num;
    stringstream stream;
    ifstream reader(filename);

    for(i=0;!reader.eof();i++)
    {
        getline(reader,line);
        vec.push_back(line);
    }
}

int getSubstring(string lineInput, int placement)
{
    if (placement ==1){
        // return magnitude integer
        return 0;
    } else {
        // return direction integer
        return 0;
    }
}

int processString(string lineInput)
{
    // or use array here
    int dirmag[2];
    dirmag[0] = direction; 
    dirmag[1] = magnitude;
    return result {getSubstring(lineInput,0),getSubstring(lineInput,1)};
}


int main(int argc, char** argv){

    readFile("../data/sample.txt", data);
    int i;
    for(i=0; i < data.size(); i++)
    {
        cout << data[i] << endl;
    }

}