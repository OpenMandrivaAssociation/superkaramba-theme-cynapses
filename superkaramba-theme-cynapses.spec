%define theme_name cynapses

Summary:	Monitoring theme for superkaramba
Name:		superkaramba-theme-%{theme_name}
Version:	2.0
Release:	8
License:	GPL
Group:		Monitoring
Url:		http://kde-look.org/content/show.php?content=11405
Source0:	11405-%{theme_name}_karamba.tar.bz2
Requires:	superkaramba
BuildArch:	noarch

%description
This is a superkaramba theme which is a desktop applet that displays
system information.

%files
%doc ChangeLog
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*

%post
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/sys_mon.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
cat %{_datadir}/apps/superkaramba/themes/default.theme | grep -v "%{theme_name}" > %{_datadir}/apps/superkaramba/themes/default.theme
exit 0
fi

#----------------------------------------------------------------------------

%prep
%setup -q -n %{theme_name}_karamba

%build

%install
mkdir -p %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}
chmod 755 %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}/scripts/mails_pop3.pl
chmod 755 %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}/scripts/osinfo.sh

