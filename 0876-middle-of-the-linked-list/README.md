<h2><a href="https://leetcode.com/problems/middle-of-the-linked-list">908. Middle of the Linked List</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a singly linked list, return <em>the middle node of the linked list</em>.</p>

<p>If there are two middle nodes, return <strong>the second middle</strong> node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>

## My Approach
### Approach 1: Two-pass (count + traverse)
**Steps:**
1. Traverse the list to find total length
2. Traverse again till (count/2)th node. For even-length lists, this returns the second middle node (as question requires)
3. That will be the middle node of the linked list
**Complexity:** Time O(n), Space O(1). Two passes.
**When to use:** Easier to reason about, fine for most cases.
---

### Approach 2: One-pass (slow and fast pointers approach)
**Steps:**
1. Create both slow and fast start at head
2. Move fast two steps and slow one step
3. Move both together until fast is NULL
4. When fast is NULL slow will exactly point to the middle node - return it
**Complexity:** Time O(n), Space O(1). One pass.
**When to use:** When asked "can you do it in one pass?"
---

### Key insight
Fast moves 2 nodes per step, slow moves 1. By the time fast travels the full length n, slow has traveled exactly n/2 — landing on the middle. The two-condition loop check (fast != NULL && fast->next != NULL) handles both even and odd lengths cleanly.

### Related problems
- Linked List Cycle (same slow/fast technique)
- Palindrome Linked List (uses find-middle as a step)
- Linked List Cycle II
