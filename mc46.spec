# TODO: check spec-syntax,pl,mo patches
#
# Conditional build:
%bcond_with	ext2undel	# with ext2 undelete fs
%bcond_without	perl_vfs	# without perl depending vfs'es -- to avoid perl autoreq
%bcond_with	samba		# with SAMBA vfs support
%bcond_without	x		# without text edit in X support
%bcond_without	utf8		# utf8
#
%define	snap	2006-09-25-14
%define ssnap	%(echo %{snap} | tr - .)
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
Version:	4.6.2
Release:	0.%{ssnap}.2
License:	GPL
Group:		Applications/Shells
Source0:	http://www.ibiblio.org/pub/Linux/utils/file/managers/mc/snapshots/%{name}-%{snap}.tar.gz
# Source0-md5:	166770dd758526b2a013a6978a8bb54a
Source1:	%{name}serv.pamd
Source2:	%{name}serv.init
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	17d7b574e1b85ad6f8ddceda9e841f19
Source6:	%{name}serv.sysconfig
Source7:	%{name}.desktop
Source8:	%{name}.png
Patch0:		%{name}-rpmfs.patch
Patch1:		%{name}-spec-syntax.patch
Patch2:		%{name}-urar.patch
Patch3:		%{name}-srpm.patch
Patch4:		%{name}-home_etc2.patch
Patch5:		%{name}-pl.patch
Patch8:		%{name}-mc.ext.patch
Patch9:		%{name}-mo.patch
Patch10:	%{name}-localenames.patch
Patch11:	%{name}-noperl-vfs.patch
# at now syntax highligthing for PLD-update-TODO and CVSROOT/users
Patch12:	%{name}-pld-developerfriendly.patch
# http://www.suse.de/~nadvornik/mc.html
Patch13:	%{name}-utf8.patch
Patch14:	%{name}-vhdl-syntax.patch

Patch17:	%{name}-nolibs.patch
Patch20:	%{name}-uglydir.patch
Patch21:	%{name}-userhost.patch
Patch22:	%{name}-utf8-look-and-feel.patch
Patch23:	%{name}-utf8-8bit-hex.patch
Patch24:	%{name}-bash-3.2.patch
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
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
%if %{with utf8}
BuildRequires:	slang-devel >= 1:2.0.0
%endif
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
Obsoletes:	tkmc
Conflicts:	bash < 2.05b
Conflicts:	rpm < 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
FTP, view tar, zip files, and poke into RPMs for specific files. :-)

%description -l de
Midnight Commander ist ein Visual-Shell, �hnlich einem Dateimanager,
aber mit zus�tzlichen Funktionen. Es l�uft im Textmodus, kann jedoch
eine Maus unterst�tzen, wenn GPM betrieben wird. Seine coolsten
F�higkeiten sind die FTP-Option, das Einsehen von tar- und zip-Dateien
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
Pracuje w trybie tekstowym, ale ma tak�e obs�ug� myszki. Jest super ;)
MC ma wbudowanego klienta FTP, mo�e zagl�da� do skompresowanych
archiw�w tar i zip, a tak�e ogl�da� pliki w pakietach RPM.

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
�al���yorsa fare deste�i vard�r. En ho� �zellikleri FTP yapabilmesi,
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
Requires(post,preun):	/sbin/chkconfig
Requires:	pam >= 0.66
Requires:	portmap
Requires:	rc-scripts

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
%setup -q -a3 -n %{name}-%{snap}
%patch0 -p1
#%patch1 -p1
%patch2 -p1
cp -f vfs/extfs/{rpm,srpm}
%patch3 -p1
# UPDATE ME (home-etc)
#%patch4 -p1
# UPDATE ME (translation)
# %patch5 -p1
%patch8 -p1
# M-o patch
#%patch9 -p1
%patch10 -p1
%{!?with_perl_vfs:%patch11 -p1}
%patch12 -p1
%if %{with utf8}
%patch13 -p1
%endif
%patch14 -p1

%patch17 -p1
%patch20 -p1
%patch21 -p1
%if %{with utf8}
%patch22 -p1
%patch23 -p1
%endif
%patch24 -p2

mv -f po/{no,nb}.po

%if %{with utf8}
# convert files in /lib to UTF-8
cd lib
for i in mc.hint mc.hint.es mc.hint.it mc.hint.nl; do
	iconv -f iso-8859-1 -t utf-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done

for i in mc.hint.cs mc.hint.hu mc.hint.pl; do
	iconv -f iso-8859-2 -t utf-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done

for i in mc.hint.sr mc.menu.sr; do
	iconv -f iso-8859-5 -t utf-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done

iconv -f koi8-r -t utf8 < mc.hint.ru > mc.hint.ru.tmp
mv -f mc.hint.ru.tmp mc.hint.ru
iconv -f koi8-u -t utf8 < mc.hint.uk > mc.hint.uk.tmp
mv -f mc.hint.uk.tmp mc.hint.uk
iconv -f big5 -t utf8 < mc.hint.zh > mc.hint.zh.tmp
mv -f mc.hint.zh.tmp mc.hint.zh
cd ..


# convert man pages in /doc to UTF-8
cd doc

cd ru
for i in mc.1.in xnc.hlp; do
	iconv -f koi8-r -t utf-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done
cd ..

cd sr
for i in mc.1.in mcserv.8.in xnc.hlp; do
	iconv -f iso-8859-5 -t utf-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done
cd ..

for d in es it; do
	for i in mc.1.in xnc.hlp; do
		iconv -f iso-8859-3 -t utf-8 < ${d}/${i} > ${d}/${i}.tmp
		mv -f ${d}/${i}.tmp ${d}/${i}
	done
done

for d in hu pl; do
	for i in mc.1.in xnc.hlp; do
		iconv -f iso-8859-2 -t utf-8 < ${d}/${i} > ${d}/${i}.tmp
		mv -f ${d}/${i}.tmp ${d}/${i}
	done
done
cd ..
%endif

rm -f syntax/Syntax.orig
sed -i 's:|hxx|:|hh|hpp|hxx|:' syntax/Syntax

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

%if %{with utf8}
CFLAGS="-DUTF8 %{rpmcflags}"
export CFLAGS
%endif
%configure \
	--enable-charset \
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
%service mcserv restart "mcserv daemon"

%preun -n mcserv
if [ "$1" = "0" ]; then
	%service mcserv stop
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
%attr(755,root,root) %{_datadir}/mc/extfs/u7z
%attr(755,root,root) %{_datadir}/mc/extfs/ualz
%attr(755,root,root) %{_datadir}/mc/extfs/uar*
%attr(755,root,root) %{_datadir}/mc/extfs/uha
%attr(755,root,root) %{_datadir}/mc/extfs/ulha
%attr(755,root,root) %{_datadir}/mc/extfs/urar
%attr(755,root,root) %{_datadir}/mc/extfs/uzoo
%attr(755,root,root) %{_datadir}/mc/extfs/srpm
%{_desktopdir}/mc.desktop
%{_pixmapsdir}/mc.png

%{_datadir}/mc/mc.charsets

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(sr) %{_mandir}/sr/man1/*

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
