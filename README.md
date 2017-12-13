Python - Python Work Directory
========

Python is being used for working with Labjack feature testing, and Graphic User
Interface(GUI) testing.

Labjack is used with Honeywell sensor RTP050LVNAA.  The codes who are associated, are 
intended to be work with Labjack only.

Tkinter module is used for testing construction of GUI based on JKL project.
Tkinter was abandoned due to Java's jFrame GUI capabilities are better than Tkinter.

Features
--------

- LabJack_Potentiometer
- PKL
- Test1
- TkinterConstruction1

Details will be added after Installation for more information based.

Installation
------------

I used PyCharm as IDE for Python and the list of modules will be added below for pip install.

- Modules
- > LabJackPython = https://github.com/labjack/LabJackPython
- > openpyxl = Ability to read/write Excel 2010 xlsx/ xlsm files
- > Pandas = Data Analysis library
- > pygubu including designer = Python Gui designer
- > pyzbar = Python wrapper around zbar barcode reader
- > Tkinter = Python's de-facto standard GUI package
- > xlwings = Python library that makes it easy to call Python from Excel and vice versa

Contents
--------

> LabJack_Potentiometer

This was intended to be created to test connection between the LabJack and the Honeywell sensor RTP050LVNAA.
Now, this code is being used as base for 

> PKL
-- Comes with PKL_Main, test_LabJack, test_features

Code name: PKL - Python Koolness Lab

This is for Honeywell project created by Lee Kaiser.  PKL_Main is created with base of LabJack_Potentiometer
and modified data result to accurate result.  The problem is that Honeywell sensor can only see
only 50 degrees out in the front, not 360 degree circle for nice versa.  I attempted to program
Honeywell sensor result data to count rotation and fool-proof rotation to avoid addup counts.
It is partially working but still need to work more to iron the code out.

> Test1

This is for JKL project and I attempted to create barcode reader using python for easiness. 
Turns out using Java and it's own GUI program have better ability to make it happen. 
This is abandoned project and I have no intended to go back work on it.


> TkinterConstruction1

I was attempting to test Python GUI capabilities to see if it is better than jFrame GUI.
This is abandoned and it is example of Tkinter from external sources.


License
-------

The project is licensed under the BSD license.
