// gcc -o single single.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
	int data;
	int key;
	struct node *next;
};

struct node *head = NULL;
struct node *current = NULL;

int main(void) {
	printf("Original List: ");
	printf("Coming Soon!\n");
	return 0;
}
