OpennessReporting
=================

IPython Notebook approaches to reporting on the openness of people, institutions, and funder outputs.

This repository is a set of tools embedded in a functioning set of IPython Notebooks intended to be 
run locally under a Vagrant virtual machine setup. If that doesn't make sense don't worry too much
as the intention is that it should also be easy to setup locally, even for someone with no experience
of setting up VMs or running a server.

Setting Up
----------

To set this up on you local machine you will need to download two packages, both of which I found
very easy to install. The first is [VirtualBox][https://www.virtualbox.org/wiki/Downloads] which
is what will actually run your VM. Simply download the package and follow the instructions as is
usual. The second package you require is [Vagrant][http://downloads.vagrantup.com/] which again is very
straightforward to download and setup in my experience. 

Once you have the two packages you can clone, fork, or simply download this repository to your 
machine. With the repository on your local machine, open a terminal window, navigate to the 
top directory of the repository (the one with the VagrantFile in it) and issue the command:

    $ vagrant up

You should see things grinding away for a bit as the VM is set up and finally if all goes well
you should get the message:

    $ Starting the iPython Notebook


    $ If no were errors reported your iPython notebook should be available at
    $ http://192.168.33.10:8888 from your local browser

    $ Returning control to your local terminal. To reach the virtual machine
    $ issue the command vagrant ssh from your command prompt.

Running your own report
-----------------------

Navigate to [http://192.168.33.10:8888] on your browser and you should see the IPython Notebook
front page with one notebook already there. The simplest way to run your own report is to go
to that notebook and change the ORCID. Then click the "play" button, just below the Kernel 
menu. If the numbers look a little low you may need to run it a few times. The Open Article
Gauge will take a while to go out and check licenses but will return the ones for which it has
an answer.
