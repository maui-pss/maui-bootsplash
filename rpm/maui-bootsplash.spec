Name:       maui-bootsplash
Summary:    Maui Boot Splash
Version:    1
Release:    1
Group:      System/Base
License:    LGPLv2.1+
URL:        https://github.com/mauios/msplash
Source0:    %{name}-%{version}.tar.xz

Requires:   systemd >= 187
Requires:   qt5-qtdeclarative-qmlscene
Requires:   maui-bootsplash-theme

%description
Boot splash.


%prep
%setup -q -n %{name}-%{version}


%install
# Prepare directories
mkdir -p %{buildroot}/lib/systemd/system/basic.target.wants/
mkdir -p %{buildroot}/lib/systemd/system/

# Services
install -m 0644 services/maui-bootsplash.service %{buildroot}/lib/systemd/system/

# Link services
ln -sf ../maui-bootsplash.service %{buildroot}/lib/systemd/system/basic.target.wants/


%files
%defattr(-,root,root,-)
/lib/systemd/system/*
/lib/systemd/system/basic.target.wants/*
