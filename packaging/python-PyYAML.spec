Name:           python-PyYAML
Version:        3.10
Release:        0
Url:            http://pyyaml.org/wiki/PyYAML
Summary:        YAML parser and emitter for Python
License:        MIT
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/P/PyYAML/PyYAML-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-nose
Provides:       python-yaml = %{version}
Obsoletes:      python-yaml < %{version}

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages.  PyYAML is a YAML parser
and emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%prep
%setup -q -n PyYAML-%{version}

%build
CFLAGS="%{optflags}" python setup.py build
find examples -type f | xargs chmod -x # Fix example permissions

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python setup.py test

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitearch}/*

%changelog
