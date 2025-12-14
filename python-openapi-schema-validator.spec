#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-openapi-schema-validator.spec)

Summary:	OpenAPI schema validation for Python
Summary(pl.UTF-8):	Sprawdzanie poprawności schematów OpenAPI dla Pythona
Name:		python-openapi-schema-validator
# keep 0.1.x here for python2 support
Version:	0.1.6
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/openapi-schema-validator/
Source0:	https://files.pythonhosted.org/packages/source/o/openapi-schema-validator/openapi-schema-validator-%{version}.tar.gz
# Source0-md5:	f0b1727a04bdc820c83d2074d0363a5e
URL:		https://pypi.org/project/openapi-schema-validator/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Openapi-schema-validator is a Python library that validates schema
against the OpenAPI Schema Specification v3.0, which is an extended
subset of the JSON Schema Specification Wright Draft 00
<http://json-schema.org/>.

%description -l pl.UTF-8
Openapi-schema-validator to biblioteka Pythona sprawdzająca poprawność
schematu względem specyfikacji OpenAPI Schema Specification v3.0,
będącej rozszerzonym podzbiorem specyfikacji JSON Schema Specification
Wright Draft 00 <http://json-schema.org/>.

%package -n python3-openapi-schema-validator
Summary:	OpenAPI schema validation for Python
Summary(pl.UTF-8):	Sprawdzanie poprawności schematów OpenAPI dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-openapi-schema-validator
Openapi-schema-validator is a Python library that validates schema
against the OpenAPI Schema Specification v3.0, which is an extended
subset of the JSON Schema Specification Wright Draft 00
<http://json-schema.org/>.

%description -n python3-openapi-schema-validator -l pl.UTF-8
Openapi-schema-validator to biblioteka Pythona sprawdzająca poprawność
schematu względem specyfikacji OpenAPI Schema Specification v3.0,
będącej rozszerzonym podzbiorem specyfikacji JSON Schema Specification
Wright Draft 00 <http://json-schema.org/>.

%package apidocs
Summary:	API documentation for Python openapi-schema-validator module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona openapi-schema-validator
Group:		Documentation

%description apidocs
API documentation for Python openapi-schema-validator module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona openapi-schema-validator.

%prep
%setup -q -n openapi-schema-validator-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/openapi_schema_validator
%{py_sitescriptdir}/openapi_schema_validator-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-openapi-schema-validator
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/openapi_schema_validator
%{py3_sitescriptdir}/openapi_schema_validator-%{version}-py*.egg-info
%endif
