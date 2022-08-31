import numpy as np 
from scipy.ndimage import generic_filter


def get_mu(arr):
    return np.mean(arr)

def get_sigma(arr):
    return np.std(arr)

def fd_flasse_ceccato(ch2, ch3, ch4, window_size = 5):
    '''
    Flasse and Ceccato 1996
    
    Consists of two stages

    Input: ch2, ch3, ch4, window_size 
        window_size is for stage-2. 
          Choose between 3 and 15
          and moving windows will be 3x3 to 15x15
    output: 1 for potential fire, 0 for no-fire
    '''
    # stage 1
    cond1 = ch3 >= 311
    cond2 = (ch3 - ch4) >= 8
    cond3 = ch2 <= 0.2 
    cond_sum1 = np.sum([cond1, cond2, cond3], axis = 0)
    cond_stage1  = np.where(cond_sum1 > 0, 1, 0)

    # stage 2
    ws = window_size
    ## get potential fire values
    pf_tdiff = (ch3 - ch4) * cond_stage1
    pf_ch3 = ch3 * cond_stage1
    ## get mu and sigma as conditions
    mu_tdiff = generic_filter((ch3 - ch4), function = get_mu, 
                         size = (ws, ws), mode = 'nearest')
    sigma_tdiff = generic_filter((ch3 - ch4), function = get_sigma, 
                         size = (ws, ws), mode = 'nearest')
    mu_ch3 = generic_filter(ch3, function = get_mu, 
                         size = (ws, ws), mode = 'nearest')
    sigma_ch3 = generic_filter(ch3, function = get_sigma, 
                         size = (ws, ws), mode = 'nearest')
    ## calculate
    s2_cond1 = pf_tdiff > (mu_tdiff + sigma_tdiff)
    s2_cond2 = (pf_ch3 - (mu_ch3 + 2 * sigma_ch3)) > 3

    final_cond = np.sum([s2_cond1, s2_cond2], axis = 0)
    output = np.where(final_cond > 0, 1, 0)
    
    return output