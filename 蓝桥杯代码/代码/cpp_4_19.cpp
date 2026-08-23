//#include <iostream>
//#include <algorithm>
//using namespace std;
//int a[5];
//int main()
//{
//	int n; cin >> n;
//	while(n--)
//	{
//		for(int i=0;i<4;i++) cin >> a[i];
//		sort(a,a+4);
//		for(int i=0;i<4;i++) cout << a[i] << " ";
//		cout << endl;
//	}
//	return 0;
//}

#include <iostream>
#include <ctime>
using namespace std;
//const int N = 1e5 + 10;
//int n, arr[N];	//n为数组元素个数 
//
////1.插入排序,默认为升序 
//void insert_sort()
//{
//	for (int i = 2; i <= n; i++)
//	{
//		int t = arr[i];	//先把arr[i]的值存放在t里面 
//		int j = i - 1; 		//再给出i前面那个元素的下标
//		//前面比t大的，统一右移 
//		while (j >= 1 && arr[j] > t)	//j>=1的限制是防止越界 
//		{
//			arr[j + 1] = arr[j];	//将j位置的值向后移动一位 
//			j--;
//		}
//		arr[j + 1] = t;
//	}
//}
//
////2.选择排序 
//void selection_sort()
//{
//	for (int i = 1; i < n; i++)
//	{
//		int pos = i;
//		for (int j = i + 1; j <= n; j++)
//		{
//			if (arr[j] < arr[pos])
//				pos = j;
//		}
//		swap(arr[i], arr[pos]);
//	}
//}
//
////3.冒泡排序
//void bubble_sort()
//{
//	for (int i = 1; i < n; i++)
//	{
//		bool flag = false;	//提前退出冒泡循环的标志位
//		for (int j = 1; j <= n - i; j++)
//		{
//			if (arr[j] > arr[j + 1])
//				swap(arr[j], arr[j + 1]);
//			flag = true;	//如果发生了交换，说明还没有排好序
//		}
//		if (!flag)	//如果没有发生交换，说明已经排好序了，可以提前退出循环
//		{
//			break;
//		}
//	}
//}
////4.堆排序
//
////向下调整算法,调整为大根堆，即父节点的值大于子节点的值
////核心思想：每次调整一个父节点，让它和它的子节点比较，如果父节点的值小于子节点的值，就交换它们的位置，然后继续向下调整，直到父节点的值大于子节点的值，或者没有子节点了
//void down(int parent, int len)
//{
//	int child = parent * 2;
//	while (child <= len)
//	{
//		if (child + 1 <= len && arr[child + 1] > arr[child])
//			child++;
//		if (arr[parent] > arr[child])
//			break;
//		swap(arr[parent], arr[child]);
//		parent = child;
//		child = parent * 2;
//	}
//}
//void heap_sort()
//{
//	//1.建堆
//	for (int i = n / 2; i >= 1; i--)
//	{
//		down(i, n);
//	}
//	//2.排序
//	for (int i = n; i >= 1; i--)
//	{
//		swap(arr[1], arr[i]);
//		down(1, i - 1);
//		//每次交换完之后，堆的长度就要减1了，因为最后一个元素已经排好序了，不需要再参与调整了
//	}
//}
//
////5.快速排序
//
////随机选择基准元素，避免出现最坏情况
//int get_random(int left, int right)
//{
//	return arr[rand() % (right - left + 1) + left];
//}
//
//void quick_sort(int left, int right)
//{
//	if (left >= right)
//		return;
//	int pivot = get_random(left, right);	//随机选择基准元素
//	//int i = left, j = right;
//	//while (i <= j)
//	//{
//	//	while (arr[i] < pivot)
//	//		i++;
//	//	while (arr[j] > pivot)
//	//		j--;
//	//	if (i <= j)
//	//	{
//	//		swap(arr[i], arr[j]);
//	//		i++;
//	//		j--;
//	//	}
//	//}
//	//quick_sort(left, j);
//	//quick_sort(i, right);
//	//数组分三块-荷兰国旗问题
//	int l = left - 1, i = left, r = right + 1;
//	while (i < r)
//	{
//		if (arr[i] < pivot)
//			swap(arr[++l], arr[i++]);
//		else if (arr[i] > pivot)
//			swap(arr[--r], arr[i]);
//		else i++;
//	}
//	quick_sort(left, l);
//	quick_sort(r, right);
//}
//
////6.归并排序
//int tmp[N];	//辅助数组
//void merge_sort(int left, int right)
//{
//	if (left >= right)
//		return;
//	int mid = (left + right) >> 1;
//	//先让左右区间有序，再进行合并
//	merge_sort(left, mid);
//	merge_sort(mid + 1, right);
//	int cur1 = left, cur2 = mid + 1, i = left;
//	while (cur1 <= mid && cur2 <= right)
//	{
//		if (arr[cur1] <= arr[cur2]) tmp[i++] = arr[cur1++];
//		else tmp[i++] = arr[cur2++];
//	}
//	while (cur1 <= mid) tmp[i++] = arr[cur1++];
//	while (cur2 <= right) tmp[i++] = arr[cur2++];
//
//	for (int j = left; j <= right; j++)
//		arr[j] = tmp[j];
//}
//
//int main()
//{
//	srand(time(0));
//	cin >> n;
//	for (int i = 1; i <= n; i++)
//	{
//		cin >> arr[i];
//	}
//	merge_sort(1,n);
//	for (int i = 1; i <= n; i++)
//		cout << arr[i] << " ";
//
//	return 0;
//} 
int main()
{
	int num = 0;
	for (int i = 1; i <= 202504; i++)
	{
		int sum = 0;
		while (i)
		{
			sum += i % 10;
			i /= 10;
		}
		cout << sum << endl;
		if (sum % 5 == 0) num++;
		cout << i << num << endl;
	}
	cout << num << endl;
	return 0;
}
