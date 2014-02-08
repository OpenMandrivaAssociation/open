%define	name	open
%define	version	1.4
%define release	25
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-22mdv2011.0
+ Revision: 666944
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-21mdv2011.0
+ Revision: 607010
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-20mdv2010.1
+ Revision: 523485
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-19mdv2010.0
+ Revision: 426269
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-18mdv2009.1
+ Revision: 351647
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4-17mdv2009.0
+ Revision: 223360
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.4-16mdv2008.1
+ Revision: 130942
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot
- fix man pages


* Sun Jan 28 2007 Olivier Thauvin <nanardon@mandriva.org> 1.4-16mdv2007.0
+ Revision: 114616
- mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.4-15mdk
- Rebuild

