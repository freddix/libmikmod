Summary:	Module player and library supporting many formats
Name:		libmikmod
Version:	3.3.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/mikmod/%{name}-%{version}.tar.gz
# Source0-md5:	bc6bea190cb8d2ce2b105cc0ff811681
URL:		http://www.freedesktop.org/wiki/Software/libevdev/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Handler library for evdev events.

%package devel
Summary:	Header files for libmikmod library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmikmod library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libmikmod.so.3
%attr(755,root,root) %{_libdir}/libmikmod.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmikmod.so
%attr(755,root,root) %{_bindir}/libmikmod-config
%{_datadir}/aclocal/libmikmod.m4
%{_includedir}/mikmod.h
%{_pkgconfigdir}/libmikmod.pc
%{_mandir}/man1/libmikmod-config.1*

