=========
nfcreader
=========


.. image:: https://img.shields.io/pypi/v/nfcreader.svg
        :target: https://pypi.python.org/pypi/nfcreader

.. image:: https://img.shields.io/travis/EDWIAN004@myuct.ac.za/nfcreader.svg
        :target: https://travis-ci.com/EDWIAN004@myuct.ac.za/nfcreader

.. image:: https://readthedocs.org/projects/nfcreader/badge/?version=latest
        :target: https://nfcreader.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python API for CR95HF NFC reader to run on the Pi Zero. Used as a python wrapper for the existing C API provided for the CR95HF module by STMicroelectronics. However, it was found to be lacking for Linux users, as well as difficult to compile and run compared to a Python API. 


* Free software: MIT license
* Documentation: https://nfcreader.readthedocs.io.

Abstract
--------
Use case scenario for demonstrator application: Student access to venues.
The aim was to provide better support for the CR95HF's use for the Raspberry Pi in Python3, via an API.
A demonstrator application was created for showing the uses of the API for an access control use case: https://github.com/IanEdwards99/CR95HF_Demo_App

Features
--------
- USB Connect
- Protocol Select
- Send Receive
- ResetSPI
- Field Off
- Send IRQ Pulse
- Send NSS Pulse
- STCmd Command
- Initiate
- ResetToReady
- MCUrev
- Echo
- Idn (Get ID number of CR95HF module)
- GetPinInterfaceState
- Reading from NFC tag
- Writing to NFC tag
- IDLE for tag
- Scan and Write
- Tag detection and hunting
- Clearing NFC tag
- Read entire contents of all registers from tag
- Extract payload
- Prepare for writing and reading with dec/hex/string conversion functions.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
