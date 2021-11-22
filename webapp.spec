Name:           webapp
Version:	1.0        
Release:        1%{?dist}
Summary:        Simple web application

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz 

Requires:       python    
Requires:       python-flask


%description    
Simple web application implemeted in python using Flask


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/%{_bindir}
#touch %{buildroot}/%{_bindir}/%{name}
cat << EOF > %{buildroot}/%{_bindir}/%{name}
!/bin/bash
/usr/bin/python /opt/%{name}/%{name}.py
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}
install -m 0644 %{name}.py %{buildroot}/opt/%{name}/

%files
%license LICENSE
%dir /opt/%{name}/
%{_bindir}/%{name}
/opt/%{name}/%{name}.py*


%changelog
* Mon Nov 22 2021 Test User
- First webapp package

