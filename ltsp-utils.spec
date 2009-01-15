Summary:   Linux Terminal Server Project (ltsp.org) utilities
Name:      ltsp-utils
Version:   0.25
Release:   %mkrel 1
License:   GPL
URL:       http://www.ltsp.org
Group:     System/Servers
Source:    http://ltsp.mirrors.tds.net/pub/ltsp/utils/%{name}-%{version}-0.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires:  dhcp
Requires:  nfs-utils
Requires:  tftp-server
Requires:  perl(LWP), perl(URI), perl(Digest::MD5), perl(Term::Cap)

%description
This package includes the following utilities for LTSP server:
  ltspadmin   For installing and managing the packages
              on an LTSP server.
  ltspcfg     For configuring the services on an LTSP server.
  ltspinfo    For querying the workstation, to learn things,
              such as which sound daemon is being used.

%prep
%setup -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install ltspadmin ltspcfg $RPM_BUILD_ROOT%{_sbindir}
install ltspinfo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog notes.txt COPYING
%{_bindir}/ltspinfo
%{_sbindir}/ltspadmin
%{_sbindir}/ltspcfg
