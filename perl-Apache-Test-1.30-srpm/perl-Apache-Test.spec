# $Id: perl-Apache-Test.spec 8085 2009-12-09 12:52:36Z cmr $
# Authority: dag
# Upstream: Fred Moyer <fred$redhotpenguin,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Test

Summary: Perl module contains a Test.pm wrapper with helpers for testing Apache
Name: perl-Apache-Test
Version: 1.30
Release: 0.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Test/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Test-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: rpm-macros-rpmforge
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(Perl::Critic) >= 1.105
BuildRequires: perl(Perl::Critic::Utils) >= 1.105
BuildRequires: perl(Perl::Critic::Violation) >= 1.105
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
Requires: perl(Carp)
Requires: perl(English)
Requires: perl(Perl::Critic) >= 1.105
Requires: perl(Perl::Critic::Utils) >= 1.105
Requires: perl(Perl::Critic::Violation) >= 1.105
Requires: perl(Test::Builder)
Requires: perl(strict)
Requires: perl(warnings)

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Apache-Test is a Perl module contains a Test.pm wrapper with helpers
for testing Apache.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE MANIFEST META.yml README ToDo install-pl
%doc %{_mandir}/man3/Apache::*.3pm*
%doc %{_mandir}/man3/Bundle::ApacheTest.3pm*
%{perl_vendorlib}/Apache/
%dir %{perl_vendorlib}/Bundle/
%{perl_vendorlib}/Bundle/ApacheTest.pm

%changelog
* Wed Nov 28 2012 Nico Kadel-Garcia <nico.kadel@tufts.edu> - 1.30-0.2
- Add rpm-macros-rpmforge dependency for RHEL 5.

* Wed Dec 09 2009 Christoph Maser <cmr@financial.com> - 1.30-2 - 8085/cmr
- Turn off auto-dependencies

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.29-1
- Initial package. (using DAR)
