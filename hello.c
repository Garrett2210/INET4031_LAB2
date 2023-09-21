#include <stdio.h>
              
               int main() {
                 char *users[] = {"User1", "User2", "User3"};
		 int size = sizeof(users) / sizeof(users[0]);
                 int a = 2;
                 int b = 2;
                 int c = a + b;
              
                 printf("C says: Hello, World!\n");
                 printf("%d + %d = %d\n",a,b,c);
              	 
		 for(int i = 0; i < size; i++){
			printf("%s\n", users[i]);
		}
                 return 0;
               }
