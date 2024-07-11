# Baby's First Forensics

## Description

They've been trying to breach our infrastructure all morning!
They're trying to get more info on our covert kangaroos! We need your help,
we've captured some traffic of them attacking us, can you tell us what tool
they were using and its version?

NOTE: Wrap your answer in the <code>DUCTF{}</code>, e.g. <code>DUCTF{nmap_7.25}</code>

## Attachments

[capture.pcap](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/forensics/BabysFirstForensics/attachments/capture.pcap)

## Solution

- I opened the PCAP file in [Wireshark](https://www.wireshark.org/), then clicked through Analyze->Follow->TCP Stream.
- The first block of text there, which you can view [here](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/forensics/BabysFirstForensics/wireshark_output.txt), revealed the tool the attackers used: **Nikto 2.1.6**. This was the flag.

## Flag

DUCTF{Nikto_2.1.6}
