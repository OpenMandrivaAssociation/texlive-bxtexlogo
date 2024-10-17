Name:		texlive-bxtexlogo
Version:	63231
Release:	2
Summary:	Additional TeX-family logos
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxtexlogo
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxtexlogo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxtexlogo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hologo package provides many useful logos of popular (and
not so popular) TeX-family software. However, its interface is
a bit cumbersome because you must type \hologo{BibTeX} instead
of \BibTeX. This package makes it possible to import some of
the logos provided by hologo as single commands, such as
\BibTeX. Additionally, the package provides logos of some
TeX-family software that is popular mainly in Japan. These
logos can be imported in the same way as those provided by the
\hologo command. bxtexlogo depends on hologo and cjhebrew (if
\logoAleph and \logoLamed are used).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxtexlogo
%doc %{_texmfdistdir}/doc/latex/bxtexlogo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
