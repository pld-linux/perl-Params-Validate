#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Params
%define	pnam	Validate
Summary:	Params::Validate - validate method/function parameters
Summary(pl):	Params::Validate - sprawdzanie poprawno¶ci parametrów funkcji/metody
Name:		perl-Params-Validate
Version:	0.69
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c0e31f95ac8065c52a3cc18ad7be03f0
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
Modu³ Params::Validate pozwala na sprawdzanie poprawno¶ci parametrów,
z jakimi wywo³ana zosta³a funkcja lub metoda, na dowolnym poziomie
szczegó³owo¶ci.  W najprostrzym przypadku mo¿liwe jest sprawdzenie,
czy podane zosta³y parametry wymagane i czy nie podano dodatkowych,
nie rozpoznawanych.

Potrafi tak¿e okre¶liæ czy parametr jest konkretnego typu, czy jest
obiektem danej hierarchii, czy posiada zadane metody, lub przypisaæ
argumentom callbacki (a, i tak wszyscy wiedz±, o co chodzi... ;-> )
sprawdzaj±ce.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
