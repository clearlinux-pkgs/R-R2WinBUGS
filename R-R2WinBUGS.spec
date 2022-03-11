#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R2WinBUGS
Version  : 2.1.21
Release  : 21
URL      : https://cran.r-project.org/src/contrib/R2WinBUGS_2.1-21.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R2WinBUGS_2.1-21.tar.gz
Summary  : Running 'WinBUGS' and 'OpenBUGS' from 'R' / 'S-PLUS'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-coda
BuildRequires : R-coda
BuildRequires : buildreq-R

%description
results and functions to work with that class.
  Function write.model() allows a 'BUGS' model file to be written.  
  The class and auxiliary functions could be used with other MCMC programs, including 'JAGS'.

%prep
%setup -q -c -n R2WinBUGS
cd %{_builddir}/R2WinBUGS

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641085158

%install
export SOURCE_DATE_EPOCH=1641085158
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2WinBUGS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2WinBUGS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2WinBUGS
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc R2WinBUGS || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R2WinBUGS/CITATION
/usr/lib64/R/library/R2WinBUGS/DESCRIPTION
/usr/lib64/R/library/R2WinBUGS/INDEX
/usr/lib64/R/library/R2WinBUGS/Meta/Rd.rds
/usr/lib64/R/library/R2WinBUGS/Meta/data.rds
/usr/lib64/R/library/R2WinBUGS/Meta/features.rds
/usr/lib64/R/library/R2WinBUGS/Meta/hsearch.rds
/usr/lib64/R/library/R2WinBUGS/Meta/links.rds
/usr/lib64/R/library/R2WinBUGS/Meta/nsInfo.rds
/usr/lib64/R/library/R2WinBUGS/Meta/package.rds
/usr/lib64/R/library/R2WinBUGS/Meta/vignette.rds
/usr/lib64/R/library/R2WinBUGS/NAMESPACE
/usr/lib64/R/library/R2WinBUGS/NEWS
/usr/lib64/R/library/R2WinBUGS/R/R2WinBUGS
/usr/lib64/R/library/R2WinBUGS/R/R2WinBUGS.rdb
/usr/lib64/R/library/R2WinBUGS/R/R2WinBUGS.rdx
/usr/lib64/R/library/R2WinBUGS/data/schools.txt.gz
/usr/lib64/R/library/R2WinBUGS/doc/R2WinBUGS.Rnw
/usr/lib64/R/library/R2WinBUGS/doc/R2WinBUGS.pdf
/usr/lib64/R/library/R2WinBUGS/doc/index.html
/usr/lib64/R/library/R2WinBUGS/help/AnIndex
/usr/lib64/R/library/R2WinBUGS/help/R2WinBUGS.rdb
/usr/lib64/R/library/R2WinBUGS/help/R2WinBUGS.rdx
/usr/lib64/R/library/R2WinBUGS/help/aliases.rds
/usr/lib64/R/library/R2WinBUGS/help/paths.rds
/usr/lib64/R/library/R2WinBUGS/html/00Index.html
/usr/lib64/R/library/R2WinBUGS/html/R.css
/usr/lib64/R/library/R2WinBUGS/model/schools.txt
