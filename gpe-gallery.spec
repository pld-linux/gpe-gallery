Summary:	GPE picture gallery
Summary(pl.UTF-8):	Galeria obrazów GPE
Name:		gpe-gallery
Version:	0.97
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	ba488fac2b1484862c2e52cd017793cb
URL:		http://gpe.linuxtogo.org/
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
BuildRequires:	pkgconfig
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define gpename %(echo %{name} | sed -e 's/gpe-//')

%description
GPE picture gallery, for embedded devices.

%description -l pl.UTF-8
Galeria obrazów GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/gpe/pixmaps/default/%{gpename}
%{_datadir}/gpe/pixmaps/default/%{gpename}/*.png
%{_pixmapsdir}/%{name}.png
