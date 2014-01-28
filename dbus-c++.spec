Summary:	Native C++ bindings for D-Bus
Name:		dbus-c++
Version:	0.9.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/dbus-cplusplus/lib%{name}-%{version}.tar.gz
# Source0-md5:	e752116f523fa88ef041e63d3dee4de2
URL:		http://sourceforge.net/projects/dbus-cplusplus/
Patch1:		%{name}-gcc4.7.patch
Patch2:		%{name}-linkfix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	ecore-devel
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	gtkmm-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbus-c++ attempts to provide a C++ API for D-Bus. The library has a
glib/gtk and an Ecore mainloop integration.

%package devel
Summary:	Development files for dbus-c++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package static
Summary:	Static dbus-c++ library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static dbus-c++ library.

%package glib
Summary:	Native C++ bindings for D-Bus (Glib Mainloop)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib
Native C++ bindings for D-Bus (Glib Mainloop).

%package glib-devel
Summary:	Development files for dbus-c++-glib
Group:		Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}

%description glib-devel
Development files for dbus-c++-glib.

%package glib-static
Summary:	Static dbus-c++-glib library
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static dbus-c++-glib library.

%package ecore
Summary:	Native C++ bindings for D-Bus (Ecore Mainloop)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ecore
Native C++ bindings for D-Bus (Ecore Mainloop).

%package ecore-devel
Summary:	Development files for dbus-c++-ecore
Group:		Development/Libraries
Requires:	%{name}-ecore = %{version}-%{release}

%description ecore-devel
Development files for dbus-c++-ecore.

%package ecore-static
Summary:	Static dbus-c++-ecore library
Group:		Development/Libraries
Requires:	%{name}-ecore-devel = %{version}-%{release}

%description ecore-static
Static dbus-c++-ecore library.

%prep
%setup -q -n lib%{name}-%{version}
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig
%post	ecore -p /sbin/ldconfig
%postun	ecore -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/dbusxx-introspect
%attr(755,root,root) %{_bindir}/dbusxx-xml2cpp
%attr(755,root,root) %{_libdir}/libdbus-c++-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbus-c++-1.so.0

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/dbus-c++-1
%dir %{_includedir}/dbus-c++-1/dbus-c++
%{_includedir}/dbus-c++-1/dbus-c++/*.h
%exclude %{_includedir}/dbus-c++-1/dbus-c++/ecore-integration.h
%exclude %{_includedir}/dbus-c++-1/dbus-c++/glib-integration.h
%attr(755,root,root) %{_libdir}/libdbus-c++-1.so
%{_pkgconfigdir}/dbus-c++-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-1.a

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-glib-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbus-c++-glib-1.so.0

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-glib-1.so
%{_includedir}/dbus-c++-1/dbus-c++/glib-integration.h
%{_pkgconfigdir}/dbus-c++-glib-1.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-glib-1.a

%files ecore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-ecore-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbus-c++-ecore-1.so.0

%files ecore-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-c++-ecore-1.so
%{_includedir}/dbus-c++-1/dbus-c++/ecore-integration.h
%{_pkgconfigdir}/dbus-c++-ecore-1.pc

%files ecore-static
%defattr(644,root,root,755)
%{_libdir}/libdbus-c++-ecore-1.a
