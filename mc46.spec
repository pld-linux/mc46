Summary:	Midnight Commander visual shell
Name:		mc
Version:	4.5.9
Release:	1d
Copyright:	GPL
Group:		Shells
Group(pl):	Pow�oki
#######		ftp://peyote-asesino.nuclecu.unam.mx/linux/local/devel
Source:		%{name}-%{version}.tar.gz
Source1:	mcserv.pam
Source2:	mcserv.init
Patch:		%{name}-profile.patch
URL:		http://mc.blackdown.org/mc/
Requires:	glib >= 1.1.7
BuildRoot:	/tmp/%{name}-%{version}-root
Summary(de):	Visuelle Shell Midnight Commander 
Summary(fr):	Le shell Midnight Commander
Summary(pl):	Midnight Commander - pow�oka wizualna
Summary(tr):	Midnight Commander g�rsel kabu�u

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features.  It is text mode, but also includes mouse support if you are
running GPM.  Its coolest feature is the ability to ftp, view tar, zip
files, and poke into RPMs for specific files.  :-)

%description -l pl
Midnight Commander jest wizualnym shellem podobnym do Norton Commandera.
Pracuje w trybie tekstowym, ale ma tak�e wspomaganie dla myszki. Jest super ;)  
MC ma wbudowanego klienta ftp, mo�e zagl�da� do skompresowanego archiwum 
tarowego, do *.zip oraz *.rpm. Teraz r�wnie� ma wspomaganie dla urz�dze� 
/dev/pts/{0-2048} - standard Unix98.  

%description -l de
Midnight Commander ist ein Visual-Shell, �hnlich einem Dateimanager, 
aber mit zus�tzlichen Funktionen. Es l�uft im Textmodus, kann jedoch 
eine Maus unterst�tzen, wenn GPM betrieben wird. Seine coolsten 
F�higkeiten sind die ftp-Option, das Einsehen von tar- und zip-Dateien 
und das Herausfischen von spezifischen Dateien aus RPMs.   

%description -l fr
Midnight Commander est un shell visuel un peu comme un gestionnaire de
fichiers mais avec plus de possibilit�s. Ceci est la version texte mais
elle int�gre aussi la gestion de la souris si vous ex�cutez gpm.
Sa caract�ristique la plus agr�able est la possibilit� de faire du ftp, de
visualiser les fichiers tar et zip et de parcourir les RPMs pour rechercher
des fichiers pr�cis. :-)

%description -l tr
Midnight Commander bir dosya y�neticisine �ok benzeyen ancak daha yetenekli
bir g�rsel kabuktur. Metin ekranda �al���r ve GPM �al���yorsa fare deste�i
vard�r. En ho� �zellikleri ftp yapabilmesi, tar, zip ve RPM dosyalar�n�n
i�eriklerini g�sterebilmesidir.
 
%package -n mcserv
Summary:	Midnight Commander file server
Group:		X11/Shells
Group(pl):	X11/Pow�oki
Requires:	portmap
Requires:	pam >= 0.66
Prereq:		/sbin/chkconfig
Summary(de):	Midnight Commander File-Server 
Summary(fr):	Serveur de fichier de Midnight Commander
Summary(pl):	Serwer plik�w Midnight Commandera
Summary(tr):	Midnight Commander dosya sunucusu

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
#Requires:	%{name} = %{version}
#Group:		X11/Shells
#Group(pl):	X11/Pow�oki
#Summary(de):	Midnight Commander Visual-Shell (GNOME Version) 
#Summary(fr):	shell visuel Midnight Commander (version GNOME)
#Summary(pl):	Midnight Commander wizualny shell (wersja GNOME)
#Summary(tr):	Midnight Commander g�rsel kabu�u (GNOME s�r�m�)

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
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
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

bzip2 -9 $RPM_BUILD_ROOT/usr/man/{man1/*,man8/*} FAQ NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv

%preun -n mcserv
if [ $1 = 0 ]; then
    /sbin/chkconfig --del mcserv
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
%attr(644,root, man) /usr/man/man8/mcserv.8.bz2
%attr(755,root,root) /usr/sbin/mcserv

#%files -n gmc
#%defattr(644, root, root, 755)
#%attr(755, root, root) /usr/bin/gmc
#/usr/lib/mc/layout
#/usr/share/icons/mc

%changelog
* Wed Jan 20 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
[4.5.9-1d]
- updated to new version,
- fixed files permissions,
- build without GNOME (description commented out) && ext2undel,
- compressed %doc && man pages,
- moved mcserv to /usr/sbin,
- added Requires: glib >= 1.1.7 && pam >= 0.66 (in mcserv sub-package),
- fixed mcserv.pam (now as separate Surce1),
- added Group(pl),
- removed %ifos Linux %attr(4711,root,root) /usr/lib/mc/bin/cons.saver
  (PLD Linux dont't like Solaris ;)
- removed "Conflicts: rpm =< 2.5.3",
- removed "Obsoletes: tkmc"

  by Micha� Zalewski <lcamtuf@dione.ids.pl>

- fixed $TEMPDIR in mc.sh. 

* Mon Nov 2 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
[4.5.1-2d]
- fixed pl translation,
- build against static libcom_err.h
- added pl.po
  (by Arkadiusz Mi�kiewicz <misiek@listar.zsz2.starachowice.pl>).

* Sun Nov 1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- addded "Conflicts: rpm <= 2.5.3" because "rpm -qplv" query output was
  changed.

* Wed Oct 14 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
[4.5.1-1d]
- updated to 4.5.1. 

* Fri Oct 02 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
[4.5.0-1d]
- updated to 4.5.0 

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
- translation modified for pl,
- changed prmissions of mc, mcedit, mcmfmt to 711,
- changed permissions of mcserv to 711.

* Mon Jul 14 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
[4.1.35-2d]
- build against glibc-2.1,
- removed gnome version of mc. 
