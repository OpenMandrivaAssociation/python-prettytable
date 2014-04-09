%define module prettytable
Name:           python-prettytable
Version:        0.7.2
Release:        1
Summary:        Python library for displaying data in ASCII table format

License:        BSD
Group:          Development/Python
URL:            http://code.google.com/p/prettytable/
Source0:        http://pypi.python.org/packages/source/P/PrettyTable/prettytable-%{version}.tar.gz
BuildRequires:  python-devel
Buildrequires:	python-setuptools
BuildArch:      noarch

%description
PrettyTable is a simple Python library designed to make
 it quick and easy to represent tabular data in visually
appealing ASCII tables. It was inspired by the ASCII
tables used in the PostgreSQL shell psql. PrettyTable
allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified
or centred) and printing of "sub-tables" by specifying a
row range.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root %{buildroot} --install-purelib=%{py_puresitedir}

%clean

%files
%{py_puresitedir}/*




