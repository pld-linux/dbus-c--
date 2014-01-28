Summary:	Native C++ bindings for D-Bus
Name:		dbus-c++
Version:	0.9.0
Release:	0.1
License:	LGPL v2+
Group:		Libraries
URL:		http://sourceforge.net/projects/dbus-cplusplus/
Source0:	http://downloads.sourceforge.net/dbus-cplusplus/lib%{name}-%{version}.tar.gz
Patch1:		%{name}-gcc4.7.patch
Patch2:		%{name}-linkfix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	dbus-devel
BuildRequires:	ecore-devel
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	gtkmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbus-c++ attempts to provide a C++ API for D-Bus. The library has a
glib/gtk and an Ecore mainloop integration.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%package        static
Summary:	Static dbus-c++ library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static dbus-c++ library.

%package glib
%description glib

%package glib-devel
%description glib

%package glib-static
%description glib

%package ecore
%description ecore

%package ecore-devel
%description ecore-devel

%package ecore-static
%description ecore-static

%prep
%setup -q -n lib%{name}-%{version}
%{__sed} -i 's/\r//' AUTHORS
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-tests

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING AUTHORS
%attr(755,root,root) %{_bindir}/dbusxx-introspect
%attr(755,root,root) %{_bindir}/dbusxx-xml2cpp
%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-1.a
