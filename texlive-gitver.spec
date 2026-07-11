%global tl_name gitver
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Get the current git hash of a project and typeset it in the document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gitver
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitver.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitver.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package will get a description of the current git version of the
document and store it in a command \gitVer. If memoir or fancyhdr are in
use, it will also add this to the document footers unless the option
"noheader" is passed. The package also defines a command \versionBox
which outputs a box containing the version and date of compilation. The
package requires hyperref, catchfile, pdftexcmds, and datetime.

