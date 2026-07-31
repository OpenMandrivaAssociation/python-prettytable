Name: python-prettytable
Version: 3.18.0
Release: 1
Source0: https://files.pythonhosted.org/packages/source/p/prettytable/prettytable-%{version}.tar.gz
Summary: Python library for displaying tabular data in an ASCII table format
URL: https://pypi.org/project/prettytable/
License: Apache 2.0
Group: System/Libraries
BuildArch: noarch
BuildSystem: python
BuildRequires: python%{pyver}dist(pip)
BuildRequires: python%{pyver}dist(hatchling)
BuildRequires: python%{pyver}dist(hatch-vcs)
BuildRequires: python%{pyver}dist(wheel)

%description
A simple Python library for easily displaying tabular data in a visually
appealing ASCII table format

%files
%{py_puresitedir}/prettytable
%{py_puresitedir}/prettytable-%{version}.dist-info
