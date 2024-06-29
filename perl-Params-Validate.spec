#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Params
%define		pnam	Validate
Summary:	Params::Validate - validate method/function parameters
Summary(pl.UTF-8):	Params::Validate - sprawdzanie poprawności parametrów funkcji/metody
Name:		perl-Params-Validate
Version:	1.31
Release:	3
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef5f57387c2c9032b59fb23023cf5b25
URL:		https://metacpan.org/dist/Params-Validate
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build >= 0.3601
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers >= 0.79
BuildRequires:	perl-Module-Implementation >= 0.04
BuildRequires:	perl-Scalar-List-Utils >= 1.10
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Taint >= 0.02
%endif
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%{__perl} Build.PL \
	installdirs=vendor \
	--config cc="%{__cc}" \
	--config ld="%{__cc}" \
	--config optimize="%{rpmcflags}"

%{__perl} ./Build

%{?with_tests:%{__perl} ./Build test}

%install
rm -rf $RPM_BUILD_ROOT

%{__perl} ./Build install \
	destdir=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Params/Validate/XS/XS.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%dir %{perl_vendorarch}/Params
%{perl_vendorarch}/Params/Validate.pm
%{perl_vendorarch}/Params/ValidatePP.pm
%{perl_vendorarch}/Params/ValidateXS.pm
%{perl_vendorarch}/Params/Validate
%dir %{perl_vendorarch}/auto/Params
%dir %{perl_vendorarch}/auto/Params/Validate
%dir %{perl_vendorarch}/auto/Params/Validate/XS
%attr(755,root,root) %{perl_vendorarch}/auto/Params/Validate/XS/XS.so
%{_mandir}/man3/Params::Validate*.3pm*
