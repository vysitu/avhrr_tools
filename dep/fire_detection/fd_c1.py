# Author: Yuhua Situ
# Date: 2022-08-31
# For AVHRR
# Fire detection algorithms collection 1

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


def fd_kennedy(ch2, ch3, ch4 ):
    '''
    Kennedy et al. 1994

    Originally for fire detection in West Africa

    Input: ch2, ch3, ch4
    output: 1 for potential fire, 0 for no-fire
    '''
    cond1 = ch3 >= 320
    cond2 = ((ch3 - ch4) >= 15)
    cond3 = (ch4 >= 295)
    cond4 = (ch2 <= 0.16)

    cond = np.sum([cond1, cond2, cond3, cond4], axis = 0)
    cond_out = np.where(cond > 0, 1, 0)

    return cond_out