**NOTE: In process of moving over to GitLab, the project was updated here to replace current version. But will be maintained on following link: 
https://gitlab.com/stick-fish/nosey_neighbour 
If you like this and want to see future updates, please join me on above link.**

<h1>Nosey Neighbour</h1>
_Everyone has 1_

<h2>Automated Basic Enumeration script for CTF's and others.</h2>

**Assumes Kali / ParrotOS distro which includes: `Dirb`, `Nikto`, `Nmap`, `Enum4linux`... But not essential and either of these can be installed manually.**

<p>
The update was a chance to refresh and re-learn some Python 3 concepts I had forgotten, I have tried to stick to OOP as far as possible. 
  I have cheated a little in some spots and used the `global` keyword, but with each revision I hope to make even the grumpiest of devs proud.
</p>

 
 **********************************************************************************************************


<h4>Installation is easy:</h4>

- Some scripts are needed in order to allow full functionality, example the python-nmap needs to be installed 
- To install the needed packages:
  - `pip install python-nmap`


Alternatively copy and paste the following to do it all automatically ( May be prompted for a `sudo` password to install `pip` if not already installed ) :

`cd /opt; sudo apt update; sudo apt install python3-pip; pip install python-nmap; git clone https://gitlab.com/stick-fish/nosey_neighbour.git ; cd /opt/nosey_neighbour; chmod 755 nosey.py`


 **********************************************************************************************************


<h4>Basic Usage:</h4>

`./nosey.py 10.10.10.1`
`python3 nosey.py 10.10.10.1`


 **********************************************************************************************************


**Screen shot example:**

![Running in terminal](https://gitlab.com/stick-fish/nosey_neighbour/-/blob/master/NN_screenshot.png)


 **********************************************************************************************************


<h3>Changelog:</h3>

<h4>V2.0</h4>

- Changed everything to Py3 format ( Current version at time of update 3.8.6 )
- Created a seperate files to try make the complete package seem more logical and using classes & methods to avoid repetitiveness like in previous versions
- Created template method (so far only web section) to reduce code reuse
- Added python-nmap 0.6.4 to handle the nmap scanning
- Changed colors slightly and tried to improve the outputs on terminal 
- Added more comments to try help anyone editing to understand my idea
- So far only TCP 53, 80, 443 have some basic checks in place (Next small update will have additonal ports / checks added)
- Switched to gobuster from dirb, to get a better scan output on screen
- Removed `Enum4linux` from previous version, looking at alternatives to enumerate SMB services
- Added auto download for a basic seclists wordlist, it has also been added to repo


<h4>V1.1</h4>

- Added in Enum4linux
- Color to headings

<h4>V1.0</h4>

- Segregated nikto and dirb scans into their own files, making the main script less clutterd.
- Added a little ASCII art because who doesnt like art.
  - ASCII ART: `http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20`

 
 **********************************************************************************************************


** TODO:**

- [ ] Include additional scanning
- [ ] Alternative to current color commands (Reduce repeat commands)
- [ ] Incorporate pass the hash
- [ ] Include the option to change Nmap flags 
- [ ] Work on menu system to set more options
- [X] Change to full class to remove if...else for every port
- [ ] Add progress bars due to minimal output on terminal during scans
