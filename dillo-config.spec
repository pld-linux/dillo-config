Summary:	Dillo configuration script
Summary(pl.UTF-8):   Skrypt configurujący dillo
Name:		dillo-config
Version:	1.0
Release:	3
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://oldeee.see.ed.ac.uk/~rjt/dillo/%{name}
URL:		http://www.see.ed.ac.uk/~rjt/dillo/config.html
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dillo configuration script, by Bob Thomson (rjt@ee.ed.ac.uk).

%description -l pl.UTF-8
Skrypt konfigurujący dillo napisany przez Boba Thomsona
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
