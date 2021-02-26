Name: python-prettytable
Version: 2.0.0
Release: 1
Source0: https://files.pythonhosted.org/packages/source/p/prettytable/prettytable-%{version}.tar.gz
Summary: Python library for displaying tabular data in an ASCII table format
URL: https://pypi.org/project/prettytable/
License: Apache 2.0
Group: System/Libraries
BuildArch: noarch
BuildRequires: python python-setuptools

%description
A simple Python library for easily displaying tabular data in a visually
appealing ASCII table format

%prep
%autosetup -p1 -n prettytable-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/prettytable
%{py_puresitedir}/*.egg-info
