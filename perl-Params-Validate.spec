#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Params
%define	pnam	Validate
Summary:	Params::Validate - validate method/function parameters
Summary(pl):	Params::Validate - sprawdzanie poprawno�ci parametr�w funkcji/metody
Name:		perl-Params-Validate
Version:	0.59
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f14fe21888eec9f04bb7657e642d37db
BuildRequires:	perl-devel >= 5.6
%{!?_without_tests:BuildRequires:	perl-Attribute-Handlers}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Params::ValidatePP)'

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
Modu� Params::Validate pozwala na sprawdzanie poprawno�ci parametr�w,
z jakimi wywo�ana zosta�a funkcja lub metoda, na dowolnym poziomie
szczeg�owo�ci.  W najprostrzym przypadku mo�liwe jest sprawdzenie,
czy podane zosta�y parametry wymagane i czy nie podano dodatkowych,
nie rozpoznawanych.

Potrafi tak�e okre�li� czy parametr jest konkretnego typu, czy jest
obiektem danej hierarchii, czy posiada zadane metody, lub przypisa�
argumentom callbacki (a, i tak wszyscy wiedz�, o co chodzi... ;-> )
sprawdzaj�ce.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL --xs \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/Params/Validate
%{perl_vendorarch}/auto/Params/Validate/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Params/Validate/*.so
%dir %{perl_vendorarch}/Attribute/Params/*.pm
%dir %{perl_vendorarch}/Params/*.pm
%{_mandir}/man3/*
