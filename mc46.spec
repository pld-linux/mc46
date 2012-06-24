Summary:	Midnight Commander visual shell
Summary(de):	Visuelle Shell Midnight Commander 
Summary(fr):	Le shell Midnight Commander
Summary(pl):	Midnight Commander - pow�oka wizualna
Summary(tr):	Midnight Commander g�rsel kabu�u
Name:		mc
Version:	4.5.9
Release:	1d
Copyright:	GPL
Group:		Shells
Group(pl):	Pow�oki
#######		ftp://peyote-asesino.nuclecu.unam.mx/linux/local/devel
Source0:	%{name}-%{version}.tar.gz
Source1:	mcserv.pamd
Source2:	mcserv.init
Patch0:		mc-profile.patch
URL:		http://mc.blackdown.org/mc/
Requires:	glib = 1.1.7
BuildRoot:	/tmp/%{name}-%{version}-root
Conflicts:	rpm =< 2.5.3
Obsoletes:	tkmc

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
Midnight Commander est un shell visuel un peu comme un gestionnaire de
fichiers mais avec plus de possibilit�s. Ceci est la version texte mais elle
int�gre aussi la gestion de la souris si vous ex�cutez gpm. Sa
caract�ristique la plus agr�able est la possibilit� de faire du ftp, de
visualiser les fichiers tar et zip et de parcourir les RPMs pour rechercher
des fichiers pr�cis. :-)

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
Summary:	Midnight Commander file server
Summary(de):	Midnight Commander File-Server 
Summary(fr):	Serveur de fichier de Midnight Commander
Summary(pl):	Serwer plik�w Midnight Commandera
Summary(tr):	Midnight Commander dosya sunucusu
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		/sbin/chkconfig
Requires:	portmap
Requires:	pam >= 0.66

%description -n mcserv
mcserv is the server program for the Midnight Commander networking file
system. It provides access to the host file system to clients running the
Midnight file system (currently, only the Midnight Commander file manager).

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l pl -n mcserv
Mcserv jest aplikacj� dla sieciowego systemy plik�w Midnight Commandera.
Pozwala na dost�p do systemu plik�w dla klienta pracuj�cego pod MC i 
u�ywaj�cego jego systemu plik�w.

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l fr -n mcserv
mcserv est un programme pour les syst�me de fichiers r�seau de
Midnight Commander. Il fournit un acc�s au syst�me de fichiers de l'h�te
aux clients sur lesquelles tourne le syst�me de fichiers Midnight
(actuellement, Midnight Commander est le seul).

%description -l tr -n mcserv
mcserv, Midnight Commander a� dosya sisteminin sunucu program�d�r. Midnight
dosya sistemini �al��t�ran istemcilerin sunucu dosya sistemine eri�imini
sa�lar.

#%package -n gmc
#Summary:	Midnight Commander visual shell (GNOME version)
#Summary(de):	Midnight Commander Visual-Shell (GNOME Version) 
#Summary(fr):	shell visuel Midnight Commander (version GNOME)
#Summary(pl):	Midnight Commander wizualny shell (wersja GNOME)
#Summary(tr):	Midnight Commander g�rsel kabu�u (GNOME s�r�m�)
#Group:		X11/Shells
#Group(pl):	X11/Pow�oki
#Requires:	%{name} = %{version}

#%description -n gmc
#Midnight Commander is a visual shell much like a file manager, only with
#way more features.  This is the GNOME version. It's coolest feature is the
#ability to ftp, view tar, zip files and poke into RPMs for specific files.
#The GNOME version of Midnight Commander is not yet finished though. :-(

%prep
%setup -q
%patch -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--without-gnome \
	--without-gnome-libs \
	--without-gnome-includes \
	--with-slang \
	--with-included-slang \
	--without-ext2undel \
	--with-netrc \
	--with-x \
	--without-debug
make  		    

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/sbin,etc/{rc.d/init.d,pam.d,profile.d}}

make prefix=$RPM_BUILD_ROOT/usr install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/profile.d

mv $RPM_BUILD_ROOT/usr/bin/mcserv $RPM_BUILD_ROOT/usr/sbin 

gzip -9nf $RPM_BUILD_ROOT/usr/man/{man1/*,man8/*} FAQ NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv
if test -r /var/run/mcserv.pid; then
	/etc/rc.d/init.d/mcserv stop >&2
	/etc/rc.d/init.d/mcserv start >&2
else
	echo "Run \"/etc/rc.d/init.d/mcserv start\" to start mcserv daemon."
fi

%preun -n mcserv
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del mcserv
	/etc/rc.d/init.d/mcserv stop >&2
fi

%files
%defattr(644,root,root,755)
%doc FAQ.bz2 NEWS.bz2 README.bz2

%attr(755,root,root) /usr/bin/mc
%attr(755,root,root) /usr/bin/mcedit
%attr(755,root,root) /usr/bin/mcmfmt

/usr/lib/mc/mc.ext
/usr/lib/mc/mc.hint
/usr/lib/mc/mc.hlp
/usr/lib/mc/mc.lib
/usr/lib/mc/mc.menu

%attr(755,root,root) /usr/lib/mc/bin/cons.saver

%attr(755,root,root) /usr/lib/mc/extfs/a
%attr(755,root,root) /usr/lib/mc/extfs/deb
%attr(644,root,root) /usr/lib/mc/extfs/extfs.ini
%attr(755,root,root) /usr/lib/mc/extfs/ftplist
%attr(755,root,root) /usr/lib/mc/extfs/hp48
%attr(755,root,root) /usr/lib/mc/extfs/lslR
%attr(755,root,root) /usr/lib/mc/extfs/mailfs
%attr(755,root,root) /usr/lib/mc/extfs/patchfs
%attr(755,root,root) /usr/lib/mc/extfs/rpm
%attr(644,root,root) /usr/lib/mc/extfs/sfs.ini
%attr(755,root,root) /usr/lib/mc/extfs/uar
%attr(755,root,root) /usr/lib/mc/extfs/ucpio
%attr(755,root,root) /usr/lib/mc/extfs/ulha
%attr(755,root,root) /usr/lib/mc/extfs/urar
%attr(755,root,root) /usr/lib/mc/extfs/uzip
%attr(755,root,root) /usr/lib/mc/extfs/uzoo

%attr(644,root, man) /usr/man/man1/*
%attr(755,root,root) %config /etc/profile.d/*

%dir /usr/lib/mc
%dir /usr/lib/mc/bin
%dir /usr/lib/mc/extfs

%lang(de) /usr/share/locale/de/LC_MESSAGES/mc.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/mc.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/mc.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/mc.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/mc.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/mc.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/mc.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/mc.mo

%files -n mcserv
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/*

%attr(700,root,root) %config /etc/rc.d/init.d/mcserv
%attr(644,root, man) /usr/man/man8/mcserv.8.gz
%attr(755,root,root) /usr/sbin/mcserv

#%files -n gmc
#%defattr(644, root, root, 755)
#%attr(755, root, root) /usr/bin/gmc
#/usr/lib/mc/layout
#/usr/share/icons/mc

%changelog
* Thu Jan 21 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.5.9-2d]
- fixed Requires (glib = 1.1.7).
- modifications %post, %preun for standarizing this section; this allow stop
  service on uninstall and automatic restart on upgrade,
- fixed Group in mcserv.

* Wed Jan 20 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [4.5.9-1d]
- updated to new version,
- build without GNOME (description commented out) && ext2undel,
- compressed %doc && man pages,
- moved mcserv to /usr/sbin,
- added Requires: glib >= 1.1.7 && pam >= 0.66 (in mcserv sub-package),
- fixed mcserv.pamd (now as separate Surce1),
- added Group(pl),
- removed %ifos Linux %attr(4711,root,root) /usr/lib/mc/bin/cons.saver
  (PLD Linux dont't like Solaris ;),
- fixed $TEMPDIR in mc.sh (by Micha� Zalewski <lcamtuf@dione.ids.pl>)

* Mon Nov 2 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [4.5.1-2d]
- fixed pl translation,
- build against static libcom_err.h
- added pl.po
  (by Arkadiusz Mi�kiewicz <misiek@listar.zsz2.starachowice.pl>).

* Sun Nov 1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- addded "Conflicts: rpm <= 2.5.3" because "rpm -qplv" query output was
  changed.

* Wed Aug 26 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.35-3]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added patch with pl translation,
- added pl translation for mc, mcserv (Wojtek �lusarczyk
  <wojtek@shadow.eu.org>),
- added using %%{name} macro in Buildroot and Source,
- added /usr/share/locale/*/LC_MESSAGES/mc.mo with %lang macros to mc
  package,
- added patch which fix support for all languages,
- added "Obsoletes: tkmc" for mc and gmc,
- added "%ifos Linux .. %endif" for /usr/lib/mc/bin/cons.saver (it
  neccessary for example for building on Solaris),
- fixed dependences: "Requires: pam" and "Prereq: /sbin/chkconfig" moved
  from mc to mcserv,
- added full %attr description in %files,
- added suid root on /usr/lib/mc/bin/cons.saver,
- removed linking mcserv with not neccesary libs (XLib and term),
- removed COPING from %doc (copyright statment is in Copyright field).

* Fri Jul 31 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [4.1.35-3d]
- build against libslang.so.1,
- translation modified for pl.

* Mon Jul 14 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [4.1.35-2d]
- build against glibc-2.1,
- removed gnome version of mc.

* Wed Aug 26 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.35-3]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added patch with pl translation,
- added pl translation for mc, mcserv (Wojtek �lusarczyk
  <wojtek@shadow.eu.org>),
- added using %%{name} macro in Buildroot and Source,
- added /usr/share/locale/*/LC_MESSAGES/mc.mo with %lang macros to mc
  package,
- added patch which fix support for all languages,
- added "Obsoletes: tkmc" for mc and gmc,
- added "%ifos Linux .. %endif" for /usr/lib/mc/bin/cons.saver (it
  neccessary for example for building on Solaris),
- fixed dependences: "Requires: pam" and "Prereq: /sbin/chkconfig" moved
  from mc to mcserv,
- added full %attr description in %files,
- added suid root on /usr/lib/mc/bin/cons.saver,
- removed linking mcserv with not neccesary libs (XLib and term),
- removed COPING from %doc (copyright statment is in Copyright field).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 4.1.33 to fix extfs problems

* Mon May 04 1998 Michael K. Johnson <johnsonm@redhat.com>
- upgraded to 4.1.32
- enhanced init script

* Mon Apr 20 1998 Erik Troan <ewt@redhat.com>
- built against newer ncurses

* Thu Oct 30 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added dependency on portmap

* Wed Oct 29 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed spec file.
- Updated to 4.1.8

* Sun Oct 26 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>

- updated to 4.1.6
- added %attr macros in %files,
- a few simplification in %install,
- removed glibc patch,
- fixed installing /etc/X11/wmconfig/tkmc.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- updated to 4.1.5
- added wmconfig

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- chkconfig is for mcserv package, not mc one

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>
- patched init script for chkconfig
- don't turn on the service by default

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Converted to new PAM conventions.
- Updated to 4.1.3
- No longer needs glibc patch.

* Thu May 22 1997 Michele Marziani <marziani@fe.infn.it>
- added support for mc alias in /etc/profile.d/mc.csh (for csh and tcsh)
- lowered number of SysV init scripts in /etc/rc.d/rc[0,1,6].d
  (mcserv needs to be killed before inet)
- removed all references to $RPM_SOURCE_DIR
- restored $RPM_OPT_FLAGS when compiling
- minor cleanup of spec file: redundant directives and comments removed

* Sun May 18 1997 Michele Marziani <marziani@fe.infn.it>
- removed all references to non-existent mc.rpmfs
- added mcedit.1 to the %files section
- reverted to un-gzipped man pages (RedHat style)
- removed double install line for mcserv.pamd

* Tue May 13 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added new rpmfs script,
- removed mcfn_install from mc (adding mc() to bash enviroment is in
  /etc/profile.d/mc.sh),
- /etc/profile.d/mc.sh changed to %config,
- removed /usr/lib/mc/bin/create_vcs,
- removed /usr/lib/mc/term.

* Wed May 9 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- changed source url,
- fixed link mcedit to mc,

* Tue May 7 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- new version 3.5.27,
- %dir /usr/lib/mc/icons and icons removed from tkmc,
- added commented xmc part.

* Tue Apr 22 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- FIX spec:
  -- added URL field,
  -- in mc added missing /usr/lib/mc/mc.ext, /usr/lib/mc/mc.hint,
     /usr/lib/mc/mc.hlp, /usr/lib/mc/mc.lib, /usr/lib/mc/mc.menu.

* Fri Apr 18 1997 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added making packages: tkmc, mcserv (xmc not work yet),
- gziped man pages,
- added /etc/pamd.d/mcserv PAM config file.
- added instaling icons,
- added /etc/profile.d/mc.sh,
- in %doc added NEWS README,
- removed /usr/lib/mc/FAQ,
- added mcserv.init script for mcserv (start/stop on level 86).
