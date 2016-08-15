/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    
        ListNode dummy = new ListNode(0);
        ListNode p1 = l1;
        ListNode p2 = l2;
        //our new merged list
        ListNode head = dummy;
        
        while(p1 != null || p2 != null)
        {
            ListNode cur;
            
            if(p1 != null && p2 == null)
            {
                cur = p1;
                p1 = p1.next;
            }
            else if(p2 != null && p1 == null)
            {
                cur = p2;
                p2 = p2.next;
            }
            else if(p1.val < p2.val)
            {
                cur = p1;
                p1 = p1.next;
            }
            else
            {
                cur = p2;
                p2 = p2.next;
            }
            
            dummy.next = cur;
            dummy = dummy.next;
        }
        
        return head.next;
        
    }
}