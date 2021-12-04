#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<int> data;
int count, sum_vec_A, sum_vec_B;

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

int increaseValuesFiltered(vector<int> vec)
{
    int lhs, count;
    count= 0;
    vector<int>::iterator ptr,nptr,n2ptr;
    lhs = vec.front();
    n2ptr=ptr;
    for(ptr = vec.begin()+1;n2ptr <= vec.end()-2; ptr++)
    {
        sum_vec_A,sum_vec_B = 0;
        nptr = n2ptr = ptr;
        advance(nptr,1);
        advance(n2ptr,2);
        sum_vec_A = lhs + *ptr + *nptr;
        sum_vec_B = *ptr + *nptr + *n2ptr;
        lhs=*ptr;
        cout << sum_vec_A << "  " << sum_vec_B << endl;
        if (sum_vec_B > sum_vec_A)
        {
            count = count + 1;
        }
    }
    return count;
}

int main(int argc, char** argv){

    readFile("../data/sample.txt", data);
    count = increaseValuesFiltered(data);
    cout << count << endl;
}