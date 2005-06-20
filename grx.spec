#
# Conditional build:
%bcond_with	gpc		# enable gpc support
%bcond_without	bgi		# disable BGI support
%bcond_without	bmp		# disable BMP support
%bcond_without	jpeg		# disable JPEG support
%bcond_without	tiff		# disable TIFF support
#
Summary:	2D graphics C library
Summary(pl):	Biblioteka w C do grafiki 2D
Name:		grx
Version:	2.4.5
%define		tar_version	%(echo %{version} | tr -d .)
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.gnu.de/software/GRX/download/%{name}%{tar_version}.tar.gz
# Source0-md5:	6b14fcdfe993f12521333ffd1edbfb8f
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnu.de/software/GRX/download/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRX is a 2D graphics C library originaly written by Csaba Biegl for
DJ Delorie's DOS port of the GCC compiler. Now it support a big range
of platforms, the main four are: DOS (DJGPPv2), Linux console, X11 and
Win32 (Mingw).

%description -l pl
GRX to biblioteka w C do grafiki 2D, oryginalnie napisana przez Csabê
Biegla dla dosowego portu DJ Delorie kompilatora GCC. Teraz obs³uguje
wiele platform, g³ównymi s±: DOS (DJGPPv2), konsola Linuksa, X11 oraz
Win32 (Mingw).

%package devel
Summary:	Header files for grx library
Summary(pl):	Pliki nag³ówkowe biblioteki grx
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for grx library.

%description devel -l pl
Pliki nag³ówkowe biblioteki grx.

%package static
Summary:	Static grx library
Summary(pl):	Statyczna biblioteka grx
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static grx library.

%description static -l pl
Statyczna biblioteka grx.

%prep
%setup -q -n %{name}%{tar_version}
%patch0 -p1

%build
./configure \
	--prefix=/usr \
	--target=X11 \
%{?with_jpeg:--enable-jpeg} \
	--enable-png \
	--enable-z \
	--enable-png-z \
%{?with_tiff:--enable-tiff} \
%{?with_bmp:--enable-bmp} \
	--enable-print \
%{?with_gpc:--enable-gpc} \
	--enable-shared \
%{?with_bgi:--enable-bgi} \
	--with-fontpath=/usr/share/grx/fonts

%{__make} \
	CCOPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-bin	\
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-fonts	\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme doc/{changes,credits.doc,fna.txt}
%{?with_bgi:%doc doc/changes.bgi}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/grx

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
