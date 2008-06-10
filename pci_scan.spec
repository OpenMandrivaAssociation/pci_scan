%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	PCI scanning tool for X Terminals and embedded systems
Name:		pci_scan
Version:	0.02
Release:	%mkrel 3
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
