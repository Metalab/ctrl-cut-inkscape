#
# spec file for package ctrl-cut-inkscape (Version 1.0)
#
# Copyright 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (C) 2009-2010 Amir Hassan <amir@viel-zu.org> and Marius Kintel <marius@kintel.net>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Summary: Laser Cutter Software (Epilog Legend 36EXT)
Name: ctrl-cut-inkscape
Version: 1.0
Release: 1
License: GPLv2+
Group: Hardware/Other
URL: https://github.com/Metalab/ctrl-cut-inkscape
Packager: Amir Hassan <amir@viel-zu.org>
BuildRequires: inkscape
Requires: inkscape ctrl-cut
Source:       %{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%description
This is an inkscape plugin which integrates ctrl-cut (a laser cutter toolchain).

# extract source tar ball
%prep
%setup -q

%build
true 

%install
DESTDIR="%{buildroot}"
PREFIX="%{_prefix}"
mkdir -p $DESTDIR/$PREFIX/share/inkscape/extensions/
cp ctrl-cut.inx $DESTDIR/$PREFIX/share/inkscape/extensions/
cp ctrl-cut.py $DESTDIR/$PREFIX/share/inkscape/extensions/

%post
exit 0

%clean
# clean up the hard disc after build
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md LICENSE

%{_prefix}/share/inkscape/extensions/ctrl-cut.inx
%{_prefix}/share/inkscape/extensions/ctrl-cut.py

