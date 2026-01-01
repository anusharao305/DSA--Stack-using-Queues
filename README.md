# DSA--Stack-using-Queues
Depicts how to use Stack data structure to make Queue data structure. Stack follows LIFO (Last In, First Out) principle while Queue follows FIFO (First In, First Out) principle. 

Method:
Difference in rules between the two data structures requires FIFO to give output following LIFO principle.
This method uses two queues: push in O(n) and pop in O(1). The newly inserted element is kept at the front of queue q1 for easy access. Queue q2 is used to rearrange the elements during push().
