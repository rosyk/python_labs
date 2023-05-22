import printing_imitation as prim

if __name__ == '__main__':
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    prim.print_models(unprinted_designs, completed_models)
    prim.show_completed_models(completed_models)
