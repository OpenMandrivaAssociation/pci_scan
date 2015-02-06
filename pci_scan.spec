%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	PCI scanning tool for X Terminals and embedded systems
Name:		pci_scan
Version:	0.02
Release:	6
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
URL:		http://www.ltsp.org
BuildRequires:	dietlibc-devel
Requires:	ltsp-hwlists >= 0.02
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program will read in a device database of PCI Vendor/Device Ids. It will
then check the /proc/bus/pci/devices file, to see if any devices in the system
are found in the list that was read in.

The device database file will contain records that look like this:

    1234:5678  somedriver

The device database file will be read into a linked list in memory. The program
will then read each entry in the /proc/bus/pci/devices file.  For each entry,
it will search the linked list to see if it finds a match. As soon as a match
is found, the drivername will be printed to stdout, and the program will exit.

This is very useful, to determine what kind of network card or video card is
installed in the system, and which driver module should be loaded.

%prep

%setup -n %{name}-%{version}

%build
diet gcc -Os -o %{name} %{name}.c

%install
rm -rf %{buildroot}

install -d %{buildroot}/sbin
install -m0755 %{name} %{buildroot}/sbin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%attr(0755,root,root) /sbin/%{name}


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.02-5mdv2010.0
+ Revision: 430247
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-4mdv2009.0
+ Revision: 268359
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 0.02-3mdv2009.0
+ Revision: 217544
- rebuilt against dietlibc-devel-0.32

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-2mdv2008.1
+ Revision: 136648
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02-2mdv2007.0
+ Revision: 133037
- use dietlibc instead

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2007.1
+ Revision: 117144
- Import pci_scan

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdk
- initial Mandriva package (mille-xterm import)

