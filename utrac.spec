Summary:	Universal Text Recognizer and Converter
Name:		utrac
Version:	0.3.0
Release:	%mkrel 4
License:	GPL
Group:		File tools
URL:		http://utrac.sourceforge.net/
Source0:	http://utrac.sourceforge.net/download/utrac-0.3.0.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
UTRAC stands for Universal Text Recognizer and Converter. It is a
command line tool and a library that recognize the encoding of an
input file (ex: UTF-8, ISO-8859-1, CP437...) and its end-of-line
type (CR, LF, CRLF). 

%prep

%setup -q

perl -pi -e "s|/usr/local|%{_prefix}|g" Makefile
perl -pi -e "s|/lib|/%{_lib}|g" Makefile
perl -pi -e "s|/man/man1|/share/man/man1|g" Makefile

%build

%make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/utrac
install -d %{buildroot}%{_mandir}/man1

install -m0755 utrac %{buildroot}%{_bindir}/
install -m0644 charsets.dat %{buildroot}%{_datadir}/utrac/
install -m0644 utrac.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README TODO doc/*.xml
%dir %{_datadir}/utrac
%attr(0755,root,root) %{_bindir}/utrac
%attr(0644,root,root) %{_datadir}/utrac/charsets.dat
%attr(0644,root,root) %{_mandir}/man1/*

