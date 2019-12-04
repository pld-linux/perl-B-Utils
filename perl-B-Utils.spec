#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	B
%define		pnam	Utils
%include	/usr/lib/rpm/macros.perl
Summary:	B::Utils - helper functions for op tree manipulation
Summary(pl.UTF-8):	B::Utils - funkcje pomocnicze do operacji na drzewie op
Name:		perl-B-Utils
Version:	0.27
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/B/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	340d6461afcec016ce6d0a0ba27290ba
URL:		http://search.cpan.org/dist/B-Utils/
BuildRequires:	perl-ExtUtils-Depends >= 0.302
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These functions make it easier to manipulate the op tree.

%description -l pl.UTF-8
Te funkcje ułatwiają operacje na drzewie op.

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
%{perl_vendorarch}/B/Utils.pm
%dir %{perl_vendorarch}/B/Utils
%dir %{perl_vendorarch}/B/Utils/Install
%{perl_vendorarch}/B/Utils/Install/BUtils.h
%{perl_vendorarch}/B/Utils/Install/Files.pm
%{perl_vendorarch}/B/Utils/Install/typemap
%{perl_vendorarch}/B/Utils/OP.pm
%dir %{perl_vendorarch}/auto/B
%dir %{perl_vendorarch}/auto/B/Utils
%attr(755,root,root) %{perl_vendorarch}/auto/B/Utils/Utils.so
%{_mandir}/man3/B::Utils*.3pm*
