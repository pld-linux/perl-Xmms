#
# Conditional build:
# _without_tests - do not perform "make test"
#

# I'm not sure if running these tests is safe..
%define		_without_tests 1

%include	/usr/lib/rpm/macros.perl
%define		pdir	Xmms
%define		pnam	Perl
Summary:	Perl modules for interaction with xmms
Summary(pl):	Modu³y perla pozwalaj±ce na interakcjê z xmms
Name:		perl-Xmms
Version:	0.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(anything_fake_or_conditional)"

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
# Don't use pipes here: they generally don't work. Apply a patch.
perl Makefile.PL
# %{__make}
# if module isn't noarch, use:
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# use macros:
#%{perl_sitelib}/...
%{perl_sitearch}/Xmms.pm
%{perl_sitearch}/Xmms
%dir %{perl_sitearch}/auto/Xmms
%dir %{perl_sitearch}/auto/Xmms/SongChange
%{perl_sitearch}/auto/Xmms/SongChange/SongChange.so
%dir %{perl_sitearch}/auto/Xmms/Remote
%{perl_sitearch}/auto/Xmms/Remote/Remote.so
%dir %{perl_sitearch}/auto/Xmms/Config
%{perl_sitearch}/auto/Xmms/Config/Config.so
%{_mandir}/man3/*
