<h2><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list">19. Remove Nth Node From End of List</a></h2><h3>Medium</h3><hr><p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do this in one pass?</p>
---
## My Approach

### Approach 1: Two-pass (count + traverse)
**Steps:**
1. Traverse the list to find total length
2. Traverse again to (length - n - 1)
3. Skip the target node

**Complexity:** Time O(L), Space O(1). Two passes.

**When to use:** Easier to reason about, fine for most cases.

---

### Approach 2: One-pass (two pointers with gap)
**Steps:**
1. Create dummy node, both slow and fast start at dummy
2. Move fast ahead by n+1 steps
3. Move both together until fast is NULL
4. Slow is now before the target — skip it

**Complexity:** Time O(L), Space O(1). One pass.

**When to use:** When asked "can you do it in one pass?"

---

### Key insight
Moving fast ahead by n+1 steps creates a gap of n+1 nodes between slow and fast.
When both move together and fast reaches NULL, slow lands exactly at the node
*before* the target. From there, we can skip the target with one assignment:
`slow->next = slow->next->next`.
If we moved fast by just n (not n+1), slow would land *on* the target itself —
but we need to be one step before to perform the deletion.

### Bug I made
Initially I didn't use a dummy node and started traversal from head. This crashed
on test cases where the head itself needed to be removed (e.g., `head=[1,2], n=2`)
— there's no node before the head to update.

After adding a dummy node, even head removal had a *previous* node (the dummy)
to rely on. Just `return dummy->next` at the end to get the new head.

### Related problems
- Merge Two Sorted Lists (also uses dummy node)
- Middle of Linked List (also two-pass vs one-pass tradeoff)
