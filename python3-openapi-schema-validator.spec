#
# Conditional build:
%bcond_without	tests	# unit+integration tests

Summary:	OpenAPI schema validation for Python
Summary(pl.UTF-8):	Sprawdzanie poprawności schematów OpenAPI dla Pythona
Name:		python3-openapi-schema-validator
Version:	0.9.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/openapi-schema-validator/
Source0:	https://files.pythonhosted.org/packages/source/o/openapi-schema-validator/openapi_schema_validator-%{version}.tar.gz
# Source0-md5:	d4282d07d496dc307335f23d1a3854ee
URL:		https://pypi.org/project/openapi-schema-validator/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-poetry-core >= 1.0.0
%if %{with tests}
BuildRequires:	python3-jsonschema >= 4.19.1
BuildRequires:	python3-jsonschema-specifications >= 2024.10.1
BuildRequires:	python3-pydantic >= 2.0.0
BuildRequires:	python3-pydantic-settings >= 2.0.0
BuildRequires:	python3-pytest >= 9
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-referencing >= 0.37.0
BuildRequires:	python3-rfc3339_validator
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
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

%prep
%setup -q -n openapi_schema_validator-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/openapi_schema_validator
%{py3_sitescriptdir}/openapi_schema_validator-%{version}.dist-info
