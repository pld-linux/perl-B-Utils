#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	B
%define		pnam	Utils
Summary:	B::Utils - helper functions for op tree manipulation
Summary(pl.UTF-8):	B::Utils - funkcje pomocnicze do obróbki drzewa op
Name:		perl-B-Utils
Version:	0.07
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d69e7d81a24093a41e90e19f8bdb54e3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	perl-Module-Info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These functions make it easier to manipulate the op tree.

%description -l pl.UTF-8
Te funkcje ułatwiają obrabianie drzewa op.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/B/Utils
%dir %{perl_vendorarch}/B/Utils/Install
%dir %{perl_vendorarch}/auto/B/Utils/
%{perl_vendorarch}/B/Utils.pm
%{perl_vendorarch}/B/Utils/Install/BUtils.h
%{perl_vendorarch}/B/Utils/Install/Files.pm
%{perl_vendorarch}/B/Utils/Install/typemap
%{perl_vendorarch}/B/Utils/OP.pm
%{perl_vendorarch}/auto/B/Utils/Utils.bs
%attr(755,root,root) %{perl_vendorarch}/auto/B/Utils/Utils.so
%{_mandir}/man3/*
