Summary:	A user-friendly file manager and visual shell
Summary(de):	Visuelle Shell Midnight Commander 
Summary(fr):	Un gestionnaire de fichiers puissant et agr�able en mode console
Summary(pl):	Midnight Commander - pow�oka wizualna
Summary(tr):	Midnight Commander g�rsel kabu�u
Name:		mc
Version:	4.5.41
Release:	2
Copyright:	GPL
Group:		Shells
Group(pl):	Pow�oki
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/mc/%{name}-%{version}.tar.gz
Source1:	mcserv.pamd
Source2:	mcserv.init
Patch0:		mc-mimekeys.patch
Patch1:		mc-enlightenment_keys.patch
Patch2:		mc-rpmfs.patch
URL:		http://mc.blackdown.org/mc/
BuildRequires:	glib-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	XFree86-devel
BuildRequires:	ORBit-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Conflicts:	rpm =< 2.5.3
Obsoletes:	tkmc

%define		sysconfdir	/etc

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features. It is text mode, but also includes mouse support if you are
running GPM. Its coolest feature is the ability to ftp, view tar, zip files,
and poke into RPMs for specific files.  :-)

%description -l de
Midnight Commander ist ein Visual-Shell, �hnlich einem Dateimanager, aber
mit zus�tzlichen Funktionen. Es l�uft im Textmodus, kann jedoch eine Maus
unterst�tzen, wenn GPM betrieben wird. Seine coolsten F�higkeiten sind die
ftp-Option, das Einsehen von tar- und zip-Dateien und das Herausfischen von
spezifischen Dateien aus RPMs.

%description -l fr
Midnight Commander est une interface pour la ligne de commande qui tient
beaucoup du gestionnaire de fichiers, mais est bien plus puissant. Il
fonctionne en mode console (texte), mais peut �tre contr�l� � la souris si
GPM est pr�sent. Ses caract�ristiques les plus remarquables sont la
possibilit� de se connecter � un serveur FTP, de visualiser des archives
tar, de compresser des fichiers avec zip, de r�cup�rer des fichiers dans les
packages RPM, et tout ceci simplement.

%description -l pl
Midnight Commander jest wizualnym shellem podobnym do Norton Commandera.
Pracuje w trybie tekstowym, ale ma tak�e wspomaganie dla myszki. Jest super
;) MC ma wbudowanego klienta ftp, mo�e zagl�da� do skompresowanego archiwum
tarowego, do *.zip oraz *.rpm. Teraz r�wnie� ma wspomaganie dla urz�dze�
/dev/pts/{0-2048} - standard Unix98.  

%description -l tr
Midnight Commander bir dosya y�neticisine �ok benzeyen ancak daha yetenekli
bir g�rsel kabuktur. Metin ekranda �al���r ve GPM �al���yorsa fare deste�i
vard�r. En ho� �zellikleri ftp yapabilmesi, tar, zip ve RPM dosyalar�n�n
i�eriklerini g�sterebilmesidir.
 
%package -n mcserv
Summary:	Server for the Midnight Commander network file management system
Summary(de):	Midnight Commander File-Server 
Summary(fr):	Serveur r�seau pour le gestionnaire de fichiers Midnight Commander
Summary(pl):	Serwer plik�w Midnight Commandera
Summary(tr):	Midnight Commander dosya sunucusu
Group:		Daemons
Group(pl):	Serwery
Prereq:		/sbin/chkconfig
Requires:	portmap
Requires:	rc-scripts
Requires:	pam >= 0.66

%description -n mcserv
The Midnight Commander file management system will allow you to manipulate
the files on a remote machine as if they were local.  This is only possible
if the remote machine is running the mcserv server program. Mcserv provides
clients running Midnight Commander with access to the host's file systems.

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l fr -n mcserv
Le syst�me de gestion de fichier Midnight Commander vous permet de manipuler
des fichiers sur une machine distante comme si ils �taient sur votre propre
machine. Ceci est possible seulement si la machine distante poss�de le
programme mcserv et que celui-ci est activ�. Mcserv apporte aux machines
clientes qui font tourner Midnight Commander un acc�s aux fichiers situ�s
sur l'h�te.

%description -l pl -n mcserv
Mcserv jest aplikacj� dla sieciowego systemy plik�w Midnight Commandera.
Pozwala na dost�p do systemu plik�w dla klienta pracuj�cego pod MC i 
u�ywaj�cego jego systemu plik�w.

%description -l tr -n mcserv
mcserv, Midnight Commander a� dosya sisteminin sunucu program�d�r. Midnight
dosya sistemini �al��t�ran istemcilerin sunucu dosya sistemine eri�imini
sa�lar.

%package -n gmc
Summary:	Midnight Commander visual shell (GNOME version)
Summary(de):	Midnight Commander Visual-Shell (GNOME Version) 
Summary(fr):	Version GNOME du gestionnaire de fichiers Midnight Commander
Summary(pl):	Midnight Commander wizualny shell (wersja GNOME)
Summary(tr):	Midnight Commander g�rsel kabu�u (GNOME s�r�m�)
Group:		X11/GNOME
Group(pl):	X11/GNOME
Requires:	%{name}	= %{version}

%description -n gmc
Midnight Commander is a visual shell much like a file manager, only with
way more features.  This is the GNOME version. It's coolest feature is the
ability to ftp, view tar, zip files and poke into RPMs for specific files.
The GNOME version of Midnight Commander is not yet finished though. :-(

%description -l fr -n gmc
Midnight Commander est une interface pour la ligne de commande qui tient
beaucoup du gestionnaire de fichiers, mais est bien plus puissant. Ceci est
la version pour GNOME. Ses caract�ristiques les plus remarquables sont la
possibilit� de se connecter � un serveur FTP, de visualiser des archives
tar, de compresser des fichiers avec zip, et de r�cup�rer des fichiers dans
les packages RPM. La version GNOME de Midnight Commander n'est pas encore
termin�e cependant. :-(

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-ext2undel \
	--with-netrc \
	--with-x \
	--without-debug \
	--with-included-slang \
	--with-gnome

make confdir=/etc/X11/GNOME/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,pam.d,profile.d}}

make install \
	confdir=/etc/X11/GNOME/ \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/profile.d

mv $RPM_BUILD_ROOT%{_bindir}/mcserv $RPM_BUILD_ROOT%{_sbindir} 

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[18]/* \
	FAQ NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv
if test -r /var/run/mcserv.pid; then
	/etc/rc.d/init.d/mcserv restart >&2
else
	echo "Run \"/etc/rc.d/init.d/mcserv start\" to start mcserv daemon."
fi

%preun -n mcserv
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del mcserv
	/etc/rc.d/init.d/mcserv stop >&2
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/mc
%attr(755,root,root) %{_bindir}/mcedit
%attr(755,root,root) %{_bindir}/mcmfmt

%{_libdir}/mc/mc.ext
%{_libdir}/mc/mc.hint
%{_libdir}/mc/mc.hlp
%{_libdir}/mc/mc.lib
%{_libdir}/mc/mc.menu

%attr(755,root,root) %{_libdir}/mc/bin/cons.saver

%attr(755,root,root) %{_libdir}/mc/extfs/a
%attr(755,root,root) %{_libdir}/mc/extfs/deb
%attr(755,root,root) %{_libdir}/mc/extfs/ftplist
%attr(755,root,root) %{_libdir}/mc/extfs/hp48
%attr(755,root,root) %{_libdir}/mc/extfs/lslR
%attr(755,root,root) %{_libdir}/mc/extfs/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs/rpm
%attr(755,root,root) %{_libdir}/mc/extfs/uar
%attr(755,root,root) %{_libdir}/mc/extfs/uarj
%attr(755,root,root) %{_libdir}/mc/extfs/ucpio
%attr(755,root,root) %{_libdir}/mc/extfs/ulha
%attr(755,root,root) %{_libdir}/mc/extfs/urar
%attr(755,root,root) %{_libdir}/mc/extfs/uzip
%attr(755,root,root) %{_libdir}/mc/extfs/uzoo
%{_libdir}/mc/extfs/extfs.ini
%{_libdir}/mc/extfs/sfs.ini
%{_libdir}/mc/syntax

%{_mandir}/man1/*
%attr(755,root,root) %config /etc/profile.d/*

%dir %{_libdir}/mc
%dir %{_libdir}/mc/bin
%dir %{_libdir}/mc/extfs

%files -n mcserv
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/*

%attr(754,root,root) %config /etc/rc.d/init.d/mcserv
%{_mandir}/man8/mcserv.8*
%attr(755,root,root) %{_sbindir}/mcserv

%files -n gmc
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/gmc
%attr(755,root,root) %{_bindir}/plain-gmc

/etc/X11/GNOME/mc.global
/etc/CORBA/servers/gmc.gnorba
%{_libdir}/mc/layout
%{_libdir}/mc/mc-gnome.ext
%{_libdir}/mc/term
%{_datadir}/mime-info
%{_datadir}/pixmaps
%{_datadir}/mc
