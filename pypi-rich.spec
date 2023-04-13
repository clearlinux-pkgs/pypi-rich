#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-rich
Version  : 13.3.4
Release  : 84
URL      : https://files.pythonhosted.org/packages/31/3b/2360352760b436f822258396e66ffb6d42585518a9cde2f93f142e64c5eb/rich-13.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/3b/2360352760b436f822258396e66ffb6d42585518a9cde2f93f142e64c5eb/rich-13.3.4.tar.gz
Summary  : Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
Group    : Development/Tools
License  : MIT
Requires: pypi-rich-license = %{version}-%{release}
Requires: pypi-rich-python = %{version}-%{release}
Requires: pypi-rich-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/13.2.0)](https://pypi.org/project/rich/) [![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)

%package license
Summary: license components for the pypi-rich package.
Group: Default

%description license
license components for the pypi-rich package.


%package python
Summary: python components for the pypi-rich package.
Group: Default
Requires: pypi-rich-python3 = %{version}-%{release}

%description python
python components for the pypi-rich package.


%package python3
Summary: python3 components for the pypi-rich package.
Group: Default
Requires: python3-core
Provides: pypi(rich)
Requires: pypi(markdown_it_py)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-rich package.


%prep
%setup -q -n rich-13.3.4
cd %{_builddir}/rich-13.3.4
pushd ..
cp -a rich-13.3.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681405818
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rich
cp %{_builddir}/rich-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rich/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-rich/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
