%global  kf_version 6.6.0

Name:           kf6-kfilemetadata
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        6.6.0
Release:        0%{?dist}
License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/kfilemetadata
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  libattr-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name
mkdir -p %{buildroot}%{_kf6_plugindir}/kfilemetadata/writers/

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kfilemetadata*
%{_kf6_libdir}/libKF6FileMetaData.so.*
%dir %{_kf6_plugindir}/kfilemetadata/
%{_kf6_plugindir}/kfilemetadata/kfilemetadata_*.so
%dir %{_kf6_plugindir}/kfilemetadata/writers/
%{_kf6_plugindir}/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files devel
%{_kf6_libdir}/libKF6FileMetaData.so
%{_kf6_libdir}/cmake/KF6FileMetaData
%{_kf6_includedir}/KFileMetaData/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
