%define major 6
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	C++ Class Library for Numbers
Name:		cln
Version:	1.3.6
Release:	2
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://www.ginac.de/CLN/
Source0:	http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2
Patch0:		cln-1.3.4-aarch64-compile.patch
BuildRequires:	gmp-devel

%description
CLN is a collection of C++ math classes and functions licensed under
the GPL that provides efficiency, type safety, and algebraic syntax in
a fast, memory-efficient library.

%package -n	%{libname}
Summary:	C++ Class Library for Numbers
Group:		Sciences/Mathematics
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
CLN is a collection of C++ math classes and functions licensed under
the GPL that provides efficiency, type safety, and algebraic syntax in
a fast, memory-efficient library.

%package -n	%{devname}
Summary:	Development files for programs using the CLN library
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package is necessary if you wish to develop software that uses
the CLN library.

%prep
%autosetup -p1

%build
%configure \
	--disable-static
%make 

%check
%make check

%install
%makeinstall_std

# prepare documents
rm -rf documents
mkdir documents
cp -p examples/*.cc documents/

rm -rf %{buildroot}%{_datadir}/dvi
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_datadir}/aclocal

%files -n %{libname}
%{_libdir}/libcln.so.%{major}*

%files -n %{devname}
%doc ChangeLog NEWS README TODO* documents/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

