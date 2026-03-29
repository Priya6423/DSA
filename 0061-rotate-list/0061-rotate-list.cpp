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
    ListNode* rotateRight(ListNode* head, int k) {
     ListNode* temp=head;
     if(head==NULL) return head;
        int length=1;
        while(temp->next!=NULL){
        temp=temp->next;
        length++;
        }
        k=k%length;
        if(k==0){
        return head;
        }
        ListNode* temp1=head;
        int count=0;
        while(count!=(length-k-1)){
        temp1=temp1->next;
        count++;
        }
        ListNode* tail=temp1;
        temp->next=head;
        head=temp1->next;
        tail->next=NULL;
        return head;
    }
};