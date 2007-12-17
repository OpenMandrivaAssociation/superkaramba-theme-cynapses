%define base_name       superkaramba-theme
%define theme_name      cynapses
%define name            %{base_name}-%{theme_name}
%define version         2.0
%define release         %mkrel 1

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: Monitoring theme for superkaramba
License: GPL
Group:   Monitoring
Source:  11405-%{theme_name}_karamba.tar.bz2
URL:     http://kde-look.org/content/show.php?content=11405
Requires: superkaramba >= 0.35
Requires: python

%description
This is a superkaramba theme which is a desktop applet 
that displays system information.


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}_karamba

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name} 
chmod 755 %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name}/scripts/mails_pop3.pl
chmod 755 %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name}/scripts/osinfo.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/sys_mon.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
cat %{_datadir}/apps/superkaramba/themes/default.theme | grep -v "%{theme_name}" > %{_datadir}/apps/superkaramba/themes/default.theme
fi


%files
%defattr(-,root,root)
%doc ChangeLog
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*



