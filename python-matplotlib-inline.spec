%define module matplotlib_inline

Name:		python-matplotlib-inline
Version:	0.2.1
Release:	1
Summary:	Inline Matplotlib backend for Jupyter
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/ipython/matplotlib-inline
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Inline Matplotlib backend for Jupyter.

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
