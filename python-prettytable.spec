%define module prettytable
Name:           python-prettytable
Version:        0.5
Release:        %mkrel 1
Summary:        Python library for displaying data in ASCII table format
License:        BSD
Group:          Development/Python
URL:            http://code.google.com/p/prettytable/
Source0:        http://pypi.python.org/packages/source/P/PrettyTable/prettytable-%{version}.tar.gz
BuildRequires:  python-devel
Buildrequires:	python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.5-1mdv2011.0
+ Revision: 683262
- import python-prettytable


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.5
- first release for Mandriva 

