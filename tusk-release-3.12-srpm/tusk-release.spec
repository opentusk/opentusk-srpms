Name:		tusk-release
Version:	3.12
Release:	0.1%{?dist}
Summary:	TUSK release file and RPM configuration management

Group:		System Environment/Base
License:	GPLv2

URL:		http://www.tusk.tufts.edu
Source0:	http://repo3.tusk.tufts.edu/RPM-GPG-KEY-TUSK-3
Source1:	GPL
Source2:	tusk.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       redhat-release >=  %{version}
Conflicts:      fedora-release
# Avoid old tusk repo package
Conflicts:	tusk-repo

%description
This package contains yum configurations for the publicly available
TUSK and OpenTUSK packages, especially the Apache 1.3 for
TUSK. TUSK is deprecated in favor of OpenTUSK: switch to OpenTUSK
4.00 ASAP.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -pm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Wed Sep 26 2012 Nico Kadel-Garcia <nico.kadel@tufts.edu> - 3.12-0.1
- Create new tusk-release SRPM from epel-release format
- Specify for TUSK 3.12 relevant repository with old apache and modules
