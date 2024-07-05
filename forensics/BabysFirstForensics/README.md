# Baby's First Forensics

## Description

They've been trying to breach our infrastructure all morning!
They're trying to get more info on our covert kangaroos! We need your help,
we've captured some traffic of them attacking us, can you tell us what tool
they were using and its version?

NOTE: Wrap your answer in the <code>DUCTF{}</code>, e.g. <code>DUCTF{nmap_7.25}</code>

## Attachments

capture.pcap

## Solution

I opened the pcap file in Wireshark, then went to Analyze->Follow->TCP Stream. The first block
of text there, which you can view here, revealed the tool the attackers used: Nikto 2.1.6. This
was the flag.

flag: DUCTF{Nikto_2.1.6}
