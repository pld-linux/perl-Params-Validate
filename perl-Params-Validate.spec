%include	/usr/lib/rpm/macros.perl
Summary:	Params::Validate perl module
Summary(pl):	Modu³ perla Params::Validate
Name:		perl-Params-Validate
Version:	0.16
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Params::Validate::Heavy)'

%description
Params::Validate - Validate method/function parameters.

%description -l pl
Params::Validate - metoda/funkcja sprawdzaj±ca poprawno¶æ parametrów.

%prep
%setup -q -n Params-Validate-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Params
%{perl_sitelib}/Params/*.pm
%dir %{perl_sitelib}/Attribute
%dir %{perl_sitelib}/Attribute/Params
%{perl_sitelib}/Attribute/Params/*.pm

%{_mandir}/man3/*
