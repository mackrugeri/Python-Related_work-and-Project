class Node:
    def __init__(self, keys, children):
        self.keys = keys 
        self.children = children 
        self.str_pos = None


    def num_keys(self):
        return len(self.keys)


    def num_children(self):
        return len(self.children)


    def is_leaf(self):
        return self.num_children() == 0


    def search(self, key):
        left = 0 
        right = self.num_keys()
        while right > left:
            mid = (left + right)//2
            if self.keys[mid] >= key:
                right = mid
            else:
                left = mid + 1
        return left


    def linear_search(self, key):
        index = 0
        while index < self.num_keys() and self.keys[index] < key:
            index += 1
        return index


    def contains_key_at(self, key, index):
        return index < self.num_keys() and self.keys[index] == key


    def deep_min(self):
        node = self
        while not node.is_leaf():
            node = node.children[0]
        return node.keys[0] if node.keys else None


    def deep_max(self):
        node = self
        while not node.is_leaf():
            node = node.children[-1]
        return node.keys[-1] if node.keys else None


    def locate_predecessor(self, key):
        index = self.search(key)
        return index-1


    def predecessor(self, key):
        index = self.locate_predecessor(key)
        return self.keys[index] if index >= 0 else None


    def deep_predecessor(self, index):
        return self.children[index].deep_max()


    def locate_successor(self, key):
        index = 0
        while index < self.num_keys() and self.keys[index] <= key:
            index += 1
        return index


    def successor(self, key):
        index = self.locate_successor(key)
        self.keys[index] if index < self.num_keys() else None


    def deep_successor(self, index):
        return self.children[index+1].deep_min()
        

    def insert(self, key):
        index = self.search(key)
        self.keys.insert(index, key)


    def delete(self, key):
        index = self.search(key)
        if self.contains_key_at(key, index):
            del self.keys[index]


    def split_child(self, index):
        child = self.children[index]
        median = (child.num_keys())//2
        median_key = child.keys[median]

        left  = Node(child.keys[:median], child.children[:median + 1])
        right = Node(child.keys[median + 1:], child.children[median + 1:])

        self.keys.insert(index, median_key)
        self.children[index:index+1] = [left, right]


    def merge_children(self, index):
        median_key = self.keys[index]
        left, right = self.children[index : index+2]

        left.keys.append(median_key)
        left.keys.extend(right.keys)

        if not right.is_leaf():
            left.children.extend(right.children)

        del self.keys[index]
        del self.children[index+1]

        merged = left

        if self.num_keys() == 0:
            self.keys = left.keys
            self.children = left.children
            merged = self

        return merged 


    def grow_child(self, index, min_num_keys):
        child = self.children[index]
        left_sibling = (index > 0) and self.children[index-1]
        right_sibling = (index < self.num_keys()) and self.children[index+1]

        if left_sibling and left_sibling.num_keys() > min_num_keys:
            self.transfer_key_clockwise(index-1)

        elif right_sibling and right_sibling.num_keys() > min_num_keys:
            self.transfer_key_counter_clockwise(index)

        else:
            shared_key_index = (index - 1) if left_sibling else index
            child = self.merge_children(shared_key_index)

        return child 


    def transfer_key_clockwise(self, index):
        left, right = self.children[index : index+2]
        right.keys.insert(0, self.keys[index])

        if left.children:
            right.children.insert(0, left.children[-1])
            del left.children[-1]

        self.keys[index] = left.keys[-1]
        del left.keys[-1]


    def transfer_key_counter_clockwise(self, index):
        left, right = self.children[index : index+2]
        left.keys.append(self.keys[index])

        if not right.is_leaf():
            left.children.append(right.children[0])
            del right.children[0]

        self.keys[index] = right.keys[0]
        del right.keys[0]




class B_Tree:
    """
    B-Tree data structure.
    """

    def __init__(self, degree):
        self.root = Node([], [])
        self.min_num_keys = degree - 1 
        self.max_num_keys = 2*degree - 1


    def insert(self, key):
        print("The key "+ str(key) + " is insert into B_Tree")
        if self.root.num_keys() == self.max_num_keys:
            self.root = Node([], [self.root])
            self.root.split_child(0)

        node = self.root 
        while not node.is_leaf():
            index = node.search(key)
            child = node.children[index]
            if child.num_keys() == self.max_num_keys:
                node.split_child(index)

                if node.keys[index] < key:
                    index += 1

            node = node.children[index] 

        node.insert(key)

    def delete(self, key):
        print ("The value " + str(key)+" is delete as shown below")
        node = self.root
        while not node.is_leaf():
            index = node.search(key)

            if node.contains_key_at(key, index):
                left, right = node.children[index : index+2]

                if left.num_keys() > self.min_num_keys:
                    node.keys[index] = node.deep_predecessor(index)
                    (node, key) = (left, node.keys[index])

                elif right.num_keys() > self.min_num_keys:
                    node.keys[index] = node.deep_successor(index) 
                    (node, key) = (right, node.keys[index])

                else:
                    node = node.merge_children(index)

            else:
                child = node.children[index]
                if child.num_keys() <= self.min_num_keys:
                   child = node.grow_child(index, self.min_num_keys)
                node = child
                    
        node.delete(key)

    def inorder(self):

        print("--------------------- Veiw of b- tree------------------------")
        """
        Generates the keys of the b-tree in non-decreasing order.
        """
        queue = []
        node = self.root
        index = 0
        while node:

            if node.is_leaf():
                print("The value recived is " + str(node.keys))
                print("----")
                # return (node.keys)

                if not queue:
                    node = None

                else:
                    node, index = queue.pop()
                    print("The value reciving  is " + str(node.keys[index]))
                    print("----")
                    # return node.keys[index]
                    index = index + 1

            else:
                if index < node.num_keys():
                    queue.append((node, index))
                    # print(queue)

                node = node.children[index]
                index = 0


bt = B_Tree(2)
bt.insert(25)
bt.inorder()
bt.insert(30)
bt.inorder()
bt.insert(35)
bt.inorder()
bt.insert(40)
bt.inorder()
bt.insert(45)
bt.inorder()
bt.delete(25)
bt.inorder()
