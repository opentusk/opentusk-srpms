#
# fop-tusk - specifically installed in /usr/local/fop for TUSK use
#

%define _fopdir /usr/local/fop-%{version}
%define _foplink /usr/local/fop

%define realname fop

Summary: TUSK packaging of Apache FOP (Formatting Objects Processor)
Name: tusk-%{realname}
Version: 1.0
Release: 1.2%{?_dist}
Group: TUSK
License: Apache License, version 2.0
Packager:   TUSK Developers <tuskdev@elist.tufts.edu>
URL: http://xmlgraphics.apache.org/fop/
Group: Development/Libraries
Source0: http://archive.apache.org/dist/xmlgraphics/fop/binaries/fop-%{version}-bin.tar.gz
Source1: fop-tusk-settings.tar.gz
Source2: README.tusk
#Provides: fop
Requires: java

# This will cause problems soon with architecture compiled RPM's.
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Apache FOP (Formatting Objects Processor) is a print formatter driven
by XSL formatting objects (XSL-FO) and an output independent
formatter. It is a Java application that reads a formatting object
(FO) tree and renders the resulting pages to a specified
output. Output formats currently supported include PDF, PS, PCL, AFP,
XML (area tree representation), Print, AWT and PNG, and to a lesser
extent, RTF and TXT. The primary output target is PDF.

This distribution in %{fopdir} is built from binary tarballs, not
compiled, for use by TUSK software.

%prep
# Binary tarball has different folder from tarball name
%setup -q -n fop-%{version}
gzip -dc %{SOURCE1} | \
     tar xf - -C conf
install -m 644 %{SOURCE2} .

chmod -R a+sX,g-w,o-w .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_fopdir}
cp -pr * %{buildroot}%{_fopdir}
ln -s `basename %{_fopdir}` %{buildroot}%{_foplink}

%clean
rm -rf %{buildroot}

%verifyscript
#perl -e 'eval {require Apache::Session::Wrapper; print "Installed\n";}; if($@) {print "Not installed\n";}'

%files
%defattr(-,root,root)
%doc KEYS LICENSE NOTICE README README.tusk
# Link to default fop location, /usr/local/fop
%{_foplink}
# Top level files
%{_fopdir}/KEYS
%{_fopdir}/LICENSE
%{_fopdir}/NOTICE
%{_fopdir}/README
%{_fopdir}/README.tusk
# Binaries
%{_fopdir}/fop
%{_fopdir}/fop.bat
%{_fopdir}/fop.cmd
%{_fopdir}/fop.js
%{_fopdir}/status.xml

# Subdirectories
%{_fopdir}/build/
%{_fopdir}/conf/
%{_fopdir}/docs/
%{_fopdir}/examples/
%{_fopdir}/javadocs/
%{_fopdir}/lib/

%changelog
* Tue Aug 21 2012 Nico Kadel-Garcia <ikadel01@tufts.edu> - 1.0
- Rename package to 'tusk-fop', distinguish from EPEL fop package.
- Import John's original TUSK specific fop binary build,
  used insteed of source based SRPM for TUSK on RHEL 5 and 6
- Rebundle TUSK SRPM with subdirectories, not individual file listings
- Add dist to release
- Use _fopdir and _foplink insted of hard-coded /usr/local

