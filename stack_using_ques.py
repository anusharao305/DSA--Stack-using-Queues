#!/usr/bin/env python3
"""Stack implemented using two queues (Python version of your JS code).
Save as `stack_using_ques.py` and run with `python3 stack_using_ques.py`.
"""

from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # insert element
    def push(self, x):
        self.q1.append(x)

    # remove top element
    def pop(self):
        if not self.q1:
            return None

        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())

        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    # return top element
    def top(self):
        if not self.q1:
            return -1

        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())

        temp = self.q1.popleft()
        self.q2.append(temp)
        self.q1, self.q2 = self.q2, self.q1
        return temp

    # return current size
    def size(self):
        return len(self.q1)


# Driver Code
if __name__ == "__main__":
    st = MyStack()
    st.push(1)
    st.push(2)
    st.push(3)

    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    print(st.size())
