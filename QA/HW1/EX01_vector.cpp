#include<iostream>
#include<stdlib.h>
#include<vector>

using namespace std;

vector<int>& unionVectors(vector<int>& a, vector<int>& b);

int main()
{
  vector<int> a;
  vector<int> b;
  vector<int> result;
  int number;
	
  int i;
	
  for (i = 0; i < 5; i ++)
    {
      cout<<"Enter a number: ";
      cin>>number;
      a.push_back(number);
    }
	
  for (i = 0; i < 5; i ++)
    {
      cout<<"Enter a number: ";
      cin>>number;
      b.push_back(number);
    }
	
  result = unionVectors(a,b);
	
  return 0;
}

vector<int>& unionVectors(vector<int>& a, vector<int>& b)
{
  vector<int> rval;
  unsigned int j;
	
  for(j = 0; j < a.size(); j++)
    {
      rval.push_back(a[j]);
      cout<<j<<endl;
    }
	
  return rval;
}
