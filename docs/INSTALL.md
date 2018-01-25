**Table of Contents**

1. [Requirements](#requirements)
2. [Install Dependencies](#install-dependencies)
   * [Ubuntu 14.04 / Debian 8](#ubuntu-1404--debian-8)
   * [Ubuntu 16.04 / Debian 9](#ubuntu-1604--debian-9)
   * [CentOS 7 / RHEL 7](#centos-7--rhel-7)
   * [openSUSE Leap 42.2](#opensuse-leap-422--423)
3. [Installation](#installation)
   * [Native packages](#native-packages)
   * [With pip](#with-pip)
     * [From PyPi](#from-pypi)
     * [From the repository](#from-the-repository)
4. [Afterwards](#afterwards)


Please report any errors you encounter at https://github.com/certtools/intelmq/issues

For upgrade instructions, see [UPGRADING.md](UPGRADING.md).

# Requirements

The following instructions assume the following requirements:

Supported and recommended operating systems are:
* CentOS 7
* Debian 8 and 9
* OpenSUSE Leap 42.2 and 42.3
* Ubuntu: 14.04 and 16.04 LTS

Other distributions which are (most probably) supported include RHEL, Fedora and openSUSE Tumbleweed.

# Install Dependencies

If you are using native packages, you can simply skip this section as all dependencies are installed automatically.

## Ubuntu 14.04 / Debian 8

```bash
apt-get install python3 python3-pip
apt-get install git build-essential libffi-dev
apt-get install python3-dev
apt-get install redis-server
```

**Special note for Debian 8**: 
if you are using Debian 8, you need to install this package extra: ``apt-get install libgnutls28-dev``.
In addition, Debian 8 has an old version of pip3. Please get a current one via:
```bash
curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"
python3.4 /tmp/get-pip.py
```

## Ubuntu 16.04 / Debian 9

```bash
apt install python3-pip python3-dnspython python3-psutil python3-redis python3-requests python3-termstyle python3-tz
apt install git redis-server
```

For Debian 9 additionally install `python3-dateutil` (it's not available in Ubuntu 16.04).

Optional dependencies:
```bash
apt install bash-completion jq cron
apt install python3-sleekxmpp python3-pymongo python3-psycopg2
```

## CentOS 7 / RHEL 7

```bash
yum install epel-release
yum install python34 python34-devel
yum install git gcc gcc-c++
yum install redis
```

Install the last pip version:
```bash
curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"
python3.4 /tmp/get-pip.py
```

## openSUSE Leap 42.2 / 42.3

```bash
zypper install python3-dateutil python3-dnspython python3-psutil python3-pytz python3-redis python3-requests python3-python-termstyle
zypper install git redis
```

For 42.3 additionally install `python3-install` (it's not available in 42.2).

Optional dependencies:
```bash
zypper in bash-completion jq cron
zypper in python3-psycopg2 python3-pymongo python3-sleekxmpp
```

# Installation

There are different methods to install IntelMQ:

* as native deb/rpm package
* from PyPi: to get the latest releases as python package
* from the (local) repository: for developers to get the latest (unstable!) version and/or have local modifications

## Native packages

Get the install instructions for your operating system here:
https://software.opensuse.org/download.html?project=home%3Asebix%3Aintelmq&package=intelmq

Currently, these operating systems are supported by the packages:
* CentOS 7, install `epel-release` first
* RHEL 7, install `epel-release` first
* Debian 8 (install `python3-typing` too) and 9
* Fedora 25, 26 and Rawhide
* openSUSE Leap 42.2, 42.3 and Tumbleweed
* Ubuntu 16.04 and 17.04

Please report any errors or improvements at https://github.com/certtools/intelmq/issues Thanks!

## With pip

pip automatically installs the dependencies of the core-library if they are not installed yet. Some bots have additional dependencies which are mentioned in their documentation. They have also a `REQUIREMENTS` file (in their source directory) which you can use for `pip3 install -r /path/to/REQUIREMENTS`.

Please note that the pip3 installation method does not (and cannot) create /opt/intelmq, as described in [Issue #189](/certtools/intelmq/issues/819).
As workaround you need to move /opt/intelmq from the site-packages directory to / manually.
The location of this directory varies, it could be `/usr/lib/python3.4/site-packages`, `/usr/local/lib/python3.5/dist-packages/` or similar.
For example:
```bash
mv /usr/lib/python3.4/site-packages/opt/intelmq /opt/
```

### From PyPi

```bash
sudo -s

pip3 install intelmq

useradd -d /opt/intelmq -U -s /bin/bash intelmq
chmod -R 0770 /opt/intelmq
chown -R intelmq.intelmq /opt/intelmq
```

### From the repository

Clone the repository if not already done:
```bash
git clone https://github.com/certtools/intelmq.git /tmp/intelmq
cd /tmp/intelmq
```

If you have a local repository and you have or will do local modification, consider using an editable installation (`pip install -e .`).
```
sudo -s

pip3 install .

mkdir /opt/intelmq
useradd -d /opt/intelmq -U -s /bin/bash intelmq
chmod -R 0770 /opt/intelmq
chown -R intelmq.intelmq /opt/intelmq
```

# Afterwards

Now continue with the [User Guide](User-Guide.md).
