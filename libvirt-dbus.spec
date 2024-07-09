#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v16
# autospec commit: b858a2a
#
Name     : libvirt-dbus
Version  : 1.4.1
Release  : 2
URL      : https://github.com/libvirt/libvirt-dbus/archive/refs/tags/v1.4.1.tar.gz
Source0  : https://github.com/libvirt/libvirt-dbus/archive/refs/tags/v1.4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libvirt-dbus-bin = %{version}-%{release}
Requires: libvirt-dbus-data = %{version}-%{release}
Requires: libvirt-dbus-license = %{version}-%{release}
Requires: libvirt-dbus-man = %{version}-%{release}
Requires: libvirt-dbus-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dbus-python
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(libvirt)
BuildRequires : pkgconfig(libvirt-glib-1.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : pygobject
BuildRequires : pypi(pytest)
BuildRequires : pypi-docutils
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
============
libvirt-dbus
============
Libvirt provides a portable, long term stable C API for managing the
virtualization technologies provided by many operating systems. It
includes support for QEMU, KVM, Xen, LXC, bhyve, Virtuozzo, VMware
vCenter and ESX, VMware Desktop, Hyper-V, VirtualBox and the POWER
Hypervisor.

%package bin
Summary: bin components for the libvirt-dbus package.
Group: Binaries
Requires: libvirt-dbus-data = %{version}-%{release}
Requires: libvirt-dbus-license = %{version}-%{release}
Requires: libvirt-dbus-services = %{version}-%{release}

%description bin
bin components for the libvirt-dbus package.


%package data
Summary: data components for the libvirt-dbus package.
Group: Data

%description data
data components for the libvirt-dbus package.


%package license
Summary: license components for the libvirt-dbus package.
Group: Default

%description license
license components for the libvirt-dbus package.


%package man
Summary: man components for the libvirt-dbus package.
Group: Default

%description man
man components for the libvirt-dbus package.


%package services
Summary: services components for the libvirt-dbus package.
Group: Systemd services
Requires: systemd

%description services
services components for the libvirt-dbus package.


%prep
%setup -q -n libvirt-dbus-1.4.1
cd %{_builddir}/libvirt-dbus-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720549579
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libvirt-dbus
cp %{_builddir}/libvirt-dbus-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libvirt-dbus/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/*  %{buildroot}/usr/bin
rmdir %{buildroot}/usr/sbin
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libvirt-dbus

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.libvirt.Connect.xml
/usr/share/dbus-1/interfaces/org.libvirt.Domain.xml
/usr/share/dbus-1/interfaces/org.libvirt.DomainSnapshot.xml
/usr/share/dbus-1/interfaces/org.libvirt.Interface.xml
/usr/share/dbus-1/interfaces/org.libvirt.NWFilter.xml
/usr/share/dbus-1/interfaces/org.libvirt.Network.xml
/usr/share/dbus-1/interfaces/org.libvirt.NodeDevice.xml
/usr/share/dbus-1/interfaces/org.libvirt.Secret.xml
/usr/share/dbus-1/interfaces/org.libvirt.StoragePool.xml
/usr/share/dbus-1/interfaces/org.libvirt.StorageVol.xml
/usr/share/dbus-1/services/org.libvirt.service
/usr/share/dbus-1/system-services/org.libvirt.service
/usr/share/dbus-1/system.d/org.libvirt.conf
/usr/share/polkit-1/rules.d/libvirt-dbus.rules

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvirt-dbus/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/libvirt-dbus.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/libvirt-dbus.service
/usr/lib/systemd/user/libvirt-dbus.service
