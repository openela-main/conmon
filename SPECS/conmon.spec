%global with_check 0

%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0

# https://github.com/containers/conmon
%global import_path github.com/containers/%{name}
%global git0 https://%{import_path}
%global commit0 158b5421dbac6bda96b1457955cf2e3c34af29bc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: conmon
Epoch: 3
Version: 2.1.6
Release: 1%{?dist}
Summary: OCI container runtime monitor
License: ASL 2.0
URL: %{git0}
%if 0%{?branch:1}
Source0: https://%{import_path}/tarball/%{commit0}/%{branch}-%{shortcommit0}.tar.gz
%else
Source0: https://%{import_path}/archive/%{commit0}/%{name}-%{version}-%{shortcommit0}.tar.gz
%endif
# https://fedoraproject.org/wiki/PackagingDrafts/Go#Go_Language_Architectures
#ExclusiveArch: %%{go_arches}
# still use arch exclude as the macro above still refers %%{ix86} in RHEL8.4:
# https://bugzilla.redhat.com/show_bug.cgi?id=1905383
ExcludeArch: %{ix86}
BuildRequires: gcc
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: systemd-devel
BuildRequires: golang >= 1.17.7
BuildRequires: /usr/bin/go-md2man
BuildRequires: libseccomp-devel

%description
%{summary}.

%prep
%if 0%{?branch:1}
%autosetup -Sgit -n containers-%{name}-%{shortcommit0}
%else
%autosetup -Sgit -n %{name}-%{commit0}
%endif

%build
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%{__make} all

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man8/*

%changelog
* Tue Feb 07 2023 Jindrich Novy <jnovy@redhat.com> - 3:2.1.6-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.6
- Related: #2123641

* Mon Nov 07 2022 Jindrich Novy <jnovy@redhat.com> - 3:2.1.5-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.5
- Related: #2123641

* Tue Aug 30 2022 Jindrich Novy <jnovy@redhat.com> - 3:2.1.4-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.4
- Related: #2061390

* Fri Aug 26 2022 Jindrich Novy <jnovy@redhat.com> - 3:2.1.2-2
- revert conmon to 2.1.2
- Related: #2061390

* Tue Jul 26 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.3-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.3
- Related: #2061390

* Thu Jun 16 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.2-2
- update to latest content of https://github.com/containers/conmon/releases/tag/2.1.2
  (https://github.com/containers/conmon/commit/2bc95ee697e87d5f7b77063cf83fc32739addafe)
- Related: #2061390

* Wed Jun 15 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.2-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.2
- Related: #2061390

* Mon Jun 06 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.1-2
- fix CVE-2022-1708 - thanks to Peter Hunt
- Related: #2061390

* Tue May 24 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.1-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.1
- Related: #2061390

* Wed May 11 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.0-3
- BuildRequires: /usr/bin/go-md2man
- Related: #2061390

* Fri Apr 08 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.0-2
- bump golang BR to 1.17.7
- Related: #2061390

* Tue Jan 25 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.1.0-1
- update to https://github.com/containers/conmon/releases/tag/v2.1.0
- Related: #2001445

* Wed Jan 12 2022 Jindrich Novy <jnovy@redhat.com> - 2:2.0.32-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.32
- Related: #2001445

* Wed Dec 08 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.31-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.31
- Related: #2001445

* Thu Sep 23 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.30-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.30
- Related: #2001445

* Thu Jun 03 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.29-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.29
- Related: #1934415

* Thu Jun 03 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.27-6
- update to the latest content of https://github.com/containers/conmon/tree/master
  (https://github.com/containers/conmon/commit/75e067e)
- Related: #1934415

* Wed Jun 02 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.27-5
- update to the latest content of https://github.com/containers/conmon/tree/master
  (https://github.com/containers/conmon/commit/b033cb5)
- Related: #1934415

* Mon May 17 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.27-4
- update to the latest content of https://github.com/containers/conmon/tree/master
  (https://github.com/containers/conmon/commit/3161452)
- Related: #1934415

* Mon May 10 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.27-3
- upload new source tarball
- Related: #1934415

* Mon May 10 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.27-2
- switch to master branch to fix /dev/null ownership issues
  (https://github.com/containers/conmon/commit/372fa19211cfeabdb2bad52a4ab8a4d1b0b0063c)
- Related: #1934415

* Tue Mar 09 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.27-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.27
- Related: #1934415

* Thu Feb 04 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.26-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.26
- Related: #1883490

* Thu Jan 21 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.25-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.25
- Related: #1883490

* Fri Jan 15 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.24-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.24
- Related: #1883490

* Mon Jan 04 2021 Jindrich Novy <jnovy@redhat.com> - 2:2.0.22-3
- exclude i686 as golang is not suppoerted there
- Related: #1883490

* Sat Dec 26 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.22-2
- add BR: golang, go-md2man
- add man pages
- Related: #1883490

* Mon Dec 21 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.22-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.22
- Related: #1883490

* Tue Dec 08 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.21-3
- simplify spec
- Related: #1883490

* Mon Nov 09 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.21-2
- be sure to harden the linked binary
- compile with debuginfo enabled
- Related: #1883490

* Wed Oct 21 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.21-1
- synchronize with stream-container-tools-rhel8
- Related: #1883490

* Tue Aug 11 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.20-2
- use proper CFLAGS
- Related: #1821193

* Wed Jul 29 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.20-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.20
- Related: #1821193

* Wed Jul 15 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.19-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.19
- Related: #1821193

* Tue Jun 16 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.18-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.18
- Related: #1821193

* Tue May 26 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.17-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.17
- Related: #1821193

* Wed May 13 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.16-1
- update to https://github.com/containers/conmon/releases/tag/v2.0.16
- Related: #1821193

* Tue May 12 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.15-2
- synchronize containter-tools 8.3.0 with 8.2.1
- Related: #1821193

* Mon Apr 06 2020 Jindrich Novy <jnovy@redhat.com> - 2:2.0.15-1
- update to 2.0.15
- Related: #1821193

* Wed Dec 11 2019 Jindrich Novy <jnovy@redhat.com> - 2:2.0.6-1
- update to 2.0.6
- Related: RHELPLAN-25139

* Tue Dec 10 2019 Jindrich Novy <jnovy@redhat.com> - 2:2.0.5-1
- update to 2.0.5
- Related: RHELPLAN-25139

* Mon Dec 09 2019 Jindrich Novy <jnovy@redhat.com> - 2:2.0.4-1
- update to 2.0.4 bugfix release
- Related: RHELPLAN-25139

* Mon Nov 25 2019 Jindrich Novy <jnovy@redhat.com> - 2:2.0.3-2.giteb5fa88
- BR: systemd-devel
- Related: RHELPLAN-25139

* Wed Nov 20 2019 Jindrich Novy <jnovy@redhat.com> - 2:2.0.3-1.giteb5fa88
- update to 2.0.3
- Related: RHELPLAN-25139

* Wed Sep 25 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.2-0.1.dev.git422ce21
- build latest upstream master

* Tue Sep 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.0-2
- remove BR: go-md2man since no manpages yet

* Tue Sep 10 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.0.0-1
- bump to v2.0.0

* Fri May 31 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:0.2.0-1
- initial package
