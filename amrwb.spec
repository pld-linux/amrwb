#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	3GPP AMR-WB Floating-point Speech Codec
Summary(pl.UTF-8):	Zmiennoprzecinkowy kodek mowy 3GPP AMR-WB
Name:		amrwb
Version:	11.0.0.0
Release:	1
# from 26204-b00.doc:
# Copyright Notification
# No part may be reproduced except as authorized by written permission.
# The copyright and the foregoing restriction extend to reproduction in all media.
# (c) 2012, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TTA, TTC).
# All rights reserved.
License:	restricted
Group:		Libraries
Source0:	http://ftp.penguin.cz/pub/users/utx/amr/%{name}-%{version}.tar.bz2
# Source0-md5:	f9ea63e6f8b778fe1040f73891ba3720
Source1:	http://www.3gpp.org/ftp/Specs/archive/26_series/26.204/26204-b00.zip
# NoSource1-md5:	9fd5a681beb11277ce370deafa4a494d
NoSource:	1
URL:		http://www.3gpp.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
3GPP AMR-WB Floating-point Speech Codec.

%description -l pl.UTF-8
Zmiennoprzecinkowy kodek mowy 3GPP AMR-WB.

%package devel
Summary:	Header files for amrwb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki amrwb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for amrwb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki amrwb.

%package static
Summary:	Static amrwb library
Summary(pl.UTF-8):	Statyczna biblioteka amrwb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static amrwb library.

%description static -l pl.UTF-8
Statyczna biblioteka amrwb.

%prep
%setup -q

ln -s %{SOURCE1} .

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 26204-b00.doc readme.txt
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/amrwb-*
%attr(755,root,root) %{_libdir}/libamrwb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libamrwb.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamrwb.so
%{_libdir}/libamrwb.la
%{_includedir}/amrwb

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libamrwb.a
%endif
