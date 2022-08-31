import numpy as np 





def fd_arino_melinotte(ch1, ch2, ch3, ch4):
    '''
    Arino and Melinotte 1998 



    '''
    cond1 = ch3 >= 320 
    cond2 = (ch3 - ch4) > 15 
    cond3 = ch4 > 245 
    cond4 = ch1 < 0.25 
    cond5 = (ch1 - ch2) > 0.01 
    
    # cond6
    cond6 = np.ones_like(cond5)  # temporary fix

    # cond7 
    ndvi = (ch2 - ch1)/(ch2 + ch1)
    cond7 = ndvi > 0.08 

    cond_sum = np.sum([cond1, cond2, cond3, 
            cond4, cond5, cond6, cond7], axis = 0)
    cond = np.where(cond_sum > 0, 1, 0)

    return cond