%include	/usr/lib/rpm/macros.perl
Summary:	Params::Validate Perl module
Summary(cs):	Modul Params::Validate pro Perl
Summary(da):	Perlmodul Params::Validate
Summary(de):	Params::Validate Perl Modul
Summary(es):	M�dulo de Perl Params::Validate
Summary(fr):	Module Perl Params::Validate
Summary(it):	Modulo di Perl Params::Validate
Summary(ja):	Params::Validate Perl �⥸�塼��
Summary(ko):	Params::Validate �� ����
Summary(no):	Perlmodul Params::Validate
Summary(pl):	Modu� perla Params::Validate
Summary(pt_BR):	M�dulo Perl Params::Validate
Summary(pt):	M�dulo de Perl Params::Validate
Summary(ru):	������ ��� Perl Params::Validate
Summary(sv):	Params::Validate Perlmodul
Summary(uk):	������ ��� Perl Params::Validate
Summary(zh_CN):	Params::Validate Perl ģ��
Name:		perl-Params-Validate
Version:	0.24
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Attribute-Handlers
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Params::Validate::Heavy)'

%description
Params::Validate - Validate method/function parameters.

%description -l pl
Params::Validate - metoda/funkcja sprawdzaj�ca poprawno�� parametr�w.

%prep
%setup -q -n Params-Validate-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitelib}/Params
%{perl_sitelib}/Params/*.pm
%dir %{perl_sitelib}/Attribute/Params
%{perl_sitelib}/Attribute/Params/*.pm
%{_mandir}/man3/*
