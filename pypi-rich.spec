#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-rich
Version  : 11.0.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/eb/be/bd5d6c37f5de55f31cb9432e0d926ceeab1b2ee774bd696557b53bc15012/rich-11.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/eb/be/bd5d6c37f5de55f31cb9432e0d926ceeab1b2ee774bd696557b53bc15012/rich-11.0.0.tar.gz
Summary  : Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
Group    : Development/Tools
License  : MIT
Requires: pypi-rich-license = %{version}-%{release}
Requires: pypi-rich-python = %{version}-%{release}
Requires: pypi-rich-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://pypi.org/project/rich/) [![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)

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
Requires: pypi(colorama)
Requires: pypi(commonmark)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-rich package.


%prep
%setup -q -n rich-11.0.0
cd %{_builddir}/rich-11.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641942505
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rich
cp %{_builddir}/rich-11.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rich/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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