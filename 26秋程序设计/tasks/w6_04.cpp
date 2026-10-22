// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>
// using namespace std;

// int countdu(string str)
// {
// 	int count = 0;
// 	int len = str.size();
// 	for (int i = 0; i < len; i++)
// 	{
// 		for (int j = i + 1; j < len; j++)
// 		{
// 			if (str[j] < str[i])
// 				count++;
// 		}
// 	}
// 	return count;
// }
// bool cmp(pair<int, int> a, pair<int, int> b)
// {
// 	return a.first < b.first;
// }
// int main()
// {
// 	int n, m; // n为字符串长度，m为字符串个数
// 	while (cin >> n >> m)
// 	{
// 		vector<string> dna(m);
// 		for (int i = 0; i < m; i++)
// 		{
// 			cin >> dna[i];
// 		}

// 		// 用pair存储dna字符串对应的逆序对数
// 		vector<pair<int, int>> order(m);
// 		for (int i = 0; i < m; i++)
// 		{
// 			order[i] = {countdu(dna[i]), i};
// 		}
// 		stable_sort(order.begin(), order.end(), cmp);
// 		// 稳定排序，不改变相同逆序对数的字符串的相对顺序
// 		for (int i = 0; i < m; i++)
// 			cout << dna[order[i].second] << endl;
// 		cout << "********************" << endl;
// 	}
// 	return 0;
// }

//求一串数字的逆序对数量
#include <iostream>
#include <vector>
using namespace std;

long long mergeSort(vector<int>& a,vector<int>& tmp,int l,int r)
{
	if(l>=r) return 0;

	int mid=(l+r)/2;
	long long res=0;
	res+=mergeSort(a,tmp,l,mid);
	res+=mergeSort(a,tmp,mid+1,r);
	//上述已经统计了左边和右边的逆序对数量，下面统计跨越左右两边的逆序对数量
	//归并排序并统计逆序对数量
	int i=l,j=mid+1,k=l;
	while(i<=mid&&j<=r)
	{
		if(a[i]<=a[j]) tmp[k++]=a[i++];
		else
		{
			tmp[k++]=a[j++];
			res+=mid-i+1; //统计逆序对数量
		}
	}
	
}