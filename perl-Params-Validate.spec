%include	/usr/lib/rpm/macros.perl
Summary:	Params::Validate perl module
Summary(pl):	Modu³ perla Params::Validate
Name:		perl-Params-Validate
Version:	0.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz
Patch0:		%{name}-rpmperl-automation-workaround.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Params::Validate - Validate method/function parameters

%prep
%setup -q -n Params-Validate-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
%dir %{perl_sitelib}/Params/Validate
%{perl_sitelib}/Params/*.pm
%{perl_sitelib}/Params/Validate/*.pm

%{_mandir}/man3/*
