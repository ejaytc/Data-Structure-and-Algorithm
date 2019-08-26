// bublesort.c
#include <stdio.h>


int main()
{
    unsigned i, j, temp, size, disp;
    unsigned set[5] = {7, 2, 5, 3, 4};
    size = sizeof(set) / sizeof(unsigned);

    for(j = 0; j < size; j++)
    {
        for(i = 0; i < size -1; i++)
        {
            if(set[i] > set[i +1])
            {
                temp = set[i];
                set[i] = set[i +1];
                set[i +1] = temp;
            }
        }
    }
    
    for(disp = 0; disp < size; disp++)
    {
        printf("%d\t", set[disp]);
    }        
    getchar();
    return 0;
}