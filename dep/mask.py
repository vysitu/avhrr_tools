import numpy as np

qa_dict = {
    0: "Unused",
    1: "Pixel is cloudy",
    2: "Pixel contains cloud shadow",
    3: "Pixel is over water",
    4: "Pixel is over sunglint",
    5: "Pixel is over dense dark vegetation",
    6: "Pixel is at night (high solar zenith)",
    7: "Channels 1-5 are valid",
    8: "Channel 1 value is invalid",
    9: "Channel 2 value is invalid",
    10: "Channel 3 value is invalid",
    11: "Channel 4 value is invalid",
    12: "Channel 5 value is invalid",
    13: "RHO3 value is invalid",
    14: "BRDF correction is invalid",
    15: "Polar flag, latitude over 60 degrees (land) or 50 degrees (ocean)",
    }

bit_dict = {
    'unused':0,
    'cloud':1,
    'cloud_shadow':2,
    'water':3,
    'sunglint':4,
    'dark_vegetation':5,
    'night':6,
    'ch1-5_valid':7,
    'ch1_invalid':8,
    'ch2_invalid':9,
    'ch3_invalid':10,
    'ch4_invalid':11,
    'ch5_invalid':12,
    'rho3_invalid':13,
    'brdf_invalid':14,
    'polar':15
    }


def binary_padding(input1, width = 0):
    """
    convert the input integer into a binary string starting with '0b'; 
      and pad the binary to the given length
      
    input1: the integer to be converted
    width: the padding length. Default is 0, which means no padding.
      if the given width is shorter than the converted string length, 
      no padding will be applied.
    """
    temp1 = bin(input1)[2:]
    if len(temp1)>=width:
        return '0b'+temp1
    else:
        temp2 = (width - len(temp1))*'0'+temp1
        return '0b'+temp2
    
def binary_interpret(binary_str):
    """
    Print out which masks are applied 
    
    binary_str: a binary string starting with '0b'
    """
    for i,k in enumerate(binary_str[2:]):
        if k == "1":
            print(qa_dict[i])
        else:
            continue
            
def bitmask_unpack(qa_arr, width=16):
    """
    Unpacks a n-bit mask into n layers of mask.
    
    qa_arr: n-bit mask array, shape (x, y), max value 2^n-1, min value 0
    width: number of bits (n), default is 16
    
    output: 0/1 mask array, shape (n, x, y)
    """
    mask_arr = np.zeros((width, qa_arr.shape[0], qa_arr.shape[1]))
    for shift in range(width):
        bit_arr = np.right_shift(qa_arr, shift) % 2
        mask_arr[shift, :, :] = bit_arr
    return(mask_arr)

def bit2mask(qa_band, bit_list, output = 'valid'):
    """
    qa_band: a numpy array
    bit_list, a list of bits to mask
        e.g. [1,2] means create cloud and cloud shadow mask
    
    return: mask array, default: 0 means masked, 1 means not masked (valid)
        e.g. cloudy pixels have bit_1=1, then in the output the corresponding pixel is 0
    """
    cond = np.zeros_like(qa_band)
    for bit in bit_list:
        t_cond = np.right_shift(qa_band, bit) % 2
        cond += t_cond
    if output == 'valid':
        mask = np.where(cond > 0, 0, 1)
    elif output == 'mask':
        mask = np.where(cond > 0, 1, 0)
    return mask