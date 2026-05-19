%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if %{defined rhel}
%bcond_with docs
%else
%bcond_without docs
%endif

Name: conmon
%if %{defined rhel}
Epoch: 3
%else
Epoch: 2
%endif
Version: 2.2.1
License: Apache-2.0
Release: 2%{?dist}
Summary: OCI container runtime monitor
URL: https://github.com/containers/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/v%{version}.tar.gz
%if %{with docs}
BuildRequires: go-md2man
%endif
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: make
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libseccomp)
Requires: glib2
Requires: systemd-libs
Requires: libseccomp

%description
%{summary}.

%prep
%autosetup -Sgit %{name}-%{version}
sed -i 's/install.bin: bin\/conmon/install.bin:/' Makefile

%build
%make_build bin/conmon

%if %{with docs}
%make_build GOMD2MAN=go-md2man -C docs
%endif

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install.bin

%if %{with docs}
%{__make} PREFIX=%{buildroot}%{_prefix} -C docs install
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%if %{with docs}
%{_mandir}/man8/%{name}.8.gz
%endif

%changelog
* Mon Feb 16 2026 Jindrich Novy <jnovy@redhat.com> - 2:2.2.1-2
- use proper macros in spec file and simplify
- Related: RHEL-111917

* Thu Feb 12 2026 Jindrich Novy <jnovy@redhat.com> - 2:2.2.1-1
- update to https://github.com/containers/conmon/releases/tag/v2.2.1
- enable RELRO
- Related: RHEL-122178

* Tue Feb 03 2026 Jindrich Novy <jnovy@redhat.com> - 2:2.2.0-1
- update to https://github.com/containers/conmon/releases/tag/v2.2.0
- Related: RHEL-122178

* Wed Feb 26 2025 Jindrich Novy <jnovy@redhat.com> - 2:2.1.13-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.13
- Resolves: RHEL-80818

* Fri Jan 17 2025 Jindrich Novy <jnovy@redhat.com> - 3:2.1.12-4
- Fix spec file, remove crio
- Related: RHEL-58990
