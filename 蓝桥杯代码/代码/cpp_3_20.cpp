//判断数组元素为空时范围for是否被执行
//#include <iostream>
//#include <vector>>
//using namespace std;
//const int N=1010;
//int arr1[N]; 
//vector<int> arr2[N];
//int main()
//{
//	for(int e:arr1)
//	{
//		cout << e << " ";
//	}
//	//执行 
//	cout << endl; 
//	for(int e:arr2[6])	//arr[6]是arr数组的第七个元素，为空vector，循环体不执行 
//	{
//		cout << e << " ";
//	}
//	//不执行 
//	cout << 0 << endl;
//	return 0;
//}


#include <iostream>

using namespace std;
const int N=1e5+10;
int n,arr[N];	//n为数组元素个数 

//插入排序,默认为升序 
void insert_sort()
{
	for(int i=2;i<=n;i++)
	{
		int t=arr[i];	//先把arr[i]的值存放在t里面 
		int j=i-1; 		//再给出i前面那个元素的下标
		//前面比t大的，统一右移 
		while(j>=1&&arr[j]>t)	//j>=0的限制是防止越界 
		{
			arr[j+1]=arr[j];	//将j位置的值向后移动一位 
			j--;
		}
		arr[j+1]=t;
	 } 
 } 
 
 //选择排序 
 void selection_sort()
 {
 	for(int i=1;i<n;i++)
 	{
 		int pos=i;
 		for(int j=i+1;j<=n;j++)
 		{
 			if(arr[j]<arr[pos])
 				pos=j;
		 }
		swap(arr[i],arr[pos]);
	 }
  } 
 
 int main()
 {
 	cin >> n;
 	for(int i=1;i<=n;i++)
 	{
 		cin >> arr[i];
	 }
	selection_sort();
	for(int i=1;i<=n;i++)
		cout << arr[i] << " ";
		
	return 0;
 }
