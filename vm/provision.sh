# Provisioning script for a Vagrant VM running iPythonNotebook

# Obtain curl and install setuptools and pip
apt-get update
apt-get -y install python-setuptools
easy_install pip

# Get ipython and dependencies
echo
echo Installing iPython and dependencies...
echo
pip install scipy
pip install -U requests==1.0.4
pip install orcid-python
apt-get -y install python-matplotlib
apt-get -y install ipython-notebook -t precise-backports
export PYTHONPATH=/vagrant/user/scripts

# Uncomment the line that starts "# iptest" to run the ipython test suite
# One test is known to fail when run from root, the following command
# skips that single test. For some reason this doesn't work when installing
# iPython via apt-get
#
# iptest -q -e test_not_writable_ipdir

# Runup the notebook starting in the synced directory
cd /vagrant/user/notebooks
echo
echo Starting the iPython Notebook
echo
# Notebook process needs to daemonized. Code here is borrowed from
# https://github.com/mitchellh/vagrant/issues/1553#issuecomment-16235753
nohup ipython notebook --ip=192.168.33.10 -pylab inline 0<&- &>/dev/null &
echo
echo If no were errors reported your iPython notebook should be available at
echo http://192.168.33.10:8888 from your local browser
echo
echo Returning control to your local terminal. To reach the virtual machine
echo issue the command "vagrant ssh" from your command prompt.
echo