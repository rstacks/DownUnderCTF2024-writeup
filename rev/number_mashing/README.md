# number mashing

## Description

Mash your keyboard numpad in a specific order and a flag might just pop out!

<code>nc 2024.ductf.dev 30014</code> 

## Attachments

number-mashing

## Solution

We are given an executable to analyze. I uploaded it to the decompiler explorer at
dogbolt.org and examined the Ghidra output. The most notable section was the main() function
of the decompiled code. You can view important segments of this function here. The program
accepts input from the user for two integers.

In order to get the flag, certain conditions must be met: the first integer (local_11c) cannot be 0,
the second integer (local_118) cannot be 0 nor 1, and the following equation must be true:
local_11c = local_11c / local_118.

It is not possible for the final condition to be true under the regular
rules of math with the constraints of the first two conditions. We can, however, take advantage
of how C/C++ handles integer overflow. The minimum and maximum values of a 32-bit int in C/C++ are
-2147483648 and 2147483647, respectively.

With this knowledge, I tried -2147483648 and -1 as my pair of input values. The first two conditions
hold true with this pair. When the program attempts to do local_11c / local_118, the result will be
2147483648. This, however, is greater than the maximum value of a 32-bit int. So, it will overflow
to -2147483648, which is indeed the value of local_11c. Entering these values as input yielded the
flag.

## Flag

DUCTF{w0w_y0u_just_br0ke_math!!}
