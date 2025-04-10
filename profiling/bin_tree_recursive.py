def gen_bin_tree_recursive(height=3, root=5):
    if height < 1:
        return {}
    node = {
        'value': root,
        'left':  {},
        'right': {}
    }
    node['left']  = gen_bin_tree_recursive(height - 1, root * 2)
    node['right'] = gen_bin_tree_recursive(height - 1, root + 3)
    return node


if __name__ == "__main__":
    recursive_bin_tree = gen_bin_tree_recursive()
    print(r"Recursive: {}".format(recursive_bin_tree))