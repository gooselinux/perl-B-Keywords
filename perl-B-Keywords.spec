Name:           perl-B-Keywords
Version:        1.09
Release:        3.1%{?dist}
Summary:        Lists of reserved barewords and symbol names

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/B-Keywords/
Source0:        http://www.cpan.org/authors/id/J/JJ/JJORE/B-Keywords-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
%{summary}.


%prep
%setup -q -n B-Keywords-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorlib}/B/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.09-3.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.09-2
- BR Test -> Test::More

* Sat Mar 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.09-1
- update to 1.09

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 31 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-2
- update buildrequires

* Sat Mar 15 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-1
- update to 1.08

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-4
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-3
- Rebuild for perl 5.10 (again), disable tests for first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-2
- rebuild normally, second pass

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-1.1
- rebuild for new perl
- disable Test-Pod-Coverage, tests for first pass

* Thu Feb 15 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.

* Sat Jan 20 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- First build.
