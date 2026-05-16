<h2><a href="https://leetcode.com/problems/reverse-linked-list">206. Reverse Linked List</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a singly linked list, reverse the list, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> A linked list can be reversed either iteratively or recursively. Could you implement both?</p>

## My Approach
### Approach 1: Three pointers
**Steps:**
1. Create prev node and assign NULL to it, then current node and assign head to it
2. Iterate through the list and take the third node called forward and assign current->next to it
3. As we move forward assign current->next to prev node, and move prev to current and current to forward
4. Forward will be automatically updated since we initialized it inside the loop and its value is current->next
5. When current reaches NULL, the loop ends. prev now points to the new head — return it.
**Complexity:** Time O(L), Space O(1). One pass.
---
### Key insight
You can't flip a pointer without first saving what it was pointing to.
`forward` is the safety net that lets us walk the list after we break each link.

### Related problems
- Palindrome Linked List (uses reversal as a step)
- Reverse Linked List II — reverse between positions m and n
- Reverse Nodes in K-Group
