Summary:	Universal Text Recognizer and Converter
Name:		utrac
Version:	0.3.0
Release:	%mkrel 6
License:	GPL
Group:		File tools
URL:		http://utrac.sourceforge.net/
Source0:	http://utrac.sourceforge.net/download/utrac-%{version}.tar.bz2
Patch0:		utrac-fix-long-64bit.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
UTRAC stands for Universal Text Recognizer and Converter. It is a command line
tool and a library that recognize the encoding of an input file (ex: UTF-8,
ISO-8859-1, CP437...) and its end-of-line type (CR, LF, CRLF). 

%prep

%setup -q
%patch0 -p1

perl -pi -e "s|/usr/local|%{_prefix}|g" Makefile
perl -pi -e "s|/lib|/%{_lib}|g" Makefile
perl -pi -e "s|/man/man1|/share/man/man1|g" Makefile

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/utrac
install -d %{buildroot}%{_mandir}/man1

install -m0755 utrac %{buildroot}%{_bindir}/
install -m0644 charsets.dat %{buildroot}%{_datadir}/utrac/
install -m0644 utrac.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README TODO doc/*.xml
%dir %{_datadir}/utrac
%attr(0755,root,root) %{_bindir}/utrac
%attr(0644,root,root) %{_datadir}/utrac/charsets.dat
%attr(0644,root,root) %{_mandir}/man1/*


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3.0-6mdv2010.0
+ Revision: 434623
- rebuild

* Sat Sep 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-5mdv2009.0
+ Revision: 284528
- fix #35379 (utrac segmentation fault)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3.0-3mdv2009.0
+ Revision: 255274
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3.0-1mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import utrac


* Tue Sep 12 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdv2007.0
- rebuild

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdk
- initial Mandriva package
