import numpy as np 




def fd_kaufman(ch3, ch4):
    '''
    Kaufman et al. 1990 
    Originally developed for fires in the Brazilian forests.
    input: ch3, ch4
    output: 1 for potential fire, 0 for no-fire
    '''

    cond1 = (ch3 >= 316)
    cond2 = ((ch3 - ch4) >= 10)
    cond3 = (ch4 >= 250)

    cond = np.sum([cond1, cond2, cond3], axis = 0)
    cond_out = np.where(cond > 0, 1, 0)

    return cond_out