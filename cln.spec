%define	version	1.2.0
%define	release	%mkrel 1

%define	name	 cln
%define	major	 5
%define oldmajor 4
%define	libname	 %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define olddevelname %mklibname %{name} %{oldmajor} -d

Summary:	C++ Class Library for Numbers
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gnu/%{name}-%{version}.tar.bz2
URL:		http://www.ginac.de/CLN/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
Obsoletes:	%{olddevelname}

%description -n %{develname}
This package is necessary if you wish to develop software that uses
the CLN library.

%prep
%setup -q

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

%{__rm} -rf %{buildroot}%{_bindir}
%{__rm} -rf %{buildroot}%{_mandir}
%{__rm} -rf %{buildroot}%{_datadir}/aclocal

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{develname}
%_install_info %{name}.info

%preun -n %{develname}
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO* documents/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_infodir}/*.info*
