Summary:	Python Linux HPI library
Summary(pl.UTF-8):	Biblioteka Linux HPI dla Pythona
Name:		python-hpi
# keep 4.20.42 here for python2 support
Version:	4.20.42
Release:	1
License:	GPL v2
Group:		Libraries/Python
#Source0Download: https://www.audioscience.com/internet/download/linux_drivers.htm
Source0:	https://www.audioscience.com/internet/download/drivers/released/v4/20/42/hpklinux_%{version}.tar.gz
# Source0-md5:	5d937b0c151332dc8f345a4b59ec7def
URL:		https://www.audioscience.com/internet/download/linux_drivers.htm
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
Requires:	hpklinux-libs >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Linux HPI library.

%description -l pl.UTF-8
Biblioteka Linux HPI dla Pythona.

%prep
%setup -q -n hpklinux_%{version}

%build
cd asi-python
%py_build

%install
rm -rf $RPM_BUILD_ROOT

cd asi-python
%py_install

%py_postclean

# packaged in python3-hpi
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{dab_data,dabtest,hpicontrol,hpimixer,hpisave}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/audioscience
%{py_sitescriptdir}/hpi-2.0-py*.egg-info
