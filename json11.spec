%global debug_package   %{nil}

Name: json11
Version: 1.0.0
Release: 1%{?dist}

Summary: A tiny JSON library for C++11
License: MIT
URL: https://github.com/nlohmann/%{name}
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

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/%{name}.hpp
%{_libdir}/pkgconfig/%{name}.pc

%changelog
