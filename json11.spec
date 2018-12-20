Name: json11
Version: 1.0.0
Release: 1%{?dist}

Summary: A tiny JSON library for C++11
License: MIT
URL: https://github.com/dropbox/%{name}
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Json11 is a tiny JSON library for C++11, providing JSON parsing
and serialization.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
mkdir -p %{_target_platform}
sed -i 's@lib/@%{_libdir}/@g' CMakeLists.txt
echo "set_property(TARGET json11 PROPERTY SOVERSION 0)" >> CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/lib%{name}.so.0

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.hpp
%{_libdir}/pkgconfig/%{name}.pc

%changelog
