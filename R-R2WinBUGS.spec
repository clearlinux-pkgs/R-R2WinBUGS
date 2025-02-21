#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-R2WinBUGS
Version  : 2.1.22.1
Release  : 34
URL      : https://cran.r-project.org/src/contrib/R2WinBUGS_2.1-22.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R2WinBUGS_2.1-22.1.tar.gz
Summary  : Running 'WinBUGS' and 'OpenBUGS' from 'R' / 'S-PLUS'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-coda
BuildRequires : R-coda
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
results and functions to work with that class.
  Function write.model() allows a 'BUGS' model file to be written.  
  The class and auxiliary functions could be used with other MCMC programs, including 'JAGS'.

%prep
%setup -q -n R2WinBUGS
pushd ..
cp -a R2WinBUGS buildavx2
popd
pushd ..
cp -a R2WinBUGS buildavx512
popd
pushd ..
cp -a R2WinBUGS buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740097614

%install
export SOURCE_DATE_EPOCH=1740097614
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
