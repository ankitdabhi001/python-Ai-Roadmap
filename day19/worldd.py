
import re
text = "Contact me at support@gmail.com or help@yahoo.com"

emails = re.findall(r'(\w+)@(gmail|yahoo)\.com', text)

print(emails)
