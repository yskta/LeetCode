/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *mergedList = new ListNode();
        ListNode *head = mergedList;
        if (list1 == NULL && list2 == NULL)
            return NULL;
        if (list1 == NULL)
            return list2;
        if (list2 == NULL)
            return list1;
        while (list1 != NULL && list2 != NULL) {
            if (list1->val > list2->val) {
                mergedList->val = list2->val;
                list2 = list2->next;
                if (list2 != NULL) {
                    mergedList->next = new ListNode();
                    mergedList = mergedList->next;
                }
            } else {
                mergedList->val = list1->val;
                list1 = list1->next;
                if (list1 != NULL) {
                    mergedList->next = new ListNode();
                    mergedList = mergedList->next;
                }
            }
        }
        if (list1 != NULL || list2 != NULL){
            mergedList->next = new ListNode();
            mergedList = mergedList->next;
        }
        if (list1 != NULL){
            while (list1 != NULL) {
                mergedList->val = list1->val;
                list1 = list1->next;
                if (list1 != NULL) {
                    mergedList->next = new ListNode();
                    mergedList = mergedList->next;
                }
            }
        }
        else if (list2 != NULL){
            while (list2 != NULL) {
                mergedList->val = list2->val;
                list2 = list2->next;
                if (list2 != NULL) {
                    mergedList->next = new ListNode();
                    mergedList = mergedList->next;
                }
            }
        }
        return (head);
    }
};
// @lc code=end

