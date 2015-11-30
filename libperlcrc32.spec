# don`t strip
%define __autobuild__ 0

%if %{__autobuild__}
%define version PKG_VERSION
%define branch GIT_TAG
%else
%define version %(/bin/date +"%Y%m%d.%H%M")
%define branch master
%endif

Name: libperlcrc32
Version: %{version}
Release: 1

Summary: Perl implementation of CRC32 algorithm
License: BSD
Group: Development/Libraries
URL: https://github.com/derElektrobesen/perl_crc32

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %{__autobuild__}
Source0: %{name}-GIT_TAG.tar.bz2
%endif

%description
Perl implementation of CRC32 algorithm

%if %{__autobuild__}
From tag: GIT_TAG
Git hash: GITHASH
Build by: BUILD_USER
%endif

%prep
#rm -rf %{name}*
%setup -q -n %{name}

%build
make so

%install
install -d %{buildroot}/%{_libdir}
install -m 755 libperlcrc32.so %{buildroot}/%{_libdir}

%files
/%{_libdir}/libperlcrc32.so
