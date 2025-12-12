%define module matplotlib-inline
Name:           python-matplotlib-inline
Version:        0.1.6
Release:        3
Summary:        Inline Matplotlib backend for Jupyter
Group:          Development/Python
License:        BSD
URL:            https://github.com/ipython/matplotlib-inline
Source0:        https://pypi.python.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(wheel)

%description
Inline Matplotlib backend for Jupyter

%prep
%autosetup -n %{module}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{python_sitelib}/matplotlib_inline-%{version}-py*.*.egg-info
%{python_sitelib}/matplotlib_inline/__init__.py
%{python_sitelib}/matplotlib_inline/backend_inline.py
%{python_sitelib}/matplotlib_inline/config.py
