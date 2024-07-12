# shufflebox

## Description

I've learned that if you shuffle your text, it's elrlay hrda to tlle htaw eht nioiglra nutpi aws.

Find the text censored with question marks in <code>output_censored.txt</code>
and surround it with <code>DUCTF{}</code>.

## Attachments

[shufflebox.py](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/crypto/shufflebox_UNFINISHED/attachments/shufflebox.py)

[output_censored.txt](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/crypto/shufflebox_UNFINISHED/attachments/output_censored.txt)

## Solution (Unfinished)

- I began by analyzing the code provided in <code>shufflebox.py</code>. The program takes in strings of length 16 and scrambles them using an array
called <code>PERM</code>. This array contains integers representing the indices of the characters in the original string in a random order.
- I wrote my own script called [unshuffle.py](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/crypto/shufflebox_UNFINISHED/unshuffle.py) in order to undo the scrambling described above. The only missing part was the <code>PERM</code> array itself from <code>shufflebox.py</code> (named <code>PERM_inverse</code> in my script for no real reason).
- This was where I got stuck. The <code>PERM</code> array is generated randomly, and I was not able to figure out the value it had that created the output in the <code>output_censored.txt</code> file that was provided. I attempted to find <code>PERM</code> through a brute force solution in a script I wrote called [recover_perm.py](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/crypto/shufflebox_UNFINISHED/recover_perm.py). Note that I did not write this code with optimization nor organization in mind, as it was thrown together toward the end of the competition.
- The important function in my script is <code>decodeFirst()</code>. It would first randomly shuffle the integers 0 through 15 to generate a candidate value for <code>PERM</code>. Next, it would apply the scrambling method that <code>shufflebox.py</code> did to the first string in <code>output_censored.txt</code>. My scramble would be compared to the actual scramble.
- The two scrambles are not likely to completely match after the first try, but there may be some individual characters that happen to match. This meant that I could save the integers in my <code>PERM</code> candidate that were correct and continue brute forcing the remaining integers.
- I continued this process until I had succeeded in generating a value for <code>PERM</code> that scrambled the first string the same way that <code>shufflebox.py</code> did. The function <code>decodeSecond()</code> does the same thing for the second string in <code>output_censored.txt</code>.
- Both of these functions could generate their own value for <code>PERM</code> very quickly. The catch was getting both functions to return the _same_
value for <code>PERM</code>, as that would very likely be the value that <code>shufflebox.py</code> used. There are **a lot** of <code>PERM</code> values that work just for each string individually.
- I set my script to continue using <code>decodeFirst()</code> and <code>decodeSecond()</code> to generate random arrays until they both generated the same one. Unfortunately, the time it would have taken this script to find the correct value was not realistic. I believe I could have instead written a single <code>decode()</code> function that used some more clever logic to pick which integers to save and which ones to continue brute forcing.
