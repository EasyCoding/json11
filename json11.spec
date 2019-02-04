Name: json11
Version: 1.0.0
Release: 2%{?dist}

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
sed -i 's@lib/@%{_lib}/@g' CMakeLists.txt
sed -i 's@lib/@%{_lib}/@g' json11.pc.in
echo "set_property(TARGET json11 PROPERTY SOVERSION 0)" >> CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DJSON11_BUILD_TESTS=ON \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

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
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial SPEC release.
