%define base_name       superkaramba-theme
%define theme_name      cynapses
%define name            %{base_name}-%{theme_name}
%define version         2.0
%define release         %mkrel 6

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
BuildRoot: %{_tmppath}/%{name}-buildroot

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
exit 0
fi


%files
%defattr(-,root,root)
%doc ChangeLog
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*





%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0-6mdv2010.0
+ Revision: 434189
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-5mdv2009.0
+ Revision: 261238
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-4mdv2009.0
+ Revision: 253751
- rebuild

* Sun Mar 02 2008 Nicolas Lécureuil <neoclust@mandriva.org> 2.0-2mdv2008.1
+ Revision: 177557
- [BUGFIX] Fix uninstall ( thanks misc) (Bug #22642)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.0-1mdv2008.1
+ Revision: 128068
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import superkaramba-theme-cynapses


* Sun Mar 06 2005 Sebastien Savarin <plouf@mandriva.org> 2.0-1mdk
-First Mandriva Linux

