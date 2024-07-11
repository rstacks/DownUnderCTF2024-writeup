# zoo feedback form

## Description

The zoo wants your feedback! Simply fill in the form, and send away, we'll handle it from there!

https://web-zoo-feedback-form-2af9cc09a15e.2024.ductf.dev 

## Attachments

[zoo-feedback-form.zip](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/web/zoo_feedback_form/attachments/zoo-feedback-form.zip)

## Solution

- The provided website has a text entry field. Once the user clicks the "Submit Feedback" button, the website displays the user's text back at them.
- I wanted to see what was happening behind the scenes during this process, so I used [Burp Suite](https://portswigger.net/burp/communitydownload) to intercept the web request after I pressed the "Submit Feedback" button.
- The subsequent POST request contained XML data that included the text I wrote in the text entry field. Since all of the XML data was shown in the POST request, this website was vulnerable to an **XXE injection**. You can learn more about this attack [here](https://portswigger.net/web-security/xxe).
- The attachment for this challenge reveals that the flag is most likely located at <code>/app/flag.txt</code>. I modified the XML in the POST request to fetch the contents of this file and display that as my feedback. The complete payload that I used can be viewed [here](https://github.com/rstacks/DownUnderCTF2024-writeup/blob/master/web/zoo_feedback_form/payload.xml).
- Forwarding the modified POST request resulted in the website displaying the flag.

## Flag

DUCTF{emU_say$_he!!0_h0!@_ci@0}
