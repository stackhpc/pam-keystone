Name:		pam-keystone
Version:	0.0.3
Release:	1%{?dist}
Summary:	PAM module for authenticating against OpenStack Keystone

Group:		System Environment/Libraries
License:	Public Domain
URL:		https://github.com/stackhpc/pam-keystone
Source0:	pam-keystone-0.0.3.tar.gz

Requires:	python
Requires:	pam-python
Requires:	PyYAML
Requires:       python-memcached

%description
This module allows authenticating against keystone as a
pam module. E.g. to allow nginx or other system
services to use keystone users.

It does not create an NSS module, so it's for auth only.

%prep
%setup -q

%build

%install
install -D keystone-auth.py $RPM_BUILD_ROOT/usr/lib64/security/keystone-auth.py

%files
%attr(0755,root,root)
/usr/lib64/security/keystone-auth.py
/usr/lib64/security/keystone-auth.pyc
/usr/lib64/security/keystone-auth.pyo

%changelog
* Sun Feb 11 2018 Stig Telfer <stig@stackhpc.com>
- Updated for Keystone v3 domain support

* Tue May 16 2017 Stig Telfer <stig@stackhpc.com>
- pam-keystone-0.0.2
- Adapted PoC implementation for bare metal OpenStack deployment

* Mon May 15 2017 Don Bowman
- pam-python-0.0.1
- Original repo at: https://github.com/donbowman/pam-keystone
