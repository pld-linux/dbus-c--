#
# Conditional build:
%bcond_without	ecore	# Ecore mainloop integration
#
Summary:	Native C++ bindings for D-Bus
Summary(pl.UTF-8):	Natywne wiązania C++ do usługi D-Bus
Name:		dbus-c++
Version:	0.9.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/dbus-cplusplus/lib%{name}-%{version}.tar.gz
# Source0-md5:	e752116f523fa88ef041e63d3dee4de2
Patch1:		%{name}-gcc4.7.patch
Patch2:		%{name}-linkfix.patch
URL:		http://sourceforge.net/projects/dbus-cplusplus/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	doxygen
%{?with_ecore:BuildRequires:	ecore-devel}
BuildRequires:	expat-devel >= 1.95
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	dbus-libs >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbus-c++ attempts to provide a C++ API for D-Bus. The library has a
GLib/GTK+ and an Ecore mainloop integration.

%description -l pl.UTF-8
dbus-c++ to próba dostarczenia API C++ do usługi D-Bus. Biblioteka
zapewnia integrację z pętlami głównymi GLib/GTK+ oraz Ecore.

%package devel
Summary:	Development files for dbus-c++
Summary(pl.UTF-8):	Pliki programistyczne biblioteki dbus-c++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 1.0.0
Requires:	libstdc++-devel

%description devel
This package contains the header files for developing applications
that use dbus-c++.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę dbus-c++.

%package static
Summary:	Static dbus-c++ library
Summary(pl.UTF-8):	Statyczna biblioteka dbus-c++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static dbus-c++ library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę dbus-c++.

%package glib
Summary:	Native C++ bindings for D-Bus (GLib Mainloop)
Summary(pl.UTF-8):	Natywne wiązania C++ do usługi D-Bus (pętla główna GLiba)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib
Native C++ bindings for D-Bus (GLib Mainloop).

%description glib -l pl.UTF-8
Natywne wiązania C++ do usługi D-Bus (pętla główna GLiba).

%package glib-devel
Summary:	Development files for dbus-c++-glib
Summary(pl.UTF-8):	Pliki programistyczne biblioteki dbus-c++-glib
Group:		Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description glib-devel
Development files for dbus-c++-glib.

%description glib-devel -l pl.UTF-8
Pliki programistyczne biblioteki dbus-c++-glib.

%package glib-static
Summary:	Static dbus-c++-glib library
Summary(pl.UTF-8):	Statyczna biblioteka dbus-c++-glib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static dbus-c++-glib library.

%description glib-static -l pl.UTF-8
Statyczna biblioteka dbus-c++-glib.

%package ecore
Summary:	Native C++ bindings for D-Bus (Ecore Mainloop)
Summary(pl.UTF-8):	Natywne wiązania C++ do usługi D-Bus (pętla główna Ecore)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ecore
Native C++ bindings for D-Bus (Ecore Mainloop).

%description ecore -l pl.UTF-8
Natywne wiązania C++ do usługi D-Bus (pętla główna Ecore).

%package ecore-devel
Summary:	Development files for dbus-c++-ecore
Summary(pl.UTF-8):	Pliki programistyczne biblioteki dbus-c++-ecore
Group:		Development/Libraries
Requires:	%{name}-ecore = %{version}-%{release}
Requires:	ecore-devel

%description ecore-devel
Development files for dbus-c++-ecore.

%description ecore-devel -l pl.UTF-8
Pliki programistyczne biblioteki dbus-c++-ecore.

%package ecore-static
Summary:	Static dbus-c++-ecore library
Summary(pl.UTF-8):	Statyczna biblioteka dbus-c++-ecore
Group:		Development/Libraries
Requires:	%{name}-ecore-devel = %{version}-%{release}

%description ecore-static
Static dbus-c++-ecore library.

%description ecore-static -l pl.UTF-8
Statyczna biblioteka dbus-c++-ecore.

%prep
%setup -q -n lib%{name}-%{version}
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_ecore:--disable-ecore}

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
%{?with_ecore:%exclude %{_includedir}/dbus-c++-1/dbus-c++/ecore-integration.h}
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

%if %{with ecore}
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
%endif
