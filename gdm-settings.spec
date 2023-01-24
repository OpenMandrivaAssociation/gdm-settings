Name:      gdm-settings
Version:   2.0
Release:   2
Group:     Graphical desktop/GNOME
Summary:   A settings app for Gnome Login Manager (GDM)
License:   AGPLv3+
Url:       https://github.com/realmazharhussain/gdm-settings
Source0:   https://github.com/realmazharhussain/gdm-settings/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  python-blueprint-compiler
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires: gdm
Requires: polkit
Requires: gettext
Requires: %{_lib}adwaita1_0

BuildArch: noarch

%description
A tool for customizing GNOME Display Manager.

With User Login Manager you can:
* Import user/session settings (currently not working on Flatpak)
* Change Background/Wallpaper (Image/Color)
* Apply themes
* Font Settings 
* Top Bar Settings 
* Display settings 

%files -f %{name}.lang
%doc README.md LICENSE
%{_bindir}/gdm-settings
%{_datadir}/gdm-settings
%{py3_puresitedir}/gdm_settings
%{_appdatadir}/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/dbus-1/services/*.service
#-------------------------------------------------------
%prep
%autosetup


%build
%meson --buildtype=release
%meson_build


%install
%meson_install
# remove use of /usr/bin/env
sed -i -e 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/g' \
    %{buildroot}%{_bindir}/gdm-settings


%find_lang %{name}


%check
meson test -C noarch-rosa-linux-gnu --print-errorlogs
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
