#
# Conditional build:
# _without_gnome	- without GNOME support
# _with_ext2undel	- with ext2 undelete fs
# _with_samba		- with SAMBA vfs support
# _with_x		- with text edit in X support
#
Summary:	A user-friendly file manager and visual shell
Summary(de):	Visuelle Shell Midnight Commander
Summary(fr):	Un gestionnaire de fichiers puissant et agr�able en mode console
Summary(pl):	Midnight Commander - pow�oka wizualna
Summary(tr):	Midnight Commander g�rsel kabu�u
Name:		mc
Version:	4.5.55
Release:	5
License:	GPL
Group:		Applications/Shells
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/mc/%{name}-%{version}.tar.gz
Source1:	%{name}serv.pamd
Source2:	%{name}serv.init
Source3:	%{name}-non-english-man-pages.tar.bz2
Source4:	%{name}-srpm
Patch0:		%{name}-mimekeys.patch
Patch1:		%{name}-rpmfs.patch
Patch2:		%{name}-system_popt.patch
Patch3:		%{name}-spec-syntax.patch
Patch4:		%{name}-gdeskpopt.patch
Patch5:		%{name}-prototype.patch
Patch6:		%{name}-gnome-editor.patch
Patch7:		%{name}-def_config.patch
Patch8:		%{name}-mouse_in_rxvt.patch
Patch9:		%{name}-proxy.patch
Patch10:	%{name}-nognome-amfix.patch
Patch11:	%{name}-urar.patch
Patch12:	%{name}-samba.patch
Patch13:	%{name}-nobashism.patch
Patch14:	%{name}-tinfo.patch
Patch15:	%{name}-vfs.patch
URL:		http://www.gnome.org/mc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	indent
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pam-devel
BuildRequires:	popt-devel
%ifnarch s390 s390x
BuildRequires:	gpm-devel
%endif
%{!?_without_gnome:BuildRequires:	ORBit-devel}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel >= 1.2.13}
%{!?_without_gnome:BuildRequires:	imlib-devel}
%{?_with_ext2undel:BuildRequires:	e2fsprogs-devel}
%{?_with_x:BuildRequires:	XFree86-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	rpm < 4.0
Requires:	file
Obsoletes:	tkmc

%define		_sysconfdir	/etc/X11/GNOME

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
ftp, view tar, zip files, and poke into RPMs for specific files. :-)

%description -l de
Midnight Commander ist ein Visual-Shell, �hnlich einem Dateimanager,
aber mit zus�tzlichen Funktionen. Es l�uft im Textmodus, kann jedoch
eine Maus unterst�tzen, wenn GPM betrieben wird. Seine coolsten
F�higkeiten sind die ftp-Option, das Einsehen von tar- und zip-Dateien
und das Herausfischen von spezifischen Dateien aus RPMs.

%description -l fr
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Il fonctionne en mode console (texte), mais peut �tre
contr�l� � la souris si GPM est pr�sent. Ses caract�ristiques les plus
remarquables sont la possibilit� de se connecter � un serveur FTP, de
visualiser des archives tar, de compresser des fichiers avec zip, de
r�cup�rer des fichiers dans les packages RPM, et tout ceci simplement.

%description -l pl
Midnight Commander jest wizualn� pow�ok� podobn� do Norton
Commandera. Pracuje w trybie tekstowym, ale ma tak�e wspomaganie dla
myszki. Jest super ;) MC ma wbudowanego klienta ftp, mo�e zagl�da� do
skompresowanego archiwum tarowego, do *.zip oraz *.rpm. Teraz r�wnie�
pracuje z urz�dzeniami /dev/pts/{0-2048} - standard Unix98.

%description -l tr
Midnight Commander bir dosya y�neticisine �ok benzeyen ancak daha
yetenekli bir g�rsel kabuktur. Metin ekranda �al���r ve GPM
�al���yorsa fare deste�i vard�r. En ho� �zellikleri ftp yapabilmesi,
tar, zip ve RPM dosyalar�n�n i�eriklerini g�sterebilmesidir.

%package -n mcserv
Summary:	Server for the Midnight Commander network file management system
Summary(de):	Midnight Commander File-Server
Summary(fr):	Serveur r�seau pour le gestionnaire de fichiers Midnight Commander
Summary(pl):	Serwer plik�w Midnight Commandera
Summary(tr):	Midnight Commander dosya sunucusu
Group:		Daemons
Prereq:		/sbin/chkconfig
Prereq:		rc-scripts
Requires:	pam >= 0.66
Requires:	portmap

%description -n mcserv
The Midnight Commander file management system will allow you to
manipulate the files on a remote machine as if they were local. This
is only possible if the remote machine is running the mcserv server
program. Mcserv provides clients running Midnight Commander with
access to the host's file systems.

%description -n mcserv -l de
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight
Commander. Es erm�glicht den Zugriff auf das Host-Dateisystem f�r
Clients, die das Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight
Commander file manager).

%description -n mcserv -l fr
Le syst�me de gestion de fichier Midnight Commander vous permet de
manipuler des fichiers sur une machine distante comme si ils �taient
sur votre propre machine. Ceci est possible seulement si la machine
distante poss�de le programme mcserv et que celui-ci est activ�.
Mcserv apporte aux machines clientes qui font tourner Midnight
Commander un acc�s aux fichiers situ�s sur l'h�te.

%description -n mcserv -l pl
Mcserv jest aplikacj� dla sieciowego systemy plik�w Midnight
Commandera. Pozwala na dost�p do systemu plik�w dla klienta
pracuj�cego pod MC i u�ywaj�cego jego systemu plik�w.

%description -n mcserv -l tr
mcserv, Midnight Commander a� dosya sisteminin sunucu program�d�r.
Midnight dosya sistemini �al��t�ran istemcilerin sunucu dosya
sistemine eri�imini sa�lar.

%package -n gmc
Summary:	Midnight Commander visual shell (GNOME version)
Summary(de):	Midnight Commander Visual-Shell (GNOME Version)
Summary(fr):	Version GNOME du gestionnaire de fichiers Midnight Commander
Summary(pl):	Midnight Commander - wizualna pow�oka (wersja GNOME)
Summary(tr):	Midnight Commander g�rsel kabu�u (GNOME s�r�m�)
Group:		X11/Applications
Requires:	%{name}	= %{version}

%description -n gmc
Midnight Commander is a visual shell much like a file manager, only
with way more features. This is the GNOME version. It's coolest
feature is the ability to ftp, view tar, zip files and poke into RPMs
for specific files. The GNOME version of Midnight Commander is not yet
finished though. :-(

%description -n gmc -l fr
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Ceci est la version pour GNOME. Ses caract�ristiques les
plus remarquables sont la possibilit� de se connecter � un serveur
FTP, de visualiser des archives tar, de compresser des fichiers avec
zip, et de r�cup�rer des fichiers dans les packages RPM. La version
GNOME de Midnight Commander n'est pas encore termin�e cependant. :-(

%description -n gmc -l pl
Midnight Commander jest wizualn� pow�ok�, posiadaj�c� znacznie
wi�cej funkcji ni� samo zarz�dzanie plikami. Ma wbudowanego klienta
ftp, potrafi przegl�da� pliki tar, zip oraz si�ga� do konkretnych
plik�w pakiet�w rpm. To jest wersja pracuj�ca pod GNOME. Niestety
nie jest ona jeszcze sko�czona.

%prep
%setup -q -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
gettextize --copy --force
aclocal -I \
	%{!?_without_gnome:%{_aclocaldir}/gnome}%{?_without_gnome:macros}
autoconf
automake -a -c
X11_WWW="
if [ -f /usr/X11R6/bin/netscape ]; then netscape;
else
  if [ -f /usr/X11R6/bin/galeon ]; then galeon;
  else
    if [ -f /usr/X11R6/bin/mozilla ]; then mozilla;
    else
      xterm -c lynx;
    fi;
  fi;
fi"
%configure \
	%{?_with_ext2undel:--with-ext2-undel}%{!?_with_ext2undel:--without-ext2undel} \
	--with-vfs \
	--with-netrc \
	--with-x \
	%{?_with_x:--with-tm-x-support} \
	--without-debug \
	--with-included-slang \
	--enable-largefile \
	--enable-mcserv-install \
	%{!?_without_gnome:--with-gnome}%{?_without_gnome:--without-gnome} \
	%{?_with_samba:--with-samba}

%{__make} confdir=%{_sysconfdir}/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,pam.d,profile.d}}

%{__make} install \
	confdir=%{_sysconfdir} \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

for a in es pl ; do
	for b in man1 man8 ; do
		install -d $RPM_BUILD_ROOT%{_mandir}/{$a,$a/$b}
		for c in man/$a/$b/* ; do
			install $c $RPM_BUILD_ROOT%{_mandir}/$a/$b
		done
	done
done

install %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/mc/extfs/srpm

install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/profile.d

mv -f $RPM_BUILD_ROOT%{_bindir}/mcserv $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf FAQ NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv
if [ -f /var/lock/subsys/mcserv ]; then
	/etc/rc.d/init.d/mcserv restart >&2
else
	echo "Run \"/etc/rc.d/init.d/mcserv start\" to start mcserv daemon."
fi

%preun -n mcserv
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/mcserv ]; then
		/etc/rc.d/init.d/mcserv stop >&2
	fi
	/sbin/chkconfig --del mcserv
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/mc*

%{_libdir}/mc/mc.ext

%{_libdir}/mc/mc.hlp
%lang(hu) %{_libdir}/mc/mc.hlp.hu
%{_libdir}/mc/mc.lib
%{_libdir}/mc/mc.menu
%{_libdir}/mc/mc.hint
%lang(cs) %{_libdir}/mc/mc.hint.cs
%lang(es) %{_libdir}/mc/mc.hint.es
%lang(hu) %{_libdir}/mc/mc.hint.hu
%lang(it) %{_libdir}/mc/mc.hint.it
%lang(nl) %{_libdir}/mc/mc.hint.nl
%lang(pl) %{_libdir}/mc/mc.hint.pl
%lang(ru) %{_libdir}/mc/mc.hint.ru
%lang(uk) %{_libdir}/mc/mc.hint.uk
%lang(zh) %{_libdir}/mc/mc.hint.zh

%attr(755,root,root) %{_libdir}/mc/bin/cons.saver

%{_libdir}/mc/extfs/README
%attr(755,root,root) %{_libdir}/mc/extfs/a
%attr(755,root,root) %{_libdir}/mc/extfs/apt
%attr(755,root,root) %{_libdir}/mc/extfs/audio
%attr(755,root,root) %{_libdir}/mc/extfs/bpp
%attr(755,root,root) %{_libdir}/mc/extfs/deb*
%attr(755,root,root) %{_libdir}/mc/extfs/dpkg
%attr(755,root,root) %{_libdir}/mc/extfs/ftplist
%attr(755,root,root) %{_libdir}/mc/extfs/hp48
%attr(755,root,root) %{_libdir}/mc/extfs/lslR
%attr(755,root,root) %{_libdir}/mc/extfs/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs/rpm*
%attr(755,root,root) %{_libdir}/mc/extfs/trpm
%attr(755,root,root) %{_libdir}/mc/extfs/uar*
%attr(755,root,root) %{_libdir}/mc/extfs/ucpio
%attr(755,root,root) %{_libdir}/mc/extfs/uha
%attr(755,root,root) %{_libdir}/mc/extfs/ulha
%attr(755,root,root) %{_libdir}/mc/extfs/urar
%attr(755,root,root) %{_libdir}/mc/extfs/uzip
%attr(755,root,root) %{_libdir}/mc/extfs/uzoo
%attr(755,root,root) %{_libdir}/mc/extfs/srpm
%{_libdir}/mc/extfs/extfs.ini
%{_libdir}/mc/extfs/sfs.ini
%{_libdir}/mc/syntax

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%attr(755,root,root) %config /etc/profile.d/*

%dir %{_libdir}/mc
%dir %{_libdir}/mc/bin
%dir %{_libdir}/mc/extfs

%files -n mcserv
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/*

%attr(754,root,root) %config /etc/rc.d/init.d/mcserv
%{_mandir}/man8/mcserv.8*
%lang(es) %{_mandir}/es/man8/mcserv.8*
%lang(pl) %{_mandir}/pl/man8/mcserv.8*
%attr(755,root,root) %{_sbindir}/mcserv

%{!?_without_gnome:%files -n gmc}
%{!?_without_gnome:%defattr(644,root,root,755)}

%{!?_without_gnome:%attr(755,root,root) %{_bindir}/gdesktoplnk}
%{!?_without_gnome:%attr(755,root,root) %{_bindir}/gmc*}
%{!?_without_gnome:%attr(755,root,root) %{_bindir}/plain-gmc}

%{!?_without_gnome:%{_sysconfdir}/mc.global}
%{!?_without_gnome:%{_sysconfdir}/CORBA/servers/gmc.gnorba}
%{!?_without_gnome:%{_datadir}/mime-info}
%{!?_without_gnome:%{_datadir}/pixmaps}
%{!?_without_gnome:%{_datadir}/mc}
