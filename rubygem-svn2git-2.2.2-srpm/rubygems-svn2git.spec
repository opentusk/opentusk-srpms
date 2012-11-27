# Generated from svn2git-2.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname svn2git
%define version 2.2.2
%define release 0.1

Summary: A tool for migrating svn projects to git
Name: rubygems-%{rbname}

Version: %{version}
Release: %{release}%{?dist}
Group: Development/Ruby
License: Distributable
URL: https://www.negativetwenty.net/redmine/projects/svn2git
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
Source1: rubygems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.3.7
BuildRequires: ruby 
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: ruby(Svn2git) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description



%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/svn2git
%doc %{gemdir}/gems/svn2git-2.2.2/ChangeLog.markdown
%{gemdir}/gems/svn2git-2.2.2/MIT-LICENSE
%doc %{gemdir}/gems/svn2git-2.2.2/README.markdown
%{gemdir}/gems/svn2git-2.2.2/Rakefile
%{gemdir}/gems/svn2git-2.2.2/VERSION.yml
%{gemdir}/gems/svn2git-2.2.2/bin/svn2git
%{gemdir}/gems/svn2git-2.2.2/lib/svn2git.rb
%{gemdir}/gems/svn2git-2.2.2/lib/svn2git/blah.rb
%{gemdir}/gems/svn2git-2.2.2/lib/svn2git/migration.rb
%{gemdir}/gems/svn2git-2.2.2/svn2git.gemspec


%doc %{gemdir}/doc/svn2git-2.2.2
%{gemdir}/cache/svn2git-2.2.2.gem
%{gemdir}/specifications/svn2git-2.2.2.gemspec

%changelog
