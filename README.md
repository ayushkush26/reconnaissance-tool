# reconnaissance-tool

This Python script performs reconnaissance on a given domain by gathering WHOIS information, DNS records, subdomains, and web technologies used by the website.

## **Features**

- Fetches WHOIS information for the specified domain.
- Retrieves DNS records including A, MX, NS, and TXT.
- Discovers subdomains using Sublist3r.
- Identifies web technologies using WhatWeb.

Make sure you have Python 3 installed on your machine.Then run the this code in terminal
**pip3 install -r requirements.txt**

Additionally, the following external tools must be installed and accessible from the command line:

- [Sublist3r](https://github.com/aboul3la/Sublist3r)
- [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
- The subdomains.txt file empty initially.I have tested the tool on practicepaper.in website.

## Installation

1. Clone the repository: **git clone https://github.com/ayushkush26/reconnaissance-tool.git**
2. cd reconnaissance-tool
3. python recon_tool.py


## License and discalimer

This tool are for educational purposes only, ALL developers and contributors are not responsible for any kind of misuse. This Project is licensed under GNU General Public License v3.0.
