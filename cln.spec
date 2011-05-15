%define	major 6
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	C++ Class Library for Numbers
Name:		cln
Version:	1.3.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
URL:		http://www.ginac.de/CLN/
Source0:	http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2
BuildRequires:	gmp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	%{mklibname cln 4}
Obsoletes:	%{mklibname cln 5}

%description -n	%{libname}
CLN is a collection of C++ math classes and functions licensed under
the GPL that provides efficiency, type safety, and algebraic syntax in
a fast, memory-efficient library.

%package -n	%{develname}
Summary:	Development files for programs using the CLN library
Group:		Development/C++
Requires(post):	info-install
Requires(preun): info-install
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{develname} = %{version}-%{release}
Obsoletes:	%{mklibname cln 4 -d} < 1.2.2
Provides:	%{mklibname cln 4 -d}

%description -n %{develname}
This package is necessary if you wish to develop software that uses
the CLN library.

%prep
%setup -q

%build
%configure2_5x
%ifarch %arm
%make CPPFLAGS="-DNO_ASM"
%else
%make
%endif

%check
%make check

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

# prepare documents
%{__rm} -rf documents
%{__mkdir} documents
%{__cp} -p examples/*.cc documents/

%{__rm} -rf %{buildroot}%{_datadir}/dvi

%{__rm} -rf %{buildroot}%{_bindir}
%{__rm} -rf %{buildroot}%{_mandir}
%{__rm} -rf %{buildroot}%{_datadir}/aclocal

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{develname}
%_install_info %{name}.info

%preun -n %{develname}
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO* documents/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_infodir}/*.info*
