This project is still in developement phase and it might be unstable. Therefore, any bug reports and suggestions are welcomed.

Gitraffe
========

Gitraffe is a git GUI based on Python and QT for UNIX-like systems (BSD / Linux / Mac OS X). Sounds unoriginal? Well, we are dissatisfied with existing GUIs - in most of them we see things that we don't like and maybe we will provide better solutions, hope so. ;)

How to run Gitraffe?
====================

1. Ensure that you have Python 3.2, PyQT4 for Py 3.2 and Python Setuptools. If you're not sure, see the next section.
2. Go to gitraffe/libraries/ directory and do:

**Ubuntu**
<pre>sudo easy_install3 setproctitle
sudo easy_install3 pexpect_u-2.5.1-py3.2.egg</pre>

**Gentoo / Sabayon**
as root:
<pre>easy_install-python3.2
easy_install-python3.2 pexpect_u-2.5.1-py3.2.egg</pre>

**Mac OS X**
<pre>sudo easy_install-3.2 setproctitle
sudo easy_install-3.2 pexpect_u-2.5.1-py3.2.egg</pre>

3. Just run gitraffe/main.py :)

Which packages do you need?
===========================

**Gentoo / Sabayon**

If you have USE_PYTHON and PYTHON_TARGETS variables defined in your /etc/make.conf file, you should include 3.2 version to get all packages and Python libraries working.
- >=dev-lang/python-3.2.3
- dev-python/PyQt4
- dev-python/setuptools

**Ubuntu / Debian**
- python3
- python3-pyqt4
- python3-setuptools

**Mac OS X (MacPorts)**
- python32
- py32-pyqt4

Screenshots
===========

![](https://raw.github.com/v4d0r/gitraffe/master/screenshots/1.png)

![](https://raw.github.com/v4d0r/gitraffe/master/screenshots/2.png)