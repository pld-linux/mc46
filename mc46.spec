#
# Conditional build:
# bcond_off_gnome	- without GNOME support
# bcond_on_ext2undel	- with ext2 undelete fs
#
Summary:	A user-friendly file manager and visual shell
Summary(de):	Visuelle Shell Midnight Commander 
Summary(fr):	Un gestionnaire de fichiers puissant et agréable en mode console
Summary(pl):	Midnight Commander - pow³oka wizualna
Summary(tr):	Midnight Commander görsel kabuðu
Name:		mc
Version:	4.5.51
Release:	22
License:	GPL
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/mc/%{name}-%{version}.tar.gz
Source1:	%{name}serv.pamd
Source2:	%{name}serv.init
Patch0:		%{name}-mimekeys.patch
Patch1:		%{name}-rpmfs.patch
Patch2:		%{name}-system_popt.patch
Patch3:		%{name}-spec-syntax.patch
Patch4:		%{name}-showagain.patch
Patch5:		%{name}-gdeskpopt.patch
Patch6:		%{name}-prototype.patch
Patch7:		%{name}-stderr.patch
Patch8:		%{name}-fixrescan.patch
Patch9:		%{name}-gnome-editor.patch
Patch10:	%{name}-extention.patch
Patch11:	%{name}-fixsh.patch
Patch12:	%{name}-def_config.patch
Patch13:	%{name}-rpmfs_rpm40.patch
Patch14:	%{name}-ftpfs_storage_on_root.patch
Patch15:	%{name}-editor_argument.patch
Patch16:	%{name}-mouse_in_rxvt.patch
Patch17:	%{name}-security_fix_cons.saver.patch
Patch18:	%{name}-spellfix_heirarchy.patch
Patch19:	%{name}-use_old_sorting.patch
URL:		http://mc.blackdown.org/mc/
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	popt-devel
BuildRequires:	gettext-devel
BuildRequires:	indent
%{!?bcond_off_gnome:BuildRequires:	ORBit-devel}
%{!?bcond_off_gnome:BuildRequires:	gnome-libs-devel}
%{!?bcond_off_gnome:BuildRequires:	imlib-devel}
%{!?bcond_off_gnome:BuildRequires:	gtk+-devel}
%{!?bcond_off_gnome:BuildRequires:	esound-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	rpm < 4.0
Obsoletes:	tkmc

%define		_sysconfdir	/etc/X11/GNOME

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
ftp, view tar, zip files, and poke into RPMs for specific files. :-)

%description -l de
Midnight Commander ist ein Visual-Shell, ähnlich einem Dateimanager,
aber mit zusätzlichen Funktionen. Es läuft im Textmodus, kann jedoch
eine Maus unterstützen, wenn GPM betrieben wird. Seine coolsten
Fähigkeiten sind die ftp-Option, das Einsehen von tar- und zip-Dateien
und das Herausfischen von spezifischen Dateien aus RPMs.

%description -l fr
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Il fonctionne en mode console (texte), mais peut être
contrôlé à la souris si GPM est présent. Ses caractéristiques les plus
remarquables sont la possibilité de se connecter à un serveur FTP, de
visualiser des archives tar, de compresser des fichiers avec zip, de
récupérer des fichiers dans les packages RPM, et tout ceci simplement.

%description -l pl
Midnight Commander jest wizualnym shellem podobnym do Norton
Commandera. Pracuje w trybie tekstowym, ale ma tak¿e wspomaganie dla
myszki. Jest super ;) MC ma wbudowanego klienta ftp, mo¿e zagl±daæ do
skompresowanego archiwum tarowego, do *.zip oraz *.rpm. Teraz równie¿
ma wspomaganie dla urz±dzeñ /dev/pts/{0-2048} - standard Unix98.

%description -l tr
Midnight Commander bir dosya yöneticisine çok benzeyen ancak daha
yetenekli bir görsel kabuktur. Metin ekranda çalýþýr ve GPM
çalýþýyorsa fare desteði vardýr. En hoþ özellikleri ftp yapabilmesi,
tar, zip ve RPM dosyalarýnýn içeriklerini gösterebilmesidir.

%package -n mcserv
Summary:	Server for the Midnight Commander network file management system
Summary(de):	Midnight Commander File-Server 
Summary(fr):	Serveur réseau pour le gestionnaire de fichiers Midnight Commander
Summary(pl):	Serwer plików Midnight Commandera
Summary(tr):	Midnight Commander dosya sunucusu
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Prereq:		/sbin/chkconfig
Requires:	portmap
Prereq:		rc-scripts
Requires:	pam >= 0.66

%description -n mcserv
The Midnight Commander file management system will allow you to
manipulate the files on a remote machine as if they were local. This
is only possible if the remote machine is running the mcserv server
program. Mcserv provides clients running Midnight Commander with
access to the host's file systems.

%description -l de -n mcserv
mcserv ist das Server-Programm für das Netzwerkdateisystem Midnight
Commander. Es ermöglicht den Zugriff auf das Host-Dateisystem für
Clients, die das Midnight-Dateisystem ausführen (z.Zt. nur Midnight
Commander file manager).

%description -l fr -n mcserv
Le système de gestion de fichier Midnight Commander vous permet de
manipuler des fichiers sur une machine distante comme si ils étaient
sur votre propre machine. Ceci est possible seulement si la machine
distante possède le programme mcserv et que celui-ci est activé.
Mcserv apporte aux machines clientes qui font tourner Midnight
Commander un accès aux fichiers situés sur l'hôte.

%description -l pl -n mcserv
Mcserv jest aplikacj± dla sieciowego systemy plików Midnight
Commandera. Pozwala na dostêp do systemu plików dla klienta
pracuj±cego pod MC i u¿ywaj±cego jego systemu plików.

%description -l tr -n mcserv
mcserv, Midnight Commander að dosya sisteminin sunucu programýdýr.
Midnight dosya sistemini çalýþtýran istemcilerin sunucu dosya
sistemine eriþimini saðlar.

%package -n gmc
Summary:	Midnight Commander visual shell (GNOME version)
Summary(de):	Midnight Commander Visual-Shell (GNOME Version) 
Summary(fr):	Version GNOME du gestionnaire de fichiers Midnight Commander
Summary(pl):	Midnight Commander - wizualny shell (wersja GNOME)
Summary(tr):	Midnight Commander görsel kabuðu (GNOME sürümü)
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}	= %{version}

%description -n gmc
Midnight Commander is a visual shell much like a file manager, only
with way more features. This is the GNOME version. It's coolest
feature is the ability to ftp, view tar, zip files and poke into RPMs
for specific files. The GNOME version of Midnight Commander is not yet
finished though. :-(

%description -l fr -n gmc
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Ceci est la version pour GNOME. Ses caractéristiques les
plus remarquables sont la possibilité de se connecter à un serveur
FTP, de visualiser des archives tar, de compresser des fichiers avec
zip, et de récupérer des fichiers dans les packages RPM. La version
GNOME de Midnight Commander n'est pas encore terminée cependant. :-(

%prep
%setup -q
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
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%build
gettextize --copy --force
%configure \
	%{?bcond_on_ext2undel:--with-ext2-undel}%{!?bcond_on_ext2undel:--without-ext2undel} \
	--with-netrc \
	--with-x \
	--without-debug \
	--with-included-slang \
	%{!?bcond_off_gnome:--with-gnome}%{?bcond_off_gnome:--without-gnome}

%{__make} confdir=%{_sysconfdir}/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,pam.d,profile.d}}

%{__make} install \
	confdir=%{_sysconfdir} \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

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

%attr(755,root,root) %{_bindir}/mc
%attr(755,root,root) %{_bindir}/mcedit
%attr(755,root,root) %{_bindir}/mcmfmt

%{_libdir}/mc/mc.ext
%{_libdir}/mc/mc.hlp
%{_libdir}/mc/mc.lib
%{_libdir}/mc/mc.menu
%{_libdir}/mc/mc.hint
%lang(cs) %{_libdir}/mc/mc.hint.cs
%lang(es) %{_libdir}/mc/mc.hint.es

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

%{!?bcond_off_gnome:%files -n gmc}
%{!?bcond_off_gnome:%defattr(644,root,root,755)}

%{!?bcond_off_gnome:%attr(755,root,root) %{_bindir}/gdesktoplnk}
%{!?bcond_off_gnome:%attr(755,root,root) %{_bindir}/gmc}
%{!?bcond_off_gnome:%attr(755,root,root) %{_bindir}/plain-gmc}

%{!?bcond_off_gnome:%{_sysconfdir}/mc.global}
%{!?bcond_off_gnome:%{_sysconfdir}/CORBA/servers/gmc.gnorba}
%{!?bcond_off_gnome:%{_libdir}/mc/layout}
%{!?bcond_off_gnome:%{_libdir}/mc/mc-gnome.ext}
%{!?bcond_off_gnome:%{_datadir}/mime-info}
%{!?bcond_off_gnome:%{_datadir}/pixmaps}
%{!?bcond_off_gnome:%{_datadir}/mc}
