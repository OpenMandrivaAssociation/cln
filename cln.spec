%define major 6
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	C++ Class Library for Numbers
Name:		cln
Version:	1.3.2
Release:	4
License:	GPLv2+
Group:		Sciences/Mathematics
URL:		http://www.ginac.de/CLN/
Source0:	http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2
BuildRequires:	gmp-devel

%description
CLN is a collection of C++ math classes and functions licensed under
the GPL that provides efficiency, type safety, and algebraic syntax in
a fast, memory-efficient library.

%package -n	%{libname}
Summary:	C++ Class Library for Numbers
Group:		Sciences/Mathematics
Provides:	%{name} = %{version}-%{release}
Provides:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname cln 4} < 1.2.2

%description -n	%{libname}
CLN is a collection of C++ math classes and functions licensed under
the GPL that provides efficiency, type safety, and algebraic syntax in
a fast, memory-efficient library.

%package -n	%{develname}
Summary:	Development files for programs using the CLN library
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{develname} = %{version}-%{release}
Obsoletes:	%{mklibname cln 4 -d} < 1.2.2

%description -n %{develname}
This package is necessary if you wish to develop software that uses
the CLN library.

%prep
%setup -q

%build
%configure2_5x --disable-static
%ifarch %arm
%make CPPFLAGS="-DNO_ASM"
%else
%make
%endif

%check
%make check

%install
%makeinstall_std

# prepare documents
%__rm -rf documents
%__mkdir documents
cp -p examples/*.cc documents/

%__rm -rf %{buildroot}%{_datadir}/dvi

%__rm -rf %{buildroot}%{_bindir}
%__rm -rf %{buildroot}%{_mandir}
%__rm -rf %{buildroot}%{_datadir}/aclocal

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog NEWS README TODO* documents/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_infodir}/*.info*


%changelog
* Thu Jun 14 2012 Andrey Bondrov <abondrov@mandriva.org> 1.3.2-3
+ Revision: 805557
- Drop some legacy junk

* Wed Dec 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3.2-2
+ Revision: 738697
- Rebuild for .la file removal.

* Mon May 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-1
+ Revision: 674980
- update to new version 1.3.2
- fix url for Source0

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3
+ Revision: 663696
- --parents/-p
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2mdv2011.0
+ Revision: 603838
- rebuild

* Sun Sep 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 449845
- update to new version 1.3.1

* Fri Sep 25 2009 Olivier Blin <blino@mandriva.org> 1.3.0-2mdv2010.0
+ Revision: 448831
- disable assembly on arm, it doesn't even compile
  (from Arnaud Patard)

* Mon Aug 03 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.0-1mdv2010.0
+ Revision: 407679
- drop patch 0

  + Christophe Fergeau <cfergeau@mandriva.com>
    - add patch from fedora (upstreamed) to fix build with gcc 4.4

* Mon Feb 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-4mdv2009.1
+ Revision: 340711
- obsolete old library

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-3mdv2009.1
+ Revision: 324379
- obsolete old library
- protect major in file list

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-2mdv2009.0
+ Revision: 264355
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-1mdv2009.0
+ Revision: 195299
- new version
- new license policy

* Mon Jan 28 2008 Lev Givon <lev@mandriva.org> 1.2.0-1mdv2008.1
+ Revision: 159472
- Update to 1.2.0.
  Make devel package conform to new naming policy.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.1.13-2mdv2008.0
+ Revision: 70156
- kill file require on info-install


* Mon Jan 22 2007 Lenny Cartier <lenny@mandriva.com> 1.1.13-1mdv2007.0
+ Revision: 111741
- Update to 1.1.13
- Import cln

* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 1.1.11-2mdv2007.0
- rebuild

* Fri Mar 17 2006 Lenny Cartier <lenny@mandriva.com> 1.1.11-1mdk
- 1.1.11

* Tue Nov 29 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.1.10-2mdk
- bump lib major

* Sat Nov 05 2005 David Walluck <walluck@mandriva.org> 1.1.10-1mdk
- 1.1.10

* Sat Sep 03 2005 David Walluck <walluck@mandriva.org> 1.1.9-3mdk
- patch for gcc4
- don't use PreReq

* Fri May 06 2005 Olivier Thauvin <nanardon@mandriva.org> 1.1.9-2mdk
- multiarch

* Mon Dec 27 2004 Abel Cheung <deaddog@mandrake.org> 1.1.9-1mdk
- New version
- Change group, avoid dumping everything into kitchen sink

* Wed Jul 28 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.8-1mdk
- 1.1.8

* Tue Jun 22 2004 Abel Cheung <deaddog@deaddog.org> 1.1.7-2mdk
- fix macros
- fix dep
- fix major

* Sun Jun 06 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.7-1mdk
- 1.1.7
- use %%mklibname
- update url
- cosmetics

