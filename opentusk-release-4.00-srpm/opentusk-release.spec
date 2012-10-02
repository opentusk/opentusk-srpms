Name:		opentusk-release
Version:	4.00
Release:	0.2%{?dist}
Summary:	OPENTUSK release file and RPM configuration management

Group:		System Environment/Base
License:	GPLv2

URL:		http://www.tusk.tufts.edu
Source0:	http://repo3.tusk.tufts.edu/RPM-GPG-KEY-OPENTUSK-4
Source1:	GPL
Source2:	opentusk.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       redhat-release >=  %{version}
Conflicts:      fedora-release
# Avoid old tusk repo package
Conflicts:	tusk-repo

%description
This package contains yum configurations for the publicly available
OpenTUSK version 4 packages, formerly TUSK version 3.

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
#%config(noreplace) /etc/yum.repos.d/*
%config /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Wed Sep 26 2012 Nico Kadel-Garcia <nico.kadel@tufts.edu> - 4.00-0.1
- Create new opentusk-release SRPM from epel-release format
- Specify for TUSK 4.00 relevant repository with RHEL 6 and x86_64 support

