# Demo NNM 

2/16/2022 - v1.0 <br/>
2/17/2022 - v1.1 <br/>
3/16/2022 - v2.0 <br/>
3/25/2022 - v2.1 <br/>


Please note that as this is a network sniffer, you will either need to attach a second interface with mirrored traffic or run the container in privileged mode to listen to the physical interface. 

# Repository

The github repository for the build files is located [here](https://github.com/underwateroverlander/Docker-NNM).

# Before We Begin

Please ensure that the directory is moved out of Downloads and placed somewhere more appropriate such as Documents. Before beginning installation, go ahead and retrieve a standalone NNM Activation Code from your Tenable Community portal unless you intend to manage it through a Tenable.sc instance. The hostname will be nnm.local, but feel free to change it. Later iterations will include a script to automatically add it to Tenable.sc using the pyTenable suite.

# Usage

You should have python3 installed, and can check this by opening terminal and typing "python3 --version". Most of the calls in the python script are python 3.5+, so please ensure you are on at least that version. You can install python3 through homebrew, the Python website, git, or other mechanisms. Google is your friend :).

    cd <folder where saved>
    python3 nnm.py

You will be prompted to press enter and input an activation code. The full installation should be completed within 3 minutes of launch, and you can access the container once it's up using command "docker exec -it nnm-local /bin/bash" from within your terminal to drop in as root. 

The GUI can be accessed at https://localhost:8835 from your browser. 
admin:password

# Deviations

This NNM is configured with complex password requirements turned off, password set to password, a monitored range of 0.0.0.0, and monitor mode enabled. Please update to reflect your needs. Stay tuned for more!

# Future Builds

The next iterations will include better fault handling, bug fixes, and an automated mechanism to connect to Tenable.sc. Feel free to contribute!
