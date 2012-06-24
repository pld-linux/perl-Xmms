#
# Conditional build:
# _with_tests - perform "make test" (runs xmms)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Xmms
%define		pnam	Perl
Summary:	Perl modules for interaction with xmms
Summary(pl):	Modu�y perla pozwalaj�ce na interakcj� z xmms
Name:		perl-Xmms
Version:	0.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides perl modules for interaction with popular xmms
player. Most important ones are: Xmms, which provides shell-like
interface to xmms and Xmms::Remote, which is Perl interface to
xmms_remote API.

%description -l pl
Pakiet zawiera modu�y pozwalaj�ce na interakcj� z popularnym
odtwarzaczem xmms. Najwa�niejsze z tych modu��w to: Xmms, kt�ry
umo�liwia sterowanie xmms-em przez interfejs przypominaj�cy pow�ok�
i Xmms::Remote, kt�ry jest perlowym interfejsem do udost�pnianego
przez xmms-a API xmms_remote.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
