import numpy as np 




def langaas(ch3, ch4):
    '''
    Langaas 1993a
    20220831: not fully understood yet
    L3, L4: Combined temperature of fire and non-fire parts of a pixel
    p: fraction of a pixel occupied by fire
    L3(Tt): fire temperature
    L3(Tb): background temperature (Extracted from only night images)

    L3 = p*L3(Tt) + (1-p)*L3(Tb)
    L4 = p*L4(Tt) + (1-p)*L4(Tb)
    Known: L3, L4
    Find out: L3(Tb), L4(Tb), from surrounding non-fire pixels
    Solve for: p, L3(Tt), L4(Tt)
    '''
    return None
