%define	name	open
%define	version	1.4
%define	release	%mkrel 22
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
rm -rf %{buildroot}
mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/man1}

make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1 install
mkdir -p %{buildroot}/bin
mv %{buildroot}%{_bindir}/open %{buildroot}/bin
ln -s /bin/open %{buildroot}%{_bindir}/open

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/bin/open
%{_bindir}/open
%{_bindir}/switchto
%{_mandir}/man1/open.*
%{_mandir}/man1/switchto.*


