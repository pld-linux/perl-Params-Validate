#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Params
%define		pnam	Validate
Summary:	Params::Validate - validate method/function parameters
Summary(pl.UTF-8):	Params::Validate - sprawdzanie poprawności parametrów funkcji/metody
Name:		perl-Params-Validate
Version:	0.91
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22c5467a1d4673374a1b7b2dbcfd473e
URL:		http://search.cpan.org/dist/Params-Validate/
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Taint
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Params::Validate module allows you to validate method or function
call parameters to an arbitrary level of specificity.  At the simplest
level, it is capable of validating the required parameters were given
and that no unspecified additional parameters were passed in.

It is also capable of determining that a parameter is of a specific
type, that it is an object of a certain class hierarchy, that it
possesses certain methods, or applying validation callbacks to
arguments.

%description -l pl.UTF-8
Moduł Params::Validate pozwala na sprawdzanie poprawności parametrów,
z jakimi wywołana została funkcja lub metoda, na dowolnym poziomie
szczegółowości.  W najprostszym przypadku możliwe jest sprawdzenie,
czy podane zostały parametry wymagane i czy nie podano dodatkowych,
nie rozpoznawanych.

Potrafi także określić czy parametr jest konkretnego typu, czy jest
obiektem danej hierarchii, czy posiada zadane metody, lub przypisać
argumentom callbacki (a, i tak wszyscy wiedzą, o co chodzi... ;-> )
sprawdzające.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/Params
%dir %{perl_vendorarch}/auto/Params/Validate
%{perl_vendorarch}/auto/Params/Validate/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Params/Validate/*.so
%dir %{perl_vendorarch}/Attribute
%dir %{perl_vendorarch}/Attribute/Params
%{perl_vendorarch}/Attribute/Params/*.pm
%dir %{perl_vendorarch}/Params
%{perl_vendorarch}/Params/*.pm
%{_mandir}/man3/*
