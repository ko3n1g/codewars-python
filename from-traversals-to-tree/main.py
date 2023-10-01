"""Problem description:

Challenge to be found at: URL(https://www.codewars.com/kata/651478c7ba373c338a173de6)

In-order-traversal:

1. Left child
2. Value
3. Right child

Post-order traversal:

1. Left child
2. Right child
3. Value

"""

from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        child_str = (
            ""
            if (self.left is None and self.right is None)
            else f",{self.left},{self.right}"
        )
        return f"{self.__class__.__name__}({self.value}{child_str})"


def build_tree(inorder: List[int] = [], postorder: List[int] = []) -> TreeNode:
    """Typically it is not safe to create an list object as default value since that would be created at
    runtime and not function-call time. But for this context it is okay since this function is only being
    called once per runtime and we want to point to this list in the recursive call stack.
    """

    # Since the post-order traversal captures the nodes value after traversing it’s children, it is
    # clear that the root node must correspond to the last item of the post-order traversal list.
    if not len(postorder):
        return None

    root_el = postorder.pop(-1)

    # Since all nodes are unique, we now know the direct children of the root by the in-order traversal
    left_in_order_child_nodes = inorder[: inorder.index(root_el)]
    left_post_order_child_nodes = postorder[: inorder.index(root_el)]

    right_in_order_child_nodes = inorder[inorder.index(root_el) + 1 :]
    # `+1` not necessary since the element does not exist in this list
    right_post_order_child_nodes = postorder[inorder.index(root_el) :]

    return TreeNode(
        value=root_el,
        left=(
            build_tree(
                inorder=left_in_order_child_nodes,
                postorder=left_post_order_child_nodes,
            )
        ),
        right=(
            build_tree(
                inorder=right_in_order_child_nodes,
                postorder=right_post_order_child_nodes,
            )
        ),
    )


if __name__ == "__main__":
    tn = build_tree(inorder=[4, 2, 1, 5, 3, 6], postorder=[4, 2, 5, 6, 3, 1])
    print(tn)
