Summary:	Dillo configuration script
Summary(pl):	Skrypt configuruj±cy dillo
Name:		dillo-config
Version:	1.0
Release:	1
License:	Unknown
Group:		X11/Applications/Networking
Source0:	http://www.see.ed.ac.uk/~rjt/dillo/%{name}
# Source0-md5:	40129e1364bd7e0ed12322c58a09aa5d
URL:		http://www.see.ed.ac.uk/~rjt/dillo/dillo-config
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Dillo configuration script, by Bob Thomson (rjt@ee.ed.ac.uk).

%description -l pl
Skrypt konfiguruj±cy dillo napisany przez Boba Thomsona
(rjt@ee.ed.ac.uk).

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
