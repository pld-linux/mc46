#
# Conditional build:
%bcond_with	ext2undel	# with ext2 undelete fs
%bcond_without	perl_vfs	# without perl depending vfs'es -- to avoid perl autoreq
%bcond_with	samba		# with SAMBA vfs support
%bcond_without	x		# without text edit in X support
%bcond_with	utf8		# for now it's bcond (broken), in future include by DEFAULT (after updating patches)
#
Summary:	A user-friendly file manager and visual shell
Summary(de):	Visuelle Shell Midnight Commander
Summary(es):	Interpretador de comandos visual Midnight Commander
Summary(fr):	Un gestionnaire de fichiers puissant et agr�able en mode console
Summary(ja):	�Ȥ��䤹���ե�����ޥ͡�����ȥӥ��奢�륷����
Summary(pl):	Midnight Commander - pow�oka wizualna
Summary(pt_BR):	Interpretador de comandos visual Midnight Commander
Summary(ru):	��������� ������ Midnight Commander
Summary(tr):	Midnight Commander g�rsel kabu�u
Summary(uk):	��������� ���̦� Midnight Commander
Summary(zh_CN):	һ������ʵ�õ��ļ�������������Shell
Name:		mc
%define	pre	pre1
Version:	4.6.1
Release:	0.1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.ibiblio.org/pub/Linux/utils/file/managers/mc/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	8c66f5eeb623b20791b3a13bbe6f8c1b
Source1:	%{name}serv.pamd
Source2:	%{name}serv.init
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	17d7b574e1b85ad6f8ddceda9e841f19
# Changelogs for Advanced Midnight Commander patches
Source4:	http://www1.mplayerhq.hu/~arpi/amc/amc-1.txt
# NoSource4-md5:	bcf001d40a63f15848a3763cf5e29f6d
Source5:	http://www1.mplayerhq.hu/~arpi/amc/amc-2.txt
# NoSource5-md5:	4f69a9856931d562fb5f942a8093e577
Source6:	%{name}serv.sysconfig
Source7:	%{name}.desktop
Source8:	%{name}.png
Patch0:		%{name}-rpmfs.patch
Patch1:		%{name}-spec-syntax.patch
Patch2:		%{name}-urar.patch
Patch3:		%{name}-srpm.patch
Patch4:		%{name}-home_etc2.patch
Patch5:		%{name}-pl.patch
# Advanced Midnight Commander patches
Patch6:		http://www1.mplayerhq.hu/~arpi/amc/amc-1.diff
#changed from:	http://www1.mplayerhq.hu/~arpi/amc/amc-2.diff
Patch7:		amc-2.diff
Patch9:		%{name}-mc.ext.patch
Patch12:	%{name}-mo.patch
Patch13:	%{name}-posix.patch
Patch15:	%{name}-tempfile.patch
Patch16:	%{name}-localenames.patch
Patch17:	%{name}-noperl-vfs.patch
# at now syntax highligthing for PLD-update-TODO and CVSROOT/users
Patch18:	%{name}-pld-developerfriendly.patch
# http://www.suse.de/~nadvornik/mc.html
Patch19:	%{name}-4.6.0-utf8.patch
Patch20:	%{name}-4.6.0-utf8-input.patch
Patch21:	%{name}-4.6.0-utf8-fix.patch
Patch22:	%{name}-4.6.0-utf8-hints.patch
URL:		http://www.ibiblio.org/mc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	indent
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
%if %{with utf8}
BuildRequires:	slang-devel >= 1:1.4.9-6
%endif
%ifnarch s390 s390x
BuildRequires:	gpm-devel
%endif
%{?with_ext2undel:BuildRequires:	e2fsprogs-devel}
%{?with_x:BuildRequires:	XFree86-devel}
Requires:	file
Requires:	pam >= 0.77.3
Requires:	setup >= 2.4.6-2
# Needed? %%{?with_perl_vfs:Requires:	perl-base}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	tkmc
Conflicts:	rpm < 4.0

%define		specflags_ia32	"-fomit-frame-pointer"

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

%description -l es
Midnight Commander es un interpretador de comandos visual que m�s
parece un administrador de archivos, solamente con varias
caracter�sticas a m�s. Es un programa en modo texto, pero incluye
soporte para rat�n, si estuviera ejecutando GPM o en una ventana
xterm. Su caracter�stica m�s genial es la habilidad de cotillear en
RPMs buscando archivos espec�ficos. :-)

%description -l fr
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Il fonctionne en mode console (texte), mais peut �tre
contr�l� � la souris si GPM est pr�sent. Ses caract�ristiques les plus
remarquables sont la possibilit� de se connecter � un serveur FTP, de
visualiser des archives tar, de compresser des fichiers avec zip, de
r�cup�rer des fichiers dans les packages RPM, et tout ceci simplement.

%description -l ja
Midnight Commander �Ϥ��������ʵ�ǽ����ä��ե�����ޥ͡������
�ӥ��奢�륷����Ǥ�������ϥƥ����ȥ⡼�ɤΥ��ץꥱ�������Ǥ�����
GPM ��ȤäƤ����硢�ޥ������Ȥ��ޤ��� Midnight Commander �ˤϡ� FTP
����³�Ǥ����ꡢ tar �� zip �� RPM ���椬������ʤɡ�������ʵ�ǽ
������ޤ���

%description -l pl
Midnight Commander jest wizualn� pow�ok� podobn� do Norton Commandera.
Pracuje w trybie tekstowym, ale ma tak�e wspomaganie dla myszki. Jest
super ;) MC ma wbudowanego klienta ftp, mo�e zagl�da� do
skompresowanego archiwum tarowego, do *.zip oraz *.rpm. Teraz r�wnie�
pracuje z urz�dzeniami /dev/pts/{0-2048} - standard Unix98.

%description -l pt_BR
Midnight Commander � um interpretador de comandos visual que mais
parece um gerenciador de arquivos, somente com v�rias caracter�sticas
a mais. Ele � um programa de modo texto, mas inclui suporte para mouse
se voc� estiver rodando GPM ou em uma janela xterm. Sua caracter�stica
mais legal � a habilidade de bisbilhotar em RPMs procurando arquivos
espec�ficos. :-)

%description -l tr
Midnight Commander bir dosya y�neticisine �ok benzeyen ancak daha
yetenekli bir g�rsel kabuktur. Metin ekranda �al���r ve GPM
�al���yorsa fare deste�i vard�r. En ho� �zellikleri ftp yapabilmesi,
tar, zip ve RPM dosyalar�n�n i�eriklerini g�sterebilmesidir.

%package -n mcserv
Summary:	Server for the Midnight Commander network file management system
Summary(de):	Midnight Commander File-Server
Summary(es):	Servidor de archivos del Midnight Commander
Summary(fr):	Serveur r�seau pour le gestionnaire de fichiers Midnight Commander
Summary(ja):	Midnight Commander �ǥͥåȥ���ե�����ޥ͡������Ȥ�Ԥ�������
Summary(pl):	Serwer plik�w Midnight Commandera
Summary(pt_BR):	Servidor de arquivos do Midnight Commander
Summary(ru):	Midnight Commander ����-������
Summary(tr):	Midnight Commander dosya sunucusu
Summary(uk):	Midnight Commander ����-������
Summary(zh_CN):	mc �����ļ�����ϵͳ�ķ�������
Group:		Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
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

%description -n mcserv -l es
Mcserv es un servidor para el sistema de archivos en red del Midnight
Commander. Permite que clientes usando el mc accedan remotamente al
sistema de archivos de la m�quina en que est� ejecutando.

%description -n mcserv -l fr
Le syst�me de gestion de fichier Midnight Commander vous permet de
manipuler des fichiers sur une machine distante comme si ils �taient
sur votre propre machine. Ceci est possible seulement si la machine
distante poss�de le programme mcserv et que celui-ci est activ�.
Mcserv apporte aux machines clientes qui font tourner Midnight
Commander un acc�s aux fichiers situ�s sur l'h�te.

%description -n mcserv -l ja
Midnight Commander
�Υե�������������ƥ�ϡ���⡼�ȥޥ���ˤ���ե������
��������ˤ��뤫�Τ褦�˰������Ȥ��Ǥ��ޤ������ε�ǽ�� mcserv
�ץ������� �¹Ԥ��Ƥ����⡼�ȥޥ�����Ф��ƤΤ�Ư���ޤ��� Mcserv
�� Midnight Commander
���饤����Ȥ��Ф��ơ����Υۥ��ȤΥե����륷���ƥ���󶡤��ޤ���

%description -n mcserv -l pl
Mcserv jest aplikacj� dla sieciowego systemu plik�w Midnight
Commandera. Pozwala na dost�p do systemu plik�w dla klienta
pracuj�cego pod MC i u�ywaj�cego jego systemu plik�w.

%description -n mcserv -l pt_BR
Mcserv � um servidor para o sistema de arquivos em rede do Midnight
Commander. Ele permite que clientes usando o mc acessem remotamente o
sistema de arquivos da m�quina em que est� rodando.

%description -n mcserv -l ru
mcserv - ��� ��������� ��������� ��� ������� �������� ������� Midnight
Commander. ��� ������������ ������ � ��������� �������� �������
��������, �������������� �������� ������� Midnight Commander (�
��������� ����� ������ ���������� Midnight Commander).

%description -n mcserv -l tr
mcserv, Midnight Commander a� dosya sisteminin sunucu program�d�r.
Midnight dosya sistemini �al��t�ran istemcilerin sunucu dosya
sistemine eri�imini sa�lar.

%description -n mcserv -l uk
mcserv - �� �������� �������� ��� �������ϧ ������ϧ ������� Midnight
Commander. ���� ��������դ ������ �� צ������ϧ ������ϧ �������
�̦�����, �� Ц��������� ������� ������� Midnight Commander (����ڦ
Ԧ���� ������ Midnight Commander).

%prep
%setup -q -n %{name}-%{version}-%{pre} -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -f vfs/extfs/{rpm,srpm}
%patch3 -p1
%patch4 -p1
%patch5 -p1
# FIXME
#%patch6 -p1
%patch7 -p1
%patch9 -p1
# FIXME
#%patch12 -p1
%patch13 -p1
%patch15 -p0
%patch16 -p1
%{!?with_perl_vfs:%patch17 -p1}
%patch18 -p1
%if %{with utf8}
%patch19 -p1
%patch20 -p0
%patch21 -p1
%patch22 -p1
%endif

mv -f po/{no,nb}.po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
X11_WWW="
if [ -f /usr/bin/netscape ]; then
	netscape;
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
	--with%{!?debug:out}-debug \
	--with%{!?with_ext2undel:out}-ext2undel \
	--with%{!?with_x:out}-x \
	--with-vfs \
	--with-mcfs \
	%{?with_samba:--with-samba} \
	--with-configdir=/etc/samba \
	--with-codepagedir=/etc/samba/codepages \
	--with-gpm-mouse \
	--with-screen=%{?!with_utf8:mc}slang \
	--with-edit

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_pixmapsdir},%{_desktopdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,shrc.d,sysconfig} \
	$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/mcserv.8 $RPM_BUILD_ROOT%{_mandir}/man8

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

install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/shrc.d

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
%doc FAQ NEWS README
%attr(755,root,root) %{_bindir}/mc*
%config /etc/shrc.d/*
%attr(755,root,root) %{_libdir}/mc/cons.saver
%dir %{_libdir}/mc

%dir %{_datadir}/mc

%{_datadir}/mc/bin
%{_datadir}/mc/syntax

%{_datadir}/mc/mc.ext
%{_datadir}/mc/cedit*
%{_datadir}/mc/edit.*
%{_datadir}/mc/mc.hlp
%lang(es) %{_datadir}/mc/mc.hlp.es
%lang(hu) %{_datadir}/mc/mc.hlp.hu
%lang(it) %{_datadir}/mc/mc.hlp.it
%lang(pl) %{_datadir}/mc/mc.hlp.pl
%lang(ru) %{_datadir}/mc/mc.hlp.ru
%lang(sr) %{_datadir}/mc/mc.hlp.sr
%{_datadir}/mc/mc.lib
%{_datadir}/mc/mc.menu
%lang(sr) %{_datadir}/mc/mc.menu.sr
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
%{_datadir}/mc/extfs/extfs.ini
%{_datadir}/mc/extfs/sfs.ini
%if %{with perl_vfs}
%attr(755,root,root) %{_datadir}/mc/extfs/a
%attr(755,root,root) %{_datadir}/mc/extfs/apt
%attr(755,root,root) %{_datadir}/mc/extfs/deb*
%attr(755,root,root) %{_datadir}/mc/extfs/dpkg
#%attr(755,root,root) %{_datadir}/mc/extfs/ftplist
%attr(755,root,root) %{_datadir}/mc/extfs/mailfs
%attr(755,root,root) %{_datadir}/mc/extfs/patchfs
%attr(755,root,root) %{_datadir}/mc/extfs/rpms
#%attr(755,root,root) %{_datadir}/mc/extfs/ucpio
%attr(755,root,root) %{_datadir}/mc/extfs/uzip
%endif
%attr(755,root,root) %{_datadir}/mc/extfs/audio
%attr(755,root,root) %{_datadir}/mc/extfs/bpp
%attr(755,root,root) %{_datadir}/mc/extfs/hp48
%attr(755,root,root) %{_datadir}/mc/extfs/iso9660
%attr(755,root,root) %{_datadir}/mc/extfs/lslR
%attr(755,root,root) %{_datadir}/mc/extfs/rpm
%attr(755,root,root) %{_datadir}/mc/extfs/trpm
%attr(755,root,root) %{_datadir}/mc/extfs/uar*
%attr(755,root,root) %{_datadir}/mc/extfs/uha
%attr(755,root,root) %{_datadir}/mc/extfs/ulha
%attr(755,root,root) %{_datadir}/mc/extfs/urar
%attr(755,root,root) %{_datadir}/mc/extfs/uesp
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

%files -n mcserv
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/*

%attr(754,root,root) /etc/rc.d/init.d/mcserv
%attr(644,root,root) %config /etc/sysconfig/mcserv
%{_mandir}/man8/mcserv.8*
%lang(es) %{_mandir}/es/man8/mcserv.8*
%lang(pl) %{_mandir}/pl/man8/mcserv.8*
%lang(sr) %{_mandir}/sr/man8/mcserv.8*
%attr(755,root,root) %{_sbindir}/mcserv
