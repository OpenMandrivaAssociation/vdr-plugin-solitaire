
%define plugin	solitaire
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	17

Summary:	VDR plugin: The well-known card game
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.djdagobert.com/vdr/solitaire/
Source:		http://www.djdagobert.com/vdr/solitaire/vdr-%plugin-%version.tar.bz2
Patch0:		vdr-cardgames-0.0.2-to-gcc3.4.diff
Patch1:		91_solitaire-0.0.2-1.5.4.dpatch
Patch2:		solitaire-0.0.2-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	dos2unix
Requires:	vdr-abi = %vdr_abi

%description
This solitaire plugin is an implementation of the (well-known) card game
"Solitaire" played on the On Screen Display of your Video Disk Recorder.

%prep
%setup -q -c
cd %plugin
dos2unix tools/list.h
%patch0 -p1 -b .gcc34
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

chmod 0644 CONTRIBUTORS HISTORY README

%build
cd %plugin
%vdr_plugin_build

%install
rm -rf %{buildroot}

cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
install -m644 solitaire/* %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
ln -s %{_vdr_plugin_datadir}/%{plugin} 	%{buildroot}%{_vdr_plugin_cfgdir}/solitaire

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin/%plugin.vdr
%defattr(-,root,root)
%doc %plugin/README %plugin/HISTORY %plugin/CONTRIBUTORS
%{_vdr_plugin_cfgdir}/solitaire
%{_vdr_plugin_datadir}/%{plugin}




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-17mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-16mdv2009.1
+ Revision: 359368
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-15mdv2009.0
+ Revision: 197981
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-14mdv2009.0
+ Revision: 197725
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.4 (P2 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-13mdv2008.1
+ Revision: 145204
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-12mdv2008.1
+ Revision: 103214
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-11mdv2008.0
+ Revision: 50048
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-10mdv2008.0
+ Revision: 42131
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-9mdv2008.0
+ Revision: 22695
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-8mdv2007.0
+ Revision: 90973
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-7mdv2007.1
+ Revision: 74084
- rebuild for new vdr
- Import vdr-plugin-solitaire

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2007.0
- use _ prefix for system path macros

* Tue Jun 06 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
- initial Mandriva release

