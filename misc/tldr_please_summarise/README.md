# tldr please summarise

## Description

I thought I was being 1337 by asking AI to help me solve challenges, now I have to reinstall
Windows again. Can you help me out by find the flag in this document?

## Attachments

[EmuWar.docx](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/misc/tldr_please_summarise/attachments/EmuWar.docx)

## Solution

- I opened the provided document in Google Docs. I tried searching for the words "flag" or "DUCTF,"
but came up empty handed. There wasn't anything unusual about the document's metadata, and there
didn't seem to be any files hidden inside of the document.
- I returned to the document and selected all of the content with Ctrl+A. This revealed some very small text on the 3rd page with the same
color as the background. That text can be found [here](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/misc/tldr_please_summarise/foundit.txt).
- Running the given commands revealed the flag, as shown in the command output [here](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/misc/tldr_please_summarise/command_output.txt).

## Flag

DUCTF{chatgpt_I_n33d_2_3scap3}
