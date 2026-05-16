<h2><a href="https://leetcode.com/problems/palindrome-linked-list">234. Palindrome Linked List</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a singly linked list, return <code>true</code><em> if it is a </em><span data-keyword="palindrome-sequence"><em>palindrome</em></span><em> or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?

## My Approach

**Pattern used:** slow/fast (find middle) + three-pointer (reverse second half) + two-pointer compare

**Steps:**
1.First find the middle of the list using slow and fast pointers
2.Then reverse the List from the middle node using the three pointers 
3.Then compare the first half and the reversed half 
4. If any single pair differs → not a palindrome, return false immediately. If you get through all pairs with every pair matching → return true

**Complexity:** Time O(n), Space O(1)

**Key insight:**
The usual way to check a palindrome is to copy all values into an array/vector, then check if the array reads the same forwards and backwards — that's O(n) space. The clever trick here is reversing the second half in place, so you compare both halves directly using only pointers — O(1) space

**Bug I made:**
No bug — solved cleanly by combining patterns already practiced (reverse + find middle).

**Related problems:**
-Reverse Linked List (used as a sub-step)
-Middle of Linked List (used as a sub-step)

 **note**:
 this destroys the original list; to restore, reverse the second half again before returning
