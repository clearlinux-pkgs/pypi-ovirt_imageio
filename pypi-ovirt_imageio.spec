#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ovirt_imageio
Version  : 2.4.6
Release  : 4
URL      : https://files.pythonhosted.org/packages/f3/71/7952dc960510624ec69d166130149af324496027dd2b5dece3caaa8aa2e5/ovirt-imageio-2.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/f3/71/7952dc960510624ec69d166130149af324496027dd2b5dece3caaa8aa2e5/ovirt-imageio-2.4.6.tar.gz
Summary  : Transfer disk images on oVirt system
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pypi-ovirt_imageio-bin = %{version}-%{release}
Requires: pypi-ovirt_imageio-filemap = %{version}-%{release}
Requires: pypi-ovirt_imageio-lib = %{version}-%{release}
Requires: pypi-ovirt_imageio-license = %{version}-%{release}
Requires: pypi-ovirt_imageio-python = %{version}-%{release}
Requires: pypi-ovirt_imageio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# An example for an ovirt-imageio configuration file.
# Below is a list of available options which can be configured.
# imageio supports drop-in configuration, which means there can
# be multiple config files, which are all read in succession to get
# final configuration.
# imageio searches the following directories for config files:
# - /etc/ovirt-imageio/conf.d/ where admins should place their configs.
#   Also oVirt engine-setup writes there a config file.
# - /usr/lib/ovirt-imageio/conf.d/ where vendor configs should be placed.
# Config files have to be in the directories listed above and must have *.conf
# suffix. Files are read in alphabetical order, taking into account only
# base name of the config file, not directory name. E.g. if there are two
# config files, 50-vdsm.conf and 99-admin.conf (see conf.d listing below),
# config options specified in 99-admin.conf will overwrite corresponding
# config options in 50-vdsm.conf.
#     $ tree /etc/ovirt-imageio/conf.d/
#       /etc/ovirt-imageio/conf.d/
#       ├── 50-vdsm.conf
#       └── 99-admin.conf
# You can check the final configuration by executing
#     ovirt-imageio --show-config

%package bin
Summary: bin components for the pypi-ovirt_imageio package.
Group: Binaries
Requires: pypi-ovirt_imageio-license = %{version}-%{release}
Requires: pypi-ovirt_imageio-filemap = %{version}-%{release}

%description bin
bin components for the pypi-ovirt_imageio package.


%package filemap
Summary: filemap components for the pypi-ovirt_imageio package.
Group: Default

%description filemap
filemap components for the pypi-ovirt_imageio package.


%package lib
Summary: lib components for the pypi-ovirt_imageio package.
Group: Libraries
Requires: pypi-ovirt_imageio-license = %{version}-%{release}
Requires: pypi-ovirt_imageio-filemap = %{version}-%{release}

%description lib
lib components for the pypi-ovirt_imageio package.


%package license
Summary: license components for the pypi-ovirt_imageio package.
Group: Default

%description license
license components for the pypi-ovirt_imageio package.


%package python
Summary: python components for the pypi-ovirt_imageio package.
Group: Default
Requires: pypi-ovirt_imageio-python3 = %{version}-%{release}

%description python
python components for the pypi-ovirt_imageio package.


%package python3
Summary: python3 components for the pypi-ovirt_imageio package.
Group: Default
Requires: pypi-ovirt_imageio-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(ovirt_imageio)

%description python3
python3 components for the pypi-ovirt_imageio package.


%prep
%setup -q -n ovirt-imageio-2.4.6
cd %{_builddir}/ovirt-imageio-2.4.6
pushd ..
cp -a ovirt-imageio-2.4.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660145305
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ovirt_imageio
cp %{_builddir}/ovirt-imageio-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-ovirt_imageio/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ovirt-imageio
/usr/bin/ovirt-imageioctl
/usr/bin/ovirt-img

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-ovirt_imageio

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ovirt_imageio/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
