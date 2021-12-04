#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<int> data;
int count;

int readFile(string filename, vector<int>& vec)
{
    string line;
    int i, num;
    stringstream stream;
    ifstream reader(filename);

    for(i=0;!reader.eof();i++)
    {
        getline(reader,line);
        stream << line;
        stream >> num;
        vec.push_back(num);
    }
}

int increaseValues(vector<int> vec)
{
    int lhs, count;
    vector<int>::iterator ptr;
    lhs = vec.front();
    for(ptr = vec.begin();ptr < vec.end(); ptr++)
    {
        if(lhs<*ptr)
        {
            count = count +1;
        }
        lhs=*ptr;
    }
    return count;
}

int main(int argc, char** argv){

    readFile("../data/data.txt", data);
    count = increaseValues(data);
    cout << count << endl;
}