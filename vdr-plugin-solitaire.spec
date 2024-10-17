%define plugin	solitaire

Summary:	VDR plugin: The well-known card game
Name:		vdr-plugin-%plugin
Version:	0.0.2
Release:	21
Group:		Video
License:	GPL
URL:		https://www.djdagobert.com/vdr/solitaire/
Source:		http://www.djdagobert.com/vdr/solitaire/vdr-%plugin-%{version}.tgz
Patch0:		vdr-cardgames-0.0.2-to-gcc3.4.diff
Patch1:		91_solitaire-0.0.2-1.5.4.dpatch
Patch2:		solitaire-0.0.2-i18n-1.6.patch
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

cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
install -m644 solitaire/* %{buildroot}%{vdr_plugin_datadir}/%{plugin}
ln -s %{vdr_plugin_datadir}/%{plugin} 	%{buildroot}%{vdr_plugin_cfgdir}/solitaire

%files -f %plugin/%plugin.vdr
%doc %plugin/README %plugin/HISTORY %plugin/CONTRIBUTORS
%{vdr_plugin_cfgdir}/solitaire
%{vdr_plugin_datadir}/%{plugin}
