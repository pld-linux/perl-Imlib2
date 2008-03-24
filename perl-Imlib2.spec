#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Imlib2
%define		pnam	Object
Summary:	Perl extension to Imlib2
Summary(pl.UTF-8):	Rozszerzenie Perla do Imlib2
Name:		perl-Imlib2
%define	_pkgname	Imlib2_Perl
Version:	0.02
%define	_snap	20050701
Release:	0.%{_snap}.0.1
# not specified; should be same as perl ?
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://dl.sourceforge.net/enlightenment/%{_pkgname}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/misc/%{_pkgname}-%{_snap}.tar.gz
# Source0-md5:	286d85a0648e95062b2e8d6d11be1fa5
URL:		http://enlightenment.org/
BuildRequires:	freetype1-devel
BuildRequires:	imlib2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension to Imlib2. Imlib2 can be very useful in CGI scripts
and, as examples shows, with GTK+. Imlib2::Object permits working
directly on files.

%description -l pl.UTF-8
Rozszerzenie Perla do Imlib2. Imlib2 może być bardzo przydatna w
skryptach CGI i, jak pokazują przykłady, w GTK+. Imlib2::Object
umożliwia pracę bezpośrednio na plikach.

%prep
%setup -q -n %{_pkgname}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* Imlib2/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Imlib2.pm
%{perl_vendorarch}/Imlib2
%dir %{perl_vendorarch}/auto/Imlib2
%{perl_vendorarch}/auto/Imlib2/Imlib2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Imlib2/Imlib2.so
%{perl_vendorarch}/auto/Imlib2/autosplit.ix
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
