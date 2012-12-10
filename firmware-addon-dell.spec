Summary:	A firmware-tools plugin to handle BIOS/Firmware for Dell systems
Name:		firmware-addon-dell
Version:	2.2.9
Release:	%mkrel 1
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		http://linux.dell.com/libsmbios/download/ 
Source0:	http://linux.dell.com/libsmbios/download/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
# Dell only sells Intel-compat systems, so this package doesnt make much sense
# on, eg. PPC.  Also, we rely on libsmbios, which is only avail on Intel-compat
ExclusiveArch:	x86_64 ia64 %{ix86}
BuildRequires:	python-devel
# I know rpmlint complains about this (An ERROR, in fact), but it is a
# false positive. Auto deps cannot find this one because I actually am running
# binaries, not linking agains libs, as indicated by the fact that I require 
# the -bin package
Requires:	libsmbios-bin 
Requires:	firmware-tools >= 0:1.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The firmware-addon-dell package provides plugins to firmware-tools which enable
BIOS updates for Dell system, plus pulls in standard inventory modules
applicable to most Dell systems.


%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/firmware/dell/bios
%makeinstall_std
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING-GPL COPYING-OSL README TODO AUTHORS
%{python_sitelib}/*
%config(noreplace) %{_sysconfdir}/firmware/firmware.d/*.conf
%{_datadir}/firmware/dell
%{_datadir}/firmware-tools/*


%changelog
* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 2.2.9-1mdv2011.0
+ Revision: 594665
- new version 2.2.9
- rebuild for python 2.7

* Wed Jan 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 486958
- new version

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.1.0-2mdv2010.0
+ Revision: 437546
- rebuild

* Tue Feb 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.0-1mdv2009.1
+ Revision: 339269
- update to new version 2.1.0
- new license policy
- spec file clean

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.4.8-4mdv2009.1
+ Revision: 325206
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4.8-3mdv2009.0
+ Revision: 245192
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4.8-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.8-1mdv2008.0
+ Revision: 79556
- import firmware-addon-dell


* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.8-1mdv2008.0
- contributed by Olivier Lahaye <olivier.lahaye at free.fr>
