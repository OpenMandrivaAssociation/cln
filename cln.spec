%define	version	1.1.13
%define	release	%mkrel 1

%define	name	cln
%define	major	4
%define	libname	%mklibname %{name} %{major}

Summary:	C++ Class Library for Numbers
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gnu/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.1.9-string.patch
URL:		http://www.ginac.de/CLN/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gmp-devel

%description
A GPLed collection of C++ math classes and functions, that will bring
efficiency, type safety, algebraic syntax to everyone in a memory
and speed efficient library.

%package -n	%{libname}
Summary:	C++ Class Library for Numbers
Group:		Sciences/Mathematics
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
A GPLed collection of C++ math classes and functions, that will bring
efficiency, type safety, algebraic syntax to everyone in a memory
and speed efficient library.

%package -n	%{libname}-devel
Summary:	Development files for programs using the CLN library
Group:		Development/C++
Requires(post):	/sbin/install-info
Requires(preun): /sbin/install-info
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
This package is necessary if you wish to develop software based on
the CLN library.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%check
%make check

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

# prepare documents
%{__rm} -rf documents
%{__mkdir} documents
%{__mv} %{buildroot}%{_datadir}/html documents/
%{__cp} --parents examples/*.cc documents/

%{__rm} -rf %{buildroot}%{_datadir}/dvi

%multiarch_binaries %buildroot%_bindir/%name-config

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
%_install_info %{name}.info

%preun -n %{libname}-devel
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO* documents/*
%{_bindir}/cln-config
%multiarch_bindir/%name-config
%{_datadir}/aclocal/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_infodir}/*.info*
%{_mandir}/man1/*


