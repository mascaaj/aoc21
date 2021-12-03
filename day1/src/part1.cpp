#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int readFile(string filename, vector<int>& vec)
{10 am
    string line;
    int i, num;
    stringstream stream;
    ifstream reader(filename);

    for(i=0;!reader.eof();i++)
    {
        getline(reader,line);
        stream << line;
        stream >> num;
        cout << "counter "<< i << endl;
        vec.push_back(num);
    }
}
int main(int argc, char** argv){

    vector<int> data;
    readFile("../data/sample.txt", data);
    cout << data.size() << endl;
    cout << data.front() << endl;
}