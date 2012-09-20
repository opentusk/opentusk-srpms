Summary: XPDF
Name: xpdf
Version: 3.03
Release: 1
Group: TUSK
License: GNU General Pulbic License (GPL), version 2 or 3
packager: TUSK Developers <tuskdev@elist.tufts.edu>
URL: http://foolabs.com/xpdf
Group: Development/Libraries
Source: xpdf-3.03.tar.gz
Requires: freetype
Provides: pdftops
Provides: pdftotext
Provides: pdfinfo
Provides: pdffonts
Provides: pdfdetach
Provides: pdfimages

Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Xpdf is an open source viewer for Portable Document Format (PDF) files.  (These are also sometimes also called 'Acrobat' files, from the name of Adobe's PDF software.)  The Xpdf project also includes a PDF text extractor, PDF-to-PostScript converter, and various other utilities.

Xpdf runs under the X Window System on UNIX, VMS, and OS/2.  The non-X components (pdftops, pdftotext, etc.) also run on Windows and Mac OSX systems and should run on pretty much any system with a decent C++ compiler.  Xpdf will run on 32-bit and 64-bit machines.  


%prep
%setup xpdf-3.03.tar.gz

%build
./configure --with-freetype2-library=/usr/lib --with-freetype2-includes=/usr/include/freetype2/ --prefix %{buildroot}
make

%install
rm -rf %{buildroot}
make install

%clean
rm -rf %{buildroot}

%verifyscript


%files
%defattr(-,root,root)
/bin/pdfdetach
/bin/pdffonts
/bin/pdfimages
/bin/pdfinfo
/bin/pdftops
/bin/pdftotext
/etc/xpdfrc
/share/man/man1/pdfdetach.1
/share/man/man1/pdffonts.1
/share/man/man1/pdfimages.1
/share/man/man1/pdfinfo.1
/share/man/man1/pdftops.1
/share/man/man1/pdftotext.1
/share/man/man5/xpdfrc.5

