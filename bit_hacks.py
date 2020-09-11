# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:36:33 2020

@author: LG
"""

# bit hacks from mit
#01
def set_bit_to_1(number, k_position): # shift, or
     #10111101 0 1101101 = number
     #10111101 1 1101101 = answer                                  
    ans = 1<<k_position
    y = ans | number
    return y

#02
def set_bit_to_0(number, k_position): # shift, complement, and
    #10111101 1 1101101 number
    #10111101 0 1101101 answer
    ans = ~(1<<k_position)
    y = ans & number
    return y

#03
def toggle_kth_bit(number, k_position): # shift, xor
    # if 1 then make it 0
    # else make it 1
    # 10111101 1 1101101 number
    # 10111101 0 1101101 answer
    ans = 1<<k_position
    y = number ^ ans
    return y

    

#04
def extract_bit_field(number, k_position): # mask and shift
    # extract 4 digits at kth positon from binary form
    #10111 1010 1101101 number
    # 1010 answer
    mask = 15<<k_position
    y = mask & number
    return y>>k_position


#05
def set_bit_field(number, k_position): # invert mask to clear, and OR the shift value
    y = 3 # set this value in number
    mask = ~(15<<k_position)
    a = (y<<k_position) # for safty esle y<<k_position is fine

    return (number & mask) | a
    



number = 48493
k_position = 7
print(bin(set_bit_field(number, k_position)))

