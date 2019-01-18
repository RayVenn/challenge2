# How to run this app

**This is for python3, so make sure you are using python3** 
### 1. Use Python PEX file
  * Checkout this repo:
  
    `git clone https://github.com/RayVenn/challenge2.git`
  * Go into project, `cd challenge2`
  * For linux OS,
  
    `./find-pair-linux test.txt 1200` (you have your own input txt file and any balance)
  * For Mac OS,
  
    `./find-pair-osx test.txt 1200` (you have your own input txt file and any balance)

### 2. Pip install
  * You need to install pip and virtualenv first
  * create a new virtualenv:
  
    `virtualenv test`
  * activate this virtualenv:
  
    `source test/bin/activate`
  * pip install the service from github:
  
    `pip install git+https://github.com/RayVenn/challenge2.git`
  * Make sure you have input text file, get my example file:
  
    `wget https://raw.githubusercontent.com/RayVenn/challenge2/master/test.txt`
  * run challenge1 module:
  
    `find-pair test.txt 1200`
  
