Summary:     Midnight Commander visual shell
Summary(de): Visuelle Shell Midnight Commander 
Summary(fr): Le shell Midnight Commander
Summary(pl): Midnight Commander wizualny shell
Summary(tr): Midnight Commander görsel kabuðu
Name:        mc
Version:     4.5.0
Release:     1
Copyright:   GPL
Group:       Shells
Source0:     ftp://peyote-asesino.nuclecu.unam.mx/linux/local/devel/%{name}-%{version}.tar.gz
Patch0:      mc.patch
Patch1:      mc-hotlist.patch
URL:         http://mc.blackdown.org/mc/
Obsoletes:   tkmc
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features. It is text mode, but also includes mouse support if you are
running GPM. Its coolest feature is the ability to ftp, view tar, zip
files, and poke into RPMs for specific files.  :-)

%description -l de
Midnight Commander ist ein Visual-Shell, ähnlich einem Dateimanager, 
aber mit zusätzlichen Funktionen. Es läuft im Textmodus, kann jedoch 
eine Maus unterstützen, wenn GPM betrieben wird. Seine coolsten 
Fähigkeiten sind die ftp-Option, das Einsehen von tar- und zip-Dateien 
und das Herausfischen von spezifischen Dateien aus RPMs.   

%description -l fr
Midnight Commander est un shell visuel un peu comme un gestionnaire de
fichiers mais avec plus de possibilités. Ceci est la version texte mais
elle intègre aussi la gestion de la souris si vous exécutez gpm.
Sa caractéristique la plus agréable est la possibilité de faire du ftp, de
visualiser les fichiers tar et zip et de parcourir les RPMs pour rechercher
des fichiers précis. :-)

%description -l pl
Midnight Commander jest wizualnym shellem podobnym do Nortona Commandera.
Pracuje w trybie tekstowym i mo¿na w trakcie pracy z nim na koncoli czy
pod xtermem wykorzystywaæ myszkê. Mc ma wbudwan± obs³ugê kilku wirtualnych
systemów plikowych jak ftpfs, tarfs, rpmfs i inne, czyli mo¿e on s³u¿yæ
jako klient ftp, a tak¿e z jego pomoc± mo¿na przegl±daæ archwa w ró¿nych
formatach, które to archiwa mo¿na przegl±daæ jak podkatalogi.

%description -l tr
Midnight Commander bir dosya yöneticisine çok benzeyen ancak daha yetenekli
bir görsel kabuktur. Metin ekranda çalýþýr ve GPM çalýþýyorsa fare desteði
vardýr. En hoþ özellikleri ftp yapabilmesi, tar, zip ve RPM dosyalarýnýn
içeriklerini gösterebilmesidir.

%package -n gmc
Summary:     Midnight Commander visual shell (GNOME version)
Summary(de): Midnight Commander Visual-Shell (GNOME Version) 
Summary(fr): shell visuel Midnight Commander (version GNOME)
Summary(pl): Midnight Commander wizualny shell (wersja GNOME)
Summary(tr): Midnight Commander görsel kabuðu (GNOME sürümü)
Requires:    %{name} = %{version}
Obsoletes:   tkmc
Group:       X11/Shells

%description -n gmc
Midnight Commander is a visual shell much like a file manager, only with
way more features.  This is the GNOME version. It's coolest feature is the
ability to ftp, view tar, zip files and poke into RPMs for specific files.
The GNOME version of Midnight Commander is not yet finished though. :-(
 
%package -n mcserv
Summary:     Midnight Commander file server
Summary(de): Midnight Commander File-Server 
Summary(fr): Serveur de fichier de Midnight Commander
Summary(pl): Serwer plików Midnight Commander'a
Summary(tr): Midnight Commander dosya sunucusu
Group:       X11/Shells
Requires:    portmap, pam >= 0.64
Prereq:      /sbin/chkconfig

%description -n mcserv
mcserv is the server program for the Midnight Commander networking file
system. It provides access to the host file system to clients running the
Midnight file system (currently, only the Midnight Commander file manager).

%description -l de -n mcserv
mcserv ist das Server-Programm für das Netzwerkdateisystem Midnight Commander.
Es ermöglicht den Zugriff auf das Host-Dateisystem für Clients, die das
Midnight-Dateisystem ausführen (z.Zt. nur Midnight Commander file manager).

%description -l fr -n mcserv
mcserv est un programme pour les système de fichiers réseau de
Midnight Commander. Il fournit un accès au systéme de fichiers de l'hôte
aux clients sur lesquelles tourne le systéme de fichiers Midnight
(actuellement, Midnight Commander est le seul).

%description -l pl -n mcserv
Mcserv jest aplikacj± dla sieciowego systemy plików Midnight Commander'a.
Pozwala na dostêp do systemu plików dla klienta pracuj±cego pod MC i 
u¿ywaj±cego jego systemu plików.

%description -l tr -n mcserv
mcserv, Midnight Commander að dosya sisteminin sunucu programýdýr. Midnight
dosya sistemini çalýþtýran istemcilerin sunucu dosya sistemine eriþimini
saðlar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure \
	--prefix=/usr \
	--with-gnome \
	--without-debug

# it is temporary hack for building mc on system with slang 1.2.x
rm slang/slang.h

make
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,profile.d,X11/wmconfig}

make prefix=$RPM_BUILD_ROOT/usr install
(cd icons; make prefix=$RPM_BUILD_ROOT/usr install_icons)
install lib/mcserv.init $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

install lib/mcserv.pamd $RPM_BUILD_ROOT/etc/pam.d/mcserv
install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n mcserv
/sbin/chkconfig --add mcserv

%postun -n mcserv
/sbin/chkconfig --del mcserv

%files
%defattr(644, root, root, 755)
%doc FAQ NEWS README
%attr(755, root, root) /usr/bin/mc
%attr(755, root, root) /usr/bin/mcedit
%attr(755, root, root) /usr/bin/mcmfmt
/usr/lib/mc/mc.ext
/usr/lib/mc/mc.hint
/usr/lib/mc/mc.hlp
/usr/lib/mc/mc.lib
/usr/lib/mc/mc.menu
%ifos Linux
%attr(4755, root, root) /usr/lib/mc/bin/cons.saver
%endif
%attr(755, root, root) /usr/lib/mc/extfs
%attr(644, root,  man) /usr/man/man1/*
%attr(755, root, root) %config /etc/profile.d/*
%dir /usr/lib/mc
%dir /usr/lib/mc/bin
%lang(es) /usr/share/locale/es/LC_MESSAGES/mc.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/mc.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/mc.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/mc.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/mc.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/mc.mo

%files -n mcserv
%defattr(644, root, root)
%config(noreplace) /etc/pam.d/mcserv
%config /etc/rc.d/init.d/mcserv
%attr(644, root,  man) /usr/man/man8/mcserv.8
%attr(755, root, root) /usr/bin/mcserv

%files -n gmc
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/gmc
/usr/lib/mc/layout
/usr/share/icons/mc

%changelog
* Wed Aug 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.35-3]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added patch with pl translation,
- added pl translation for mc, mcserv (Wojtek ¦lusarczyk
  <wojtek@shadow.eu.org>),
- added using %%{name} macro in Buildroot and Source,
- added /usr/share/locale/*/LC_MESSAGES/mc.mo with %lang macros to mc
  package,
- added patch which fix support for all languages,
- added "Obsoletes: tkmc" for mc and gmc,
- added "%ifos Linux .. %endif" for /usr/lib/mc/bin/cons.saver (it
  neccessary for egzample for building on Solaris),
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

* Sun Oct 26 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

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

* Tue May 13 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added new rpmfs script,
- removed mcfn_install from mc (adding mc() to bash enviroment is in
  /etc/profile.d/mc.sh),
- /etc/profile.d/mc.sh changed to %config,
- removed /usr/lib/mc/bin/create_vcs,
- removed /usr/lib/mc/term.

* Wed May 9 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- changed source url,
- fixed link mcedit to mc,

* Tue May 7 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- new version 3.5.27,
- %dir /usr/lib/mc/icons and icons removed from tkmc,
- added commented xmc part.

* Tue Apr 22 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- FIX spec:
   - added URL field,
   - in mc added missing /usr/lib/mc/mc.ext, /usr/lib/mc/mc.hint,
     /usr/lib/mc/mc.hlp, /usr/lib/mc/mc.lib, /usr/lib/mc/mc.menu.

* Fri Apr 18 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added making packages: tkmc, mcserv (xmc not work yet),
- gziped man pages,
- added /etc/pamd.d/mcserv PAM config file.
- added instaling icons,
- added /etc/profile.d/mc.sh,
- in %doc added NEWS README,
- removed /usr/lib/mc/FAQ,
- added mcserv.init script for mcserv (start/stop on level 86).
