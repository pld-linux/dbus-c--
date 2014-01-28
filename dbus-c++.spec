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
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib

%package glib-devel
Group:		Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}

%description glib

%package glib-static
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib

%package ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ecore

%package ecore-devel
Group:		Development/Libraries
Requires:	%{name}-ecore = %{version}-%{release}

%description ecore-devel

%package ecore-static
Group:		Development/Libraries
Requires:	%{name}-ecore-devel = %{version}-%{release}

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
%attr(755,root,root) %{_libdir}/libdbus-c++-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc TODO
%{_includedir}/*
%attr(755,root,root) %{_libdir}/libdbus-c++-1.so
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-1.a

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-glib-1.so.*.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-glib-1.so

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-glib-1.a

%files ecore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-ecore-1.so.*.*.*

%files ecore-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-ecore-1.so

%files ecore-static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-ecore-1.a
