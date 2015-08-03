# $Id$
# Refer to the following for more info on .spec file syntax:
#   http://www.rpm.org/max-rpm/
#   http://www.rpm.org/max-rpm-snapshot/	(Updated version of above)
#   http://docs.fedoraproject.org/drafts/rpm-guide-en/
# More links may be available from http://www.rpm.org

%define release %{relnum}.%{dist}

Summary: Build Debian-compatible .deb packages from RPM .spec files
Name: debbuild
Version: #VERSION#
Release: %{release}
Source: https://secure.deepnet.cx/releases/debbuild/debbuild-%{version}.tar.gz
Group: Development/Tools
License: GPLv2+
Packager: Kris Deugau <kdeugau@deepnet.cx>
Requires: perl, build-essential, pax, fakeroot, bash
%if %{_vendor} == "debbuild"
Recommends: patch, bzip2, xz-utils
# For setting DEB_HOST_ARCH
Recommends: dpkg-architecture
Suggests: rpm, subversion
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
debbuild attempts to build Debian-friendly semi-native packages from
RPM spec files, RPM-friendly tarballs, and RPM source packages
(.src.rpm files).  It accepts most of the options rpmbuild does, and
should be able to interpret most spec files usefully.  Perl modules
should be handled via CPAN+dh-make-perl instead as it's simpler
than even tweaking a .spec template.

Note that patch is not strictly required unless you have .spec files
with %patch directives, and RPM is not required unless you wish to
rebuild .src.rpm source packages as .deb binary packages.

%prep
# Steps to unpack and patch source as needed
%setup -q

%build
# nothing to do here

%install
# Steps to install to a temporary location for packaging
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Fill in the pathnames to be packaged here
%files
%{_bindir}/*
%{_mandir}/man8/*

%changelog
* Sun Jul 19 2015  Kris Deugau <kdeugau@deepnet.cx>
- Remove the stack of %if's determining the Debian dist;  use the recently
  refined %{dist} instead

* Thu Feb 28 2008  Kris Deugau <kdeugau@deepnet.cx> -1
- Initial package
