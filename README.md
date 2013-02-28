Tunneler
========

Python tool to setup multiple SSH tunnels running on local ports.

The usage is very simple once the source is downloaded and it only consists
of a single script ``run_ssh_tunnels``::

    ./run_ssh_tunnels [-v+] [-q+] [-s] [list of tunnel aliases..]

The tunnel aliases are defined in the keys of ``TUNNEL_DATA`` in
``settings.py.example``.  This file should be copied to ``settings.py`` where
you may enter your custom connection data.