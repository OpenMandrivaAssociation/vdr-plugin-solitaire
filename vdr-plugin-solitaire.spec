
%define plugin	solitaire
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	12

Summary:	VDR plugin: The well-known card game
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.djdagobert.com/vdr/solitaire/
Source:		http://www.djdagobert.com/vdr/solitaire/vdr-%plugin-%version.tar.bz2
Patch0:		vdr-cardgames-0.0.2-to-gcc3.4.diff
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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


