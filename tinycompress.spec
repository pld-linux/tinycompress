#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Userspace library for ALSA compressed APIs
Summary(pl.UTF-8):	Biblioteka przestrzeni użytkownika dla API systemu ALSA dla danych skompresowanych
Name:		tinycompress
Version:	1.2.11
Release:	1
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/tinycompress/%{name}-%{version}.tar.bz2
# Source0-md5:	d868f323161f01b98db3bebbe9093ad3
URL:		https://www.alsa-project.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tinycompress is a userspace library for anyone who wants to use the
ALSA compressed APIs introduced in Linux 3.3.

This library provides the APIs to open a ALSA compressed device and
read/write compressed data like MP3 etc to it.

%description -l pl.UTF-8
tinycompress to biblioteka przestrzeni użytkownika dla chcących
wykorzystywać API systemu ALSA dla danych skompresowanych, wprowadzone
w Linuksie 3.3.

Biblioteka udostępnia API do otwierania urządzeń kompresowanych ALSA
oraz odczytu/zapisu przez nie danych skompresowanych np. MP3.

%package devel
Summary:	Header files for tinycompress library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tinycompress
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tinycompress library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tinycompress.

%package static
Summary:	Static tinycompress library
Summary(pl.UTF-8):	Statyczna biblioteka tinycompress
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tinycompress library.

%description static -l pl.UTF-8
Statyczna biblioteka tinycompress.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies, obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtinycompress.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/cplay
%attr(755,root,root) %{_bindir}/crecord
%attr(755,root,root) %{_libdir}/libtinycompress.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtinycompress.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtinycompress.so
%{_includedir}/tinycompress
%{_pkgconfigdir}/tinycompress.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtinycompress.a
%endif
