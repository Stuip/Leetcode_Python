class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

#  将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow ,fast = head, head
        while fast and fast.next: # 寻找中间指针
            slow = slow.next
            fast = fast.next.next
        stack = list()
        mid = slow
        while slow:  # 后半部分压入栈中
            stack.append(slow.val)
            slow = slow.next
        while head != mid:
            num = stack.pop()
            if head.val != num:
                return False
            head = head.next
        return True


if __name__ == '__main__':
    arr = [1, 2, 2, 1]
    head = create_linked_list(arr)
    s = Solution()
    result = s.isPalindrome(head)
    print(result)