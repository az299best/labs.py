def gen_bin_tree_non_recursive(height=3, root=5):
    tree = {
        'value': root,
        'left':  {},
        'right': {}
    }
    curr_level_nodes = [tree]
    while height > 1:
        child_level_nodes = []
        for node in curr_level_nodes:
            node['left'] = {
                'value': node['value'] * 2,
                'left': {},
                'right': {}
            }
            node['right'] = {
                'value': node['value'] + 3,
                'left': {},
                'right': {}
            }
            child_level_nodes.extend([node['left'], node['right']])
        height -= 1
        curr_level_nodes = child_level_nodes
    return tree


if __name__ == "__main__":
    non_recursive_bin_tree = gen_bin_tree_non_recursive()
    print(r"Non-Recursive: {}".format(non_recursive_bin_tree))