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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
    ListNode* beforeA=list1;
    ListNode* temp1=list2;
    for(int i=0;i<a-1;i++){
    beforeA=beforeA->next;
    }
    ListNode* AfterB=beforeA;
    for(int i=0;i<b-a+2;i++){
    AfterB=AfterB->next;
    }
    while(temp1->next!=NULL){
    temp1=temp1->next;
    }
    beforeA->next=list2;
    temp1->next=AfterB;
    return list1;  
    }
};