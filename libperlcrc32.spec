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
Packager: BUILD_USER
Source0: perl_crc32-GIT_TAG.tar.bz2
%else
Packager: Pavel Berezhnoy <p.berezhnoy@corp.mail.ru>
%endif

%description
Perl implementation of CRC32 algorithm

%if %{__autobuild__}
From tag: GIT_TAG
Git hash: GITHASH
Build by: BUILD_USER
%endif

%package devel
Summary: Header files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header files for %{name}

%{lua:
if rpm.expand("%{__autobuild__}") == '1'
then
print("From tag: GIT_TAG\n")
print("Git hash: GITHASH\n")
print("Build by: BUILD_USER\n")
end}

%prep
%if %{__autobuild__}
%setup -q -n perl_crc32
%else
rm -rf %{name}-%{version}
git clone https://github.com/derElektrobesen/perl_crc32.git %{name}-%{version}
%setup -T -D -n %{name}-%{version}
%endif

%build
make so

%build devel
make install_headers DESTDIR=%{buildroot}/%{_includedir}

%install
install -d %{buildroot}/%{_libdir}
install -m 755 libperlcrc32.so %{buildroot}/%{_libdir}

%files
/%{_libdir}/libperlcrc32.so

%files devel
%{_includedir}/*

%post
ldconfig

%changelog
%if %{__autobuild__}
GIT_LOG
%endif

