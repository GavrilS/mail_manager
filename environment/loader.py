def load_env_variables(file):
    with open(file, 'r') as f:
        variables = f.readlines()
    
    print('Loaded variables: ', variables)
    return variables
