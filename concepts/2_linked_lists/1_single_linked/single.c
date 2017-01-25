// gcc -o single single.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
	int data;
	struct node *next;
};

struct node *head = NULL;
struct node *current = NULL;

void printList() {
	struct node *ptr = head;
	while(ptr != NULL) {
		printf("%d ",ptr->data);
		ptr = ptr->next;
	}
	printf("\n");
}

// check if list is empty (only need to check head)
bool checkEmpty() {
	return head == NULL;
}

// insert value at beginning of list
void insertStart(int data) {
	// create node and allocate space
	struct node *temp = (struct node*) malloc(sizeof(struct node));

	// update data
	temp->data = data;

	// update next
	temp->next = head;

	// update head
	head = temp;
}

// delete first node
void deleteFirst() {
	struct node *current = head;

	if (current->next != NULL) {
		head = current->next;
	} else {
		head = NULL;
	}

	free(current);
}

void deleteValue(int data) {
	struct node *current = head;

	if ( checkEmpty() ) { // current or empty
		return;
	} else if (current->data == data) { // first
		deleteFirst();
	}

	// steps: update pointer (if value exists), free space
	while(current->next != NULL) {
		if (current->next->data == data) {
			if (current->next->next != NULL) {
				current->next = current->next->next;
			} else {
				current->next = NULL;
			}
			free(current->next);
		}
		current = current->next;
	}

}

int main() {
	printf("Start \n");

	if ( checkEmpty() ) {
		printf("Empty\n");
	} else {
		printf("Not empty\n");
	}

	insertStart(6); // causes seg fault
	insertStart(2);
	insertStart(4);
	insertStart(6);
	insertStart(8);
	insertStart(6);
	insertStart(100);
	insertStart(6); // causes seg fault

	printList();

	if ( checkEmpty() ) {
		printf("Empty\n");
	} else {
		printf("Not empty\n");
	}

	deleteFirst();
	deleteValue(6);

	printList();

	printf("End \n");

	return 0;
}
