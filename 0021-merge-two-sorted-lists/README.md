<h2><a href="https://leetcode.com/problems/merge-two-sorted-lists">21. Merge Two Sorted Lists</a></h2><h3>Easy</h3><hr><p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>

<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>Return <em>the head of the merged linked list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>Input:</strong> list1 = [1,2,4], list2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>Both <code>list1</code> and <code>list2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>

## My Approach

**Pattern used:** Dummy node + tail pointer

**Steps:**
1. Take a new node named dummy and a tail node. Assign dummy to tail node.Dummy should not be null because the tail is a moving pointer and it will crash.
2. Now start comparing the node values of both the lists and assign the lower value to the tail->next and move tail to next pointer(tail = tail->next) and also move the list to next pointer.
3. Since both the lists are not of same length we need to ensure no values of both the lists are left behind
4. AAfter the loop, exactly one list may have leftover nodes. Attach that remaining chain to tail in one step (it's already sorted and larger than everything merged so far).
5. Now return dummy->next 

**Complexity:** Time O(n+m), Space O(1)

**Key insight:**
The tail is the moving node. Eventually Tail will be lost at the tail of the merged list so, we need a pointer that will point to the head so that we can easily return the head after merging. That is why we use dummy node. The dummy node will point to the head.

**Bug I made:**
- Initially I took dummy=NULL instead of new ListNode(0) which returned error
- I returned the dummy->next inside the while loop accidentally
- I typed List1 instead of list1
  
**Rule I learned**:
whenever the head node might be lost, changed, or removed during the operation, use a dummy node.

**Related problems:**
- Remove Nth node From End
