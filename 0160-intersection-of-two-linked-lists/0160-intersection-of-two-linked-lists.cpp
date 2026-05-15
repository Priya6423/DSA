/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    ListNode* temp1=headA;
    ListNode* temp2=headB;
    int count1=0,count2=0;
    while(temp1!=NULL){
    count1++;
    temp1=temp1->next;
    }
    while(temp2!=NULL){
    count2++;
    temp2=temp2->next;
    }
    ListNode* list1=headA;
    ListNode* list2=headB;
    if(count1>count2){
    int diff=count1-count2;
    while(diff){
    list1=list1->next;
    diff--;
    }
    }else{
    int diff=count2-count1;
    while(diff){
    list2=list2->next;
    diff--;
    }
    }
    ListNode* a=list1;
    ListNode* b=list2;
    while(a!=NULL && b!=NULL){
    if(a==b) return a;
    a=a->next;
    b=b->next;
    }
    return NULL;
    }
};