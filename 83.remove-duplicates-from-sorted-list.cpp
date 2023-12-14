/*
 * @lc app=leetcode id=83 lang=cpp
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *preserveNode;
        ListNode *currentNode;
        preserveNode = head;
        currentNode = head;
        while (currentNode != NULL)
        {
            if (currentNode->next != NULL && currentNode->val < currentNode->next->val){
                preserveNode->next = currentNode->next;
                preserveNode = preserveNode->next;
            }
            else if (currentNode->next == NULL){
                preserveNode->next = NULL;
            }
            currentNode = currentNode->next;
        }
        return head;
    }
};
// @lc code=end

