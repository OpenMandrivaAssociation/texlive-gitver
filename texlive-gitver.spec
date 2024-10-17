Name:		texlive-gitver
Version:	63920
Release:	2
Summary:	Get the current git hash of a project and typeset it in the document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gitver
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitver.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitver.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package will get a description of the current git version
of the document and store it in a command \gitVer. If memoir or
fancyhdr are in use, it will also add this to the document
footers unless the option "noheader" is passed. The package
also defines a command \versionBox which outputs a box
containing the version and date of compilation. The package
requires hyperref, catchfile, pdftexcmds, and datetime.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gitver
%doc %{_texmfdistdir}/doc/latex/gitver

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
