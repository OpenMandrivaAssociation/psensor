%define _disable_ld_no_undefined 1
%define _disable_lto 1

Name:		psensor
Version:	1.2.1
Release:	1
Summary:	Graphical Temperature Monitor for CPU and GPU
License:	GPLv2+
Group:		Monitoring
URL:		http://wpitchoune.net/psensor
Source0:	http://wpitchoune.net/psensor/files/%{name}-%{version}.tar.gz

BuildRequires:	cppcheck
BuildRequires:	help2man
BuildRequires:	lm_sensors-devel
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmicrohttpd)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(udisks2)

Requires:	hddtemp
Requires:	lm_sensors

%description
Psensor is a graphical hardware temperature monitor for Linux.
It can monitor:
* the temperature of the motherboard and CPU sensors (using lm-sensors).
* the temperature of the NVidia GPUs (using XNVCtrl).
* the temperature of ATI/AMD GPUs (not enabled in Ubuntu PPAs or official
  distribution repositories, see the instructions for enabling its support).
* the temperature of the Hard Disk Drives (using hddtemp or libatasmart).
* the rotation speed of the fans (using lm-sensors).
* the CPU usage (since 0.6.2.10 and using Gtop2).

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_docdir}/%{name}/
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/psensor.gschema.xml
%{_iconsdir}/*/*/*/%{name}*
%{_mandir}/man1/%{name}*.1.*
%exclude %{_docdir}/%{name}/INSTALL
