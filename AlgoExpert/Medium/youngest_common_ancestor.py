# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    stack_one = []
    stack_two = []

    while descendantOne.name != topAncestor.name:
        stack_one.append(descendantOne)
        descendantOne = descendantOne.ancestor

    while descendantTwo.name != topAncestor.name:
        stack_two.append(descendantTwo)
        descendantTwo = descendantTwo.ancestor

    youngest_common_found = None

    while stack_one or stack_two:
        
        if stack_one:
            one_to_compare = stack_one.pop()
        else:
            one_to_compare = AncestralTree("")
        
        if stack_two:
            two_to_compare = stack_two.pop()
        else:
            two_to_compare = AncestralTree("")

        if one_to_compare.name == two_to_compare.name:
            youngest_common_found = two_to_compare
    
    return youngest_common_found if youngest_common_found else topAncestor

# node_a = AncestralTree("A", None)
# node_b = AncestralTree("B", node_a)
# node_e = AncestralTree("E", node_b)
# node_d = AncestralTree("D", node_b)
# node_i = AncestralTree("I", node_d)


# getYoungestCommonAncestor(node_a, node_e, node_i)