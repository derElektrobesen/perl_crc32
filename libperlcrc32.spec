%define __autobuild__ 0

%if %{__autobuild__}
%define release 1
%else
%define release PKG_RELEASE
%endif

Summary: Perl implementation of CRC32 algorithm
Name: libperlcrc32
Version: 1.0
Release: 1
Group: Development/Libraries
URL: https://github.com/derElektrobesen/perl_crc32
License: BSD
%if %{__autobuild__}
Packager: BUILD_USER
Source0: libperlcrc32-GIT_TAG.tar.bz2
%else
Packager: Pavel Berezhnoy <p.berezhnoy@corp.mail.ru>
Source: libperlcrc32-1.0.tar.gz
%endif

%description
Perl implementation of CRC32 algorithm

%{lua:
if rpm.expand("%{__autobuild__}") == '1'
then
print("From tag: GIT_TAG\n")
print("Git hash: GITHASH\n")
print("Build by: BUILD_USER\n")
end}

%prep
%if %{__autobuild__}
%setup -q -n libperl_crc32
%else
%setup -q
%endif

%build
make %{?_smp_mflags} so

%install
install -d %{buildroot}/%{_libdir}
install -m 755 libperlcrc32.so %{buildroot}/%{_libdir}

%files
/%{_libdir}/libperlcrc32.so
