#
# Conditional build:
# _with_tests - perform "make test" (runs xmms)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Xmms
%define		pnam	Perl
Summary:	Perl modules for interaction with xmms
Summary(pl):	Modu³y perla pozwalaj±ce na interakcjê z xmms
Name:		perl-Xmms
Version:	0.12
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1fbf6d09330f7855dd80f3ceee8e6f7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides perl modules for interaction with popular xmms
player. Most important ones are: Xmms, which provides shell-like
interface to xmms and Xmms::Remote, which is Perl interface to
xmms_remote API.

%description -l pl
Pakiet zawiera modu³y pozwalaj±ce na interakcjê z popularnym
odtwarzaczem xmms. Najwa¿niejsze z tych modu³ów to: Xmms, który
umo¿liwia sterowanie xmms-em przez interfejs przypominaj±cy pow³okê
i Xmms::Remote, który jest perlowym interfejsem do udostêpnianego
przez xmms-a API xmms_remote.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Xmms.pm
%{perl_vendorarch}/Xmms
%dir %{perl_vendorarch}/auto/Xmms
%dir %{perl_vendorarch}/auto/Xmms/SongChange
%{perl_vendorarch}/auto/Xmms/SongChange/SongChange.so
%dir %{perl_vendorarch}/auto/Xmms/Remote
%{perl_vendorarch}/auto/Xmms/Remote/Remote.so
%dir %{perl_vendorarch}/auto/Xmms/Config
%{perl_vendorarch}/auto/Xmms/Config/Config.so
%{_mandir}/man3/*
