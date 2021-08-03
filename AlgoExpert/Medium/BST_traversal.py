def inOrderTraverse(tree, array):
	if not tree:
		return array
	
	inOrderTraverse(tree.left, array)
	array.append(tree.value)
	inOrderTraverse(tree.right, array)
	
	return array

def preOrderTraverse(tree, array):
    if not tree:
        return array
        
    array.append(tree.value)    
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
	if not tree:
		return array
	
	postOrderTraverse(tree.left, array)
	postOrderTraverse(tree.right, array)
	array.append(tree.value)

	return array
