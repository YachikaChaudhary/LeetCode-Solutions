/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        //beforeLeftNode => bL
        //leftNode => lN 
        if(head.next == null || left == right) return head;

        //finding bL and lN
        ListNode bL = head, lN = head;
        for(int i = 1; i < left; i++) {
            bL = lN;
            lN = lN.next;
        }

        //reverse logic
        ListNode curr = head, prev = null;
        for(int i = 1; i <= right; i++) {
            if(i >= left) {
                ListNode next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
                continue;
            }
            prev = curr;
            curr = curr.next;
        }

        //edge case : when left == 1
        if(left == 1) {
            head = prev;
        }else {
            bL.next = prev;
        }


        lN.next = curr;
        return head;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna