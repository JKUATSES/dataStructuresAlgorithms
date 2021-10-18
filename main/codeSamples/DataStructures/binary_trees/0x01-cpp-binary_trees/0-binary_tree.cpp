#include <stdlib.h>
#include <iostream>

using namespace std;

struct node
{
	int data;
	struct node *left;
	struct node *right;
};

// New node creation
struct node *newNode(int data)
{
	struct node *node = (struct node *)malloc(sizeof(struct node));

	node->data = data;

	node->left = NULL;
	node->right = NULL;
	return (node);
}

void addNode(struct node** root, int data)
{
	if (*root == NULL)
	{
		*root = newNode(data);
	}
	else
	{
		if ((*root)->data > data)
		{
			if ((*root)->left != NULL)
				addNode(&(*root)->left, data);
			else
				(*root)->left = newNode(data);
		}
		else
		{
			if ((*root)->right != NULL)
				addNode(&(*root)->right, data);
			else
				(*root)->right =  newNode(data);
		}
	}
}

void _printBinaryTree(struct node *node)
{
	if (node != NULL)
	{
		_printBinaryTree(node->left);
		cout << node->data << " is a value held in a node" << endl;
		_printBinaryTree(node->right);
	}
}

void printBinaryTree(struct node *root)
{
	if (root != NULL)
		_printBinaryTree(root);
	else
		cout << "The Binary Tree is empty" << endl;
}

// Traverse Preorder
void traversePreOrder(struct node *node) {
	if (node != NULL)
	{
		cout << " " << node->data;
		traversePreOrder(node->left);
		traversePreOrder(node->right);
	}
}

// Traverse Inorder
void traverseInOrder(struct node *node) {
	if (node != NULL)
	{
		traverseInOrder(node->left);
		cout << " " << node->data;
		traverseInOrder(node->right);
	}
}

// Traverse Postorder
void traversePostOrder(struct node *node) {
	if (node != NULL) {
		traversePostOrder(node->left);
		traversePostOrder(node->right);
		cout << " " << node->data;
	}
}



int main()
{
	struct node* root = NULL;

	addNode(&root, 5);
	addNode(&root, 2);
	addNode(&root, 8);
	addNode(&root, 4);
	addNode(&root, 1);
	addNode(&root, 7);
	addNode(&root, 12);
	addNode(&root, 19);
	addNode(&root, 33);
	addNode(&root, 6);

	cout << "------- Start of Binary Tree -------\n" << endl;
	printBinaryTree(root);
	cout << "\n------- End of Binary Tree -------\n" << endl;

	cout << "\n------- Preorder traversal ---------" << endl;
	traversePreOrder(root);
	cout << "\n\n------- Inorder traversal ----------" << endl;
	traverseInOrder(root);
	cout << "\n\n------- Postorder traversal -------- " << endl;
	traversePostOrder(root);
	cout << "" << endl;

	return (0);
}
