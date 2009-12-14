# TODO:
# - check spec-syntax,mo patches
# - update ancient X11_WWW (or drop if it's no longer used)
#
# Conditional build:
%bcond_with	ext2undel	# with ext2 undelete fs
%bcond_without	perl_vfs	# without perl depending vfs'es -- to avoid perl autoreq
%bcond_with	samba		# with SAMBA vfs support
%bcond_without	x		# without text edit in X support
#
%define	snap	pre4
Summary:	A user-friendly file manager and visual shell
Summary(de.UTF-8):	Visuelle Shell Midnight Commander
Summary(es.UTF-8):	Interpretador de comandos visual Midnight Commander
Summary(fr.UTF-8):	Un gestionnaire de fichiers puissant et agréable en mode console
Summary(ja.UTF-8):	使いやすいファイルマネージャとビジュアルシェル
Summary(pl.UTF-8):	Midnight Commander - powłoka wizualna
Summary(pt_BR.UTF-8):	Interpretador de comandos visual Midnight Commander
Summary(ru.UTF-8):	Диспетчер файлов Midnight Commander
Summary(tr.UTF-8):	Midnight Commander görsel kabuğu
Summary(uk.UTF-8):	Диспетчер файлів Midnight Commander
Summary(zh_CN.UTF-8):	一个方便实用的文件管理器和虚拟Shell
Name:		mc
Version:	4.7.0
Release:	0.9
License:	GPL v2+
Group:		Applications/Shells
Source0:	http://www.midnight-commander.org/downloads/%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	7bdc0ac4fe57c19a6bf2fd3e8894a073
Source1:	%{name}serv.pamd
Source2:	%{name}serv.init
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	17d7b574e1b85ad6f8ddceda9e841f19
Source6:	%{name}serv.sysconfig
Source7:	%{name}.desktop
Source8:	%{name}.png
Patch0:		%{name}-rpmfs.patch
Patch1:		slang-8bit_xterm.patch
Patch4:		%{name}-home_etc2.patch
Patch5:		%{name}-pl.patch
Patch6:		%{name}-no-ws-visible.patch
Patch11:	%{name}-noperl-vfs.patch
# at now syntax highligthing for PLD-update-TODO and CVSROOT/users
Patch12:	%{name}-pld-developerfriendly.patch
Patch17:	%{name}-nolibs.patch
Patch24:	%{name}-find_options.patch
URL:		http://www.midnight-commander.org/
BuildRequires:	It's broken, see changelog!
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	indent
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel >= 2.2.1
%ifnarch s390 s390x
BuildRequires:	gpm-devel
%endif
# Needed? %%{?with_perl_vfs:Requires:	perl-base}
%{?with_x:BuildRequires:	xorg-lib-libX11-devel}
%{?with_ext2undel:BuildRequires:	e2fsprogs-devel}
Requires:	file
Requires:	pam >= 0.77.3
Requires:	sed
Requires:	setup >= 2.4.6-2
Suggests:	bzip2
Suggests:	gzip
Suggests:	lynx
Suggests:	p7zip-standalone
Suggests:	rpm-utils
Suggests:	tar
Suggests:	unzip
Obsoletes:	tkmc
Conflicts:	bash < 2.05b
Conflicts:	rpm < 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
FTP, view tar, zip files, and poke into RPMs for specific files. :-)

%description -l de.UTF-8
Midnight Commander ist ein Visual-Shell, ähnlich einem Dateimanager,
aber mit zusätzlichen Funktionen. Es läuft im Textmodus, kann jedoch
eine Maus unterstützen, wenn GPM betrieben wird. Seine coolsten
Fähigkeiten sind die FTP-Option, das Einsehen von tar- und zip-Dateien
und das Herausfischen von spezifischen Dateien aus RPMs.

%description -l es.UTF-8
Midnight Commander es un interpretador de comandos visual que más
parece un administrador de archivos, solamente con varias
características a más. Es un programa en modo texto, pero incluye
soporte para ratón, si estuviera ejecutando GPM o en una ventana
xterm. Su característica más genial es la habilidad de cotillear en
RPMs buscando archivos específicos. :-)

%description -l fr.UTF-8
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Il fonctionne en mode console (texte), mais peut être
contrôlé à la souris si GPM est présent. Ses caractéristiques les plus
remarquables sont la possibilité de se connecter à un serveur FTP, de
visualiser des archives tar, de compresser des fichiers avec zip, de
récupérer des fichiers dans les packages RPM, et tout ceci simplement.

%description -l ja.UTF-8
Midnight Commander はいろいろな機能を持ったファイルマネージャ兼
ビジュアルシェルです。これはテキストモードのアプリケーションですが、
GPM を使っている場合、マウスが使えます。 Midnight Commander には、 FTP
に接続できたり、 tar や zip や RPM の中が見えるなど、クールな機能
があります。

%description -l pl.UTF-8
Midnight Commander jest wizualną powłoką podobną do Norton Commandera.
Pracuje w trybie tekstowym, ale ma także obsługę myszki. Jest super ;)
MC ma wbudowanego klienta FTP, może zaglądać do skompresowanych
archiwów tar i zip, a także oglądać pliki w pakietach RPM.

%description -l pt_BR.UTF-8
Midnight Commander é um interpretador de comandos visual que mais
parece um gerenciador de arquivos, somente com várias características
a mais. Ele é um programa de modo texto, mas inclui suporte para mouse
se você estiver rodando GPM ou em uma janela xterm. Sua característica
mais legal é a habilidade de bisbilhotar em RPMs procurando arquivos
específicos. :-)

%description -l tr.UTF-8
Midnight Commander bir dosya yöneticisine çok benzeyen ancak daha
yetenekli bir görsel kabuktur. Metin ekranda çalışır ve GPM
çalışıyorsa fare desteği vardır. En hoş özellikleri FTP yapabilmesi,
tar, zip ve RPM dosyalarının içeriklerini gösterebilmesidir.

%package -n mcserv
Summary:	Server for the Midnight Commander network file management system
Summary(de.UTF-8):	Midnight Commander File-Server
Summary(es.UTF-8):	Servidor de archivos del Midnight Commander
Summary(fr.UTF-8):	Serveur réseau pour le gestionnaire de fichiers Midnight Commander
Summary(ja.UTF-8):	Midnight Commander でネットワークファイルマネージメントを行うサーバ
Summary(pl.UTF-8):	Serwer plików Midnight Commandera
Summary(pt_BR.UTF-8):	Servidor de arquivos do Midnight Commander
Summary(ru.UTF-8):	Midnight Commander файл-сервер
Summary(tr.UTF-8):	Midnight Commander dosya sunucusu
Summary(uk.UTF-8):	Midnight Commander файл-сервер
Summary(zh_CN.UTF-8):	mc 网络文件管理系统的服务器。
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	pam >= 0.99.7.1-1
Requires:	portmap
Requires:	rc-scripts >= 0.4.1.5

%description -n mcserv
The Midnight Commander file management system will allow you to
manipulate the files on a remote machine as if they were local. This
is only possible if the remote machine is running the mcserv server
program. Mcserv provides clients running Midnight Commander with
access to the host's file systems.

%description -n mcserv -l de.UTF-8
mcserv ist das Server-Programm für das Netzwerkdateisystem Midnight
Commander. Es ermöglicht den Zugriff auf das Host-Dateisystem für
Clients, die das Midnight-Dateisystem ausführen (z.Zt. nur Midnight
Commander file manager).

%description -n mcserv -l es.UTF-8
Mcserv es un servidor para el sistema de archivos en red del Midnight
Commander. Permite que clientes usando el mc accedan remotamente al
sistema de archivos de la máquina en que está ejecutando.

%description -n mcserv -l fr.UTF-8
Le système de gestion de fichier Midnight Commander vous permet de
manipuler des fichiers sur une machine distante comme si ils étaient
sur votre propre machine. Ceci est possible seulement si la machine
distante possède le programme mcserv et que celui-ci est activé.
Mcserv apporte aux machines clientes qui font tourner Midnight
Commander un accès aux fichiers situés sur l'hôte.

%description -n mcserv -l ja.UTF-8
Midnight Commander
のファイル管理システムは、リモートマシンにあるファイルを
ローカルにあるかのように扱うことができます。この機能は mcserv
プログラムを 実行しているリモートマシンに対してのみ働きます。 Mcserv
は Midnight Commander
クライアントに対して、このホストのファイルシステムを提供します。

%description -n mcserv -l pl.UTF-8
Mcserv jest aplikacją dla sieciowego systemu plików Midnight
Commandera. Pozwala na dostęp do systemu plików dla klienta
pracującego pod MC i używającego jego systemu plików.

%description -n mcserv -l pt_BR.UTF-8
Mcserv é um servidor para o sistema de arquivos em rede do Midnight
Commander. Ele permite que clientes usando o mc acessem remotamente o
sistema de arquivos da máquina em que está rodando.

%description -n mcserv -l ru.UTF-8
mcserv - это серверная программа для сетевой файловой системы Midnight
Commander. Она обеспечивает доступ к удаленной файловой системе
клиентам, поддерживающим файловую систему Midnight Commander (в
настоящее время только собственно Midnight Commander).

%description -n mcserv -l tr.UTF-8
mcserv, Midnight Commander ağ dosya sisteminin sunucu programıdır.
Midnight dosya sistemini çalıştıran istemcilerin sunucu dosya
sistemine erişimini sağlar.

%description -n mcserv -l uk.UTF-8
mcserv - це серверна програма для мережевої файлової системи Midnight
Commander. Вона забезпечує доступ до віддаленої файлової системи
клієнтам, що підтримують файлову систему Midnight Commander (наразі
тільки власне Midnight Commander).

%prep
%setup -q -a3 -n %{name}-%{version}-%{snap}
%patch0 -p1
%patch1 -p1
cp -f vfs/extfs/{rpm,srpm}
# doesn't apply
#%patch4 -p1
# doesn't apply
#%patch5 -p1
%patch6 -p1
%{!?with_perl_vfs:%patch11 -p1}
%patch12 -p1
%patch17 -p1
%if "%{pld_release}" == "ti"
%patch24 -p1
%endif

rm -f po/stamp-po

sed -i 's:|hxx|:|hh|hpp|hxx|tcc|:' syntax/Syntax

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
X11_WWW="
if [ -f /usr/bin/iceweasel ]; then
	iceweasel;
else
	if [ -f /usr/bin/galeon ]; then
		galeon
	else
		if [ -f /usr/bin/mozilla ]; then
			mozilla
		else
			xterm -c lynx
		fi;
	fi;
fi"

%configure \
	--enable-dependency-tracking \
	--enable-charset \
	--with%{!?debug:out}-debug \
	--with%{!?with_ext2undel:out}-ext2undel \
	--with%{!?with_x:out}-x \
	--with-vfs \
	--enable-vfs-mcfs \
	--enable-mcserver \
	%{?with_samba:--with-samba} \
	--with-configdir=/etc/samba \
	--with-codepagedir=/etc/samba/codepages \
	--with-gpm-mouse \
	--with-screen=slang \
	--with-edit

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_pixmapsdir},%{_desktopdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,shrc.d,sysconfig} \
	$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/mcserv
install %{SOURCE7} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE8} $RPM_BUILD_ROOT%{_pixmapsdir}

for a in es pl ; do
	for b in man1 man8 ; do
		install -d $RPM_BUILD_ROOT%{_mandir}/{$a,$a/$b}
		for c in man/$a/$b/* ; do
			install $c $RPM_BUILD_ROOT%{_mandir}/$a/$b
		done
	done
done

install contrib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/shrc.d

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/be-tarask

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv
%service mcserv restart "mcserv daemon"

%preun -n mcserv
if [ "$1" = "0" ]; then
	%service mcserv stop
	/sbin/chkconfig --del mcserv
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/mc*
%config /etc/shrc.d/*
%attr(755,root,root) %{_libdir}/mc/cons.saver
%dir %{_libdir}/mc
%attr(755,root,root) %{_libdir}/mc/*.sh
%attr(755,root,root) %{_libdir}/mc/*.csh
%dir %{_datadir}/mc

%{_datadir}/mc/skins
%{_datadir}/mc/syntax

%{_datadir}/mc/mc.hlp
%lang(es) %{_datadir}/mc/mc.hlp.es
%lang(hu) %{_datadir}/mc/mc.hlp.hu
%lang(it) %{_datadir}/mc/mc.hlp.it
%lang(pl) %{_datadir}/mc/mc.hlp.pl
%lang(ru) %{_datadir}/mc/mc.hlp.ru
%lang(sr) %{_datadir}/mc/mc.hlp.sr
%{_datadir}/mc/mc.hint
%lang(cs) %{_datadir}/mc/mc.hint.cs
%lang(es) %{_datadir}/mc/mc.hint.es
%lang(hu) %{_datadir}/mc/mc.hint.hu
%lang(it) %{_datadir}/mc/mc.hint.it
%lang(nl) %{_datadir}/mc/mc.hint.nl
%lang(pl) %{_datadir}/mc/mc.hint.pl
%lang(ru) %{_datadir}/mc/mc.hint.ru
%lang(sr) %{_datadir}/mc/mc.hint.sr
%lang(uk) %{_datadir}/mc/mc.hint.uk
%lang(zh) %{_datadir}/mc/mc.hint.zh

%dir %{_datadir}/mc/extfs
%{_datadir}/mc/extfs/README
%if %{with perl_vfs}
%attr(755,root,root) %{_datadir}/mc/extfs/a
%attr(755,root,root) %{_datadir}/mc/extfs/apt
%attr(755,root,root) %{_datadir}/mc/extfs/deb*
%attr(755,root,root) %{_datadir}/mc/extfs/dpkg
%attr(755,root,root) %{_datadir}/mc/extfs/mailfs
%attr(755,root,root) %{_datadir}/mc/extfs/patchfs
%attr(755,root,root) %{_datadir}/mc/extfs/rpms
%attr(755,root,root) %{_datadir}/mc/extfs/uzip
%endif
%attr(755,root,root) %{_datadir}/mc/extfs/audio
%attr(755,root,root) %{_datadir}/mc/extfs/bpp
%attr(755,root,root) %{_datadir}/mc/extfs/hp48
%attr(755,root,root) %{_datadir}/mc/extfs/iso9660
%attr(755,root,root) %{_datadir}/mc/extfs/lslR
%attr(755,root,root) %{_datadir}/mc/extfs/rpm
%attr(755,root,root) %{_datadir}/mc/extfs/trpm
%attr(755,root,root) %{_datadir}/mc/extfs/u7z
%attr(755,root,root) %{_datadir}/mc/extfs/ualz
%attr(755,root,root) %{_datadir}/mc/extfs/uar*
%attr(755,root,root) %{_datadir}/mc/extfs/uace
%attr(755,root,root) %{_datadir}/mc/extfs/uc1541
%attr(755,root,root) %{_datadir}/mc/extfs/ucab
%attr(755,root,root) %{_datadir}/mc/extfs/uha
%attr(755,root,root) %{_datadir}/mc/extfs/ulha
%attr(755,root,root) %{_datadir}/mc/extfs/urar
%attr(755,root,root) %{_datadir}/mc/extfs/uzoo
%attr(755,root,root) %{_datadir}/mc/extfs/srpm
%{_desktopdir}/mc.desktop
%{_pixmapsdir}/mc.png

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(sr) %{_mandir}/sr/man1/*

%dir %{_sysconfdir}/mc
%config(noreplace) %verify(not md5 mtime size) /etc/mc/Syntax
%config(noreplace) %verify(not md5 mtime size) /etc/mc/*.*
%dir %{_sysconfdir}/mc/extfs
%config(noreplace) %verify(not md5 mtime size) /etc/mc/extfs/*.*

%files -n mcserv
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*
%attr(754,root,root) /etc/rc.d/init.d/mcserv
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mcserv
%{_mandir}/man8/mcserv.8*
%lang(es) %{_mandir}/es/man8/mcserv.8*
%lang(pl) %{_mandir}/pl/man8/mcserv.8*
%lang(sr) %{_mandir}/sr/man8/mcserv.8*
%attr(755,root,root) %{_sbindir}/mcserv
