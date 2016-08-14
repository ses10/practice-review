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
        
        //our new merged list
        ListNode head = null;
        ListNode p1 = l1;
        ListNode p2 = l2;
        
        //splice together both lists
        while(p1 != null || p2 != null)
        {
            if(p1 != null && p2 == null)
            {
                head = addN(head, p1.val);
                p1 = p1.next;
            }
            else if(p2 != null && p1 == null)
            {
                head = addN(head, p2.val);
                p2 = p2.next;
            }
            else if(p1.val < p2.val)
            {
                head = addN(head, p1.val);
                p1 = p1.next;
            }
            else
            {
                head = addN(head, p2.val);
                p2 = p2.next;
            }
        }

        //because of the way linked list insert nodes we need to reverse it
        head = revList(head);
        
        return head;
        
    }
    
    public ListNode addN(ListNode head, int val)
    {
        ListNode node = new ListNode(val);
        
        if(head == null)
            head = node;
        else
        {
            node.next = head;
            head = node;
        }
        
        return head;
        
    }
    
    public ListNode revList(ListNode head)
    {
        if(head == null)
            return head;
        else if(head.next == null)
            return head;
        
        ListNode prev = null;
        ListNode mid = head;
        ListNode next = head.next;
        
        while(true)
        {
            mid.next = prev;
            prev = mid;
            mid = next;
            if(mid == null)
                break;
            next = next.next;
            
        }
        return prev;
    }
}