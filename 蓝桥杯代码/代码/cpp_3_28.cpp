#include <stdio.h>
#include <string.h>

//轮换前n个，再递归处理
void permu(char* data, int cur)
{
    int i,j;
    
    if(data[cur]=='\0'){
        printf("%s\n", data);
        return;
    }
    
    for(i=cur; data[i]; i++){
        char tmp = data[i]; 
        for(j=i-1; j>=cur; j--) data[j+1] = data[j];
        data[cur] = tmp;            

        permu(data, cur+1);            

        tmp = data[cur]; 
//        ___________________________________ ;  //填空
        data[i] = tmp;            
    }
}

int main()
{
    char a[105];
    scanf("%s",a);
    permu(a,0);
    return 0;
}
