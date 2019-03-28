#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	Rendering library for Kate text streams using Pango and Cairo
Summary(pl.UTF-8):	Biblioteka renderująca strumienie tekstowe Kate przy użyciu Pango i Cairo
Name:		libtiger
Version:	0.3.4
Release:	13
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://code.google.com/p/libtiger/downloads/list
Source0:	http://libtiger.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	dc1dbeb658c95485ba10b9b2897b4ae2
Patch0:		libm.patch
URL:		http://code.google.com/p/libtiger/
BuildRequires:	doxygen
BuildRequires:	libkate-devel >= 0.2.0
BuildRequires:	pango-devel >= 1:1.16
BuildRequires:	pkgconfig
Requires:	libkate >= 0.2.0
Requires:	pango >= 1:1.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is libtiger, a rendering library for Kate streams using Pango and
Cairo.

%description -l pl.UTF-8
libtiger to biblioteka renderująca dla strumieni Kate, korzystająca z
bibliotek Pango i Cairo.

%package devel
Summary:	Header files for libtiger library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtiger
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libkate-devel >= 0.2.0
Requires:	pango-devel >= 1:1.16

%description devel
This package contains the header files for developing applications
that use libtiger library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libtiger.

%package static
Summary:	Static libtiger library
Summary(pl.UTF-8):	Statyczna biblioteka libtiger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtiger library.

%description static -l pl.UTF-8
Statyczna biblioteka libtiger.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/src/*.[ch] $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libtiger

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/libtiger.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtiger.so.5

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libtiger.so
%{_libdir}/libtiger.la
%{_includedir}/tiger
%{_pkgconfigdir}/tiger.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libtiger.a
