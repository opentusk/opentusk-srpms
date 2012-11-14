#
# tusk3-apache - specifically installed in /usr/local/fop for TUSK use
#

# Use this for listing perl files
%define filelist %{pkgname}-%{version}-filelist

%define realname apache

Summary: TUSK 3 packaging of Apache 1.3.41 for RHEL
Name: tusk3-%{realname}
Version: 1.3.41
Release: 0.1%{?_dist}
Group: TUSK
License: Apache License, version 1.0
Packager:   TUSK Developers <tuskdev@elist.tufts.edu>
URL: http://httpd.apach.org/
Group: System Environment Daemons
Source0: %{name}-%{version}.tar.gz
Source1: ABOUT_APACHE
Source2: LICENSE
Source3: README
Requires: /sbin/chkconfig
# Used to analyze list of packaged files
BuildRequires: perl(File::Find)
Provides: apache = %{version}-%{release}
Provides: mod_perl = 1.31
Provides: webserver
#BuildArch: i386

# Derived from original but undocumentd binary RPM
Requires: coreutils
Requires: sed
Requires: gdbm 
Requires: grep 
Requires: libcrypto.so.6 
Requires: libcrypt.so.1(GLIBC_2.0) 
Requires: libc.so.6(GLIBC_2.0) 
Requires: libc.so.6(GLIBC_2.1) 
Requires: libc.so.6(GLIBC_2.1.3) 
Requires: libc.so.6(GLIBC_2.2) 
Requires: libc.so.6(GLIBC_2.3) 
Requires: libc.so.6(GLIBC_2.3.3) 
Requires: libc.so.6(GLIBC_2.3.4) 
Requires: libc.so.6(GLIBC_2.4) 
Requires: libdb-4.3.so 
Requires: libdl.so.2 
Requires: libdl.so.2(GLIBC_2.0) 
Requires: libdl.so.2(GLIBC_2.1) 
Requires: libgdbm.so.2 
Requires: libm.so.6 
Requires: libm.so.6(GLIBC_2.0) 
Requires: libnsl.so.1 
Requires: libperl.so 
Requires: libpthread.so.0(GLIBC_2.0) 
Requires: libresolv.so.2 
Requires: libssl.so.6 
Requires: libutil.so.1 
Requires: perl >= 0:5.003_97
Requires: perl(AnyDBM_File) 
Requires: perl(Apache) 
Requires: perl(Apache::Connection) 
Requires: perl(Apache::Constants) 
Requires: perl(Apache::File) 
Requires: perl(Apache::ModuleConfig) 
Requires: perl(Apache::PerlRun) 
Requires: perl(Apache::Registry) 
Requires: perl(Apache::RegistryNG) 
Requires: perl(Apache::Server) 
Requires: perl(Benchmark) 
Requires: perl(BSD::Resource) 
Requires: perl(Config) 
Requires: perl(constant) 
Requires: perl(Cwd) 
Requires: perl(Data::Dumper) 
Requires: perl(Devel::Symdump) 
Requires: perl(DynaLoader) 
Requires: perl(Exporter) 
Requires: perl(Fcntl) 
Requires: perl(File::Basename) 
Requires: perl(File::Copy) 
Requires: perl(FileHandle) 
Requires: perl(File::Path) 
Requires: perl(IO::File) 
Requires: perl(lib) 
Requires: perl(mod_perl) 
Requires: perl(mod_perl) >= 1.17
Requires: perl(strict) 
Requires: perl(subs) 
Requires: perl(vars) 
Requires: chkconfig
Requires: sh-utils 
Requires: textutils 
Requires: perl
Requires: shadow-utils


# This will cause problems soon with architecture compiled RPM's.
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Apache is a powerful, full-featured, efficient, and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

This distribution in /usr/local/apache is specifically for TUSK 3.12
and conflicts with modern httpd.

%prep
# Tarball is pulled from old binary RPFM for i386
# Do not attempt to build from real source without further documentation
%setup -q
%{__cp} %{SOURCE1} .
%{__cp} %{SOURCE2} .
%{__cp} %{SOURCE3} .

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}

%{__cp} -pr usr %{buildroot}/usr

# Set up init script for reference
%{__mkdir_p} %{buildroot}/etc/rc.d/init.d
%{__ln_s} /usr/local/tusk/current/bin/apachectl %{buildroot}/etc/rc.d/init.d/httpd

# no empty directories
find %{buildroot}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

# Collect list of perl files
%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

# Tweak for Apache setup
sed -i '/\/usr\/share\/man\//d' %filelist
sed -i '/\/usr\/local\/apache\/htdocs\//d' %filelist

echo '%doc  ABOUT_APACHE LICENSE README' >> %filelist
echo '%doc /usr/share/man/*/*' >> %filelist
#echo '%doc /usr/local/apache/htdocs/manual' >> %filelist
echo '/etc/rc.d/init.d/httpd' >> %filelist

%pre
# Add the "apache" user
/usr/sbin/useradd -c "Apache" -u 48 \
        -s /sbin/nologin -r -d %{contentdir} apache 2> /dev/null || :

%post
# Register the httpd service
/sbin/chkconfig --add httpd

%preun
if [ $1 = 0 ]; then
        /sbin/service httpd stop > /dev/null 2>&1
        /sbin/chkconfig --del httpd
fi

%posttrans
/sbin/service httpd condrestart >/dev/null 2>&1 || :

%clean
rm -rf %{buildroot}

%verifyscript
#perl -e 'eval {require Apache::Session::Wrapper; print "Installed\n";}; if($@) {print "Not installed\n";}'

%files -f %filelist
%defattr(-,root,root)
#%doc /usr/share/man/*/*
#%doc /usr/local/apache/htdocs/manual
#/usr/local/apache/bin
#/usr/local/apache/cgi-bin
#/usr/local/apache/conf
#/usr/local/apache/htdocs/*.*
#/usr/local/apache/icons
#/usr/local/apache/include
#/usr/local/apache/libexec

%changelog
* Tue Aug 21 2012 Nico Kadel-Garcia <ikadel01@tufts.edu> - 1.0
- Build tusk3-apache package from old apache-1.3.41 binary RPM
- Provide 'tusk3-apache' name to avoid conflicts with 'apache' obsolescence
- List mod_perl

