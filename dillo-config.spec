Summary:	Dillo configuration script
Summary(pl):	Skrypt configuruj±cy dillo
Name:		dillo-config
Version:	1.0
Release:	1
License:	Unknown
Group:		X11/Applications/Networking
Source0:	http://www.ee.ed.ac.uk/~rjt/dillo/%{name}
URL:		http://www.ee.ed.ac.uk/~rjt/dillo/config.html
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:   noarch

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dillo configuration script, by Bob Thomson (rjt@ee.ed.ac.uk).

%description -l pl
Skrypt konfiguruj±cy dillo napisany przez Boba Thomsona
(rjt@ee.ed.ac.uk).

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
