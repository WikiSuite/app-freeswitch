
Name: app-freeswitch
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: FreeSWITCH
License: GPLv3
Group: ClearOS/Apps
Packager: eGloo
Vendor: WikiSuite
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base

%description
FreeSWITCH - a description goes here.

%package core
Summary: FreeSWITCH - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-users-core >= 1:2.3.23
Requires: app-groups-core
Requires: app-network-core
Requires: freeswitch-config-vanilla

%description core
FreeSWITCH - a description goes here.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/freeswitch
cp -r * %{buildroot}/usr/clearos/apps/freeswitch/

install -d -m 0755 %{buildroot}/var/clearos/freeswitch
install -d -m 0755 %{buildroot}/var/clearos/freeswitch/backup
install -D -m 0644 packaging/freeswitch.php %{buildroot}/var/clearos/base/daemon/freeswitch.php

%post
logger -p local6.notice -t installer 'app-freeswitch - installing'

%post core
logger -p local6.notice -t installer 'app-freeswitch-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/freeswitch/deploy/install ] && /usr/clearos/apps/freeswitch/deploy/install
fi

[ -x /usr/clearos/apps/freeswitch/deploy/upgrade ] && /usr/clearos/apps/freeswitch/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-freeswitch - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-freeswitch-core - uninstalling'
    [ -x /usr/clearos/apps/freeswitch/deploy/uninstall ] && /usr/clearos/apps/freeswitch/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/freeswitch/controllers
/usr/clearos/apps/freeswitch/htdocs
/usr/clearos/apps/freeswitch/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/freeswitch/packaging
%exclude /usr/clearos/apps/freeswitch/unify.json
%dir /usr/clearos/apps/freeswitch
%dir /var/clearos/freeswitch
%dir /var/clearos/freeswitch/backup
/usr/clearos/apps/freeswitch/deploy
/usr/clearos/apps/freeswitch/language
/usr/clearos/apps/freeswitch/libraries
/var/clearos/base/daemon/freeswitch.php
