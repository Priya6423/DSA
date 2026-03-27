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
    ListNode* middleNode(ListNode* head) {
    ListNode* temp=head;
    int cnt=0;
    while(temp){
    cnt++;
    temp=temp->next;
    }
    int target=cnt/2,count=0;
    while(count!=target){
    head=head->next;
    count++;
    }
    return head;
    }
};