%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A firmware-tools plugin to handle BIOS/Firmware for Dell systems
Name:		firmware-addon-dell
Version:	2.2.9
Release:	3
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		https://linux.dell.com/libsmbios/download/ 
Source0:	http://linux.dell.com/libsmbios/download/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
# I know rpmlint complains about this (An ERROR, in fact), but it is a
# false positive. Auto deps cannot find this one because I actually am running
# binaries, not linking agains libs, as indicated by the fact that I require
# the -bin package
Requires:	libsmbios-bin
Requires:	firmware-tools
# Dell only sells Intel-compat systems, so this package doesnt make much sense
# on, eg. PPC. Also, we rely on libsmbios, which is only avail on Intel-compat
ExclusiveArch:	x86_64 %{ix86}

%description
The firmware-addon-dell package provides plugins to firmware-tools which enable
BIOS updates for Dell system, plus pulls in standard inventory modules
applicable to most Dell systems.

%files
%doc COPYING-GPL COPYING-OSL README TODO AUTHORS
%{python_sitelib}/*
%config(noreplace) %{_sysconfdir}/firmware/firmware.d/*.conf
%{_datadir}/firmware/dell
%{_datadir}/firmware-tools/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}/%{_datadir}/firmware/dell/bios
%makeinstall_std

