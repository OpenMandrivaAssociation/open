%define	name	open
%define	version	1.4
%define	release	%mkrel 19
Summary:	A tool which will start a program on a virtual console
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Terminals
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.4-includes.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The open command starts a specified command with the first available virtual
console, or on a virtual console that you specify.

Install the open package if you regularly use virtual consoles to run programs.

%prep
%setup -q
%patch0 -p1

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

make BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install
mkdir -p $RPM_BUILD_ROOT/bin
mv $RPM_BUILD_ROOT%{_bindir}/open $RPM_BUILD_ROOT/bin
ln -s /bin/open $RPM_BUILD_ROOT%{_bindir}/open

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/bin/open
%{_bindir}/open
%{_bindir}/switchto
%{_mandir}/man1/open.*
%{_mandir}/man1/switchto.*


