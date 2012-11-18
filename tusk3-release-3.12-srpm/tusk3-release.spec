Summary: TUSK 3.x Repo Server
Name: tusk3-release
Version: 3.12
Release: 0.2%{?dist}
Group: TUSK
License: TUFTS License
packager: TUSK Developers <tuskdev@elist.tufts.edu>
URL: http://tusk.tufts.edu
Group: Applications/Internet
Provides: tusk(repo)
Source1: tusk3.repo
Source2: http://repo3.tusk.tufts.edu/RPM-GPG-KEY-TUSK-3

Obsoletes: tusk-repo
Obsoletes: TUSK-repo

BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}
Requires: /etc/yum.repos.d
Requires: /etc/pki/rpm-gpg
Requires: /etc/redhat-release

%description
This enables access to the TUSK %{vesion} repository

%prep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/yum.repos.d
cp %{SOURCE1} %{buildroot}/etc/yum.repos.d

mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cp %{SOURCE2} %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-TUSK-3

%pre
echo Some TUSK packages are also taken from Repoforge and EPEL.
echo If you do not already connect to thes, consider using these commands:
echo Activate EPEL:
echo     yum install --nogpg epel-release
echo Activate Repoforge, but disable by default
echo     yum install --nogpg rpmforge-release
echo     sed -i 's/^enabled.*/enabled = 0/g' /etc/yum.repos.d/rpmforge-release

%post

%clean

%verifyscript

%files
/etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Wed Nov 14 2012 nico.kadel@tufts.edu - 3.12-0.2
- Update to 3.12
- Add conflicts
- Renamem to 'tusk3-release'
- Point to new repo3.tusk.tufts.edu server.
- Use source files, not cat from .spec file

* Fri Aug 17 2012 ikadel@tufts.edu - 1.2-0.1
- Update Johnls old 1.1 vresion
- Discard unused source tarball, all components are in .spec file
- Eliminate post scripted releasever settings, use yum settings
- Add dependencies for /etc/pki/rpm-gpg, /etc/yum.repos.d,,
  and /etc/redhat-release
