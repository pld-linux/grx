#
# Conditional build:
# _with_gpc:		enable gpc support
# _without_bgi:		disable BGI support
# _without_bmp:		disable BMP support
# _without_jpeg:	disable JPEG support
# _without_tiff:	disable TIFF support
#
Summary:	-
Summary(pl):	-
Name:		grx
Version:	2.4.5
%define		tar_version	%(echo %{version} | sed 's:\\.::g')
Release:	1
License:	LGPL
Group:		Libraries
Vendor:		-
#Icon:		-
Source0:	http://www.gnu.de/software/GRX/download/%{name}%{tar_version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnu.de/software/GRX/download/
#BuildRequires:	-
#PreReq:		-
#Requires:	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Summary:	-
Summary(pl):	-
Group:		-

%description devel

%description devel -l pl

%package static
Summary:	-
Summary(pl):	-
Group:		-

%description static

%description static -l pl

%prep
%setup -q -n %{name}%{tar_version}
%patch0 -p1

%build
./configure \
	--prefix=/usr \
	--target=X11 \
%{!?_without_jpeg:--enable-jpeg} \
	--enable-png \
	--enable-z \
	--enable-png-z \
%{!?_without_tiff:--enable-tiff} \
%{!?_without_bmp:--enable-bmp} \
	--enable-print \
%{?_with_gpc:--enable-gpc} \
	--enable-shared \
%{!?_without_bgi:--enable-bgi} \
	--with-fontpath=/usr/share/grx/fonts

%{__make} CCOPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-bin	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-fonts	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme doc/{changes,credits.doc,fna.txt}
%{!?_without_bgi:%doc doc/changes.bgi}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/grx

%files devel
%defattr(644,root,root,755)
%doc doc/watcom.txt
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
