#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fst
Version  : 0.9.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/fst_0.9.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fst_0.9.0.tar.gz
Summary  : Lightning Fast Serialization of Data Frames for R
Group    : Development/Tools
License  : AGPL-3.0 BSD-3-Clause GPL-2.0
Requires: R-fst-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-bit64
BuildRequires : R-Rcpp
BuildRequires : R-bit64
BuildRequires : R-data.table
BuildRequires : R-lintr
BuildRequires : buildreq-R
BuildRequires : buildreq-cmake
BuildRequires : util-linux

%description
'fst' format. The 'fst' format allows for random access of stored data and
    compression with the LZ4 and ZSTD compressors created by Yann Collet. The ZSTD
    compression library is owned by Facebook Inc.

%package lib
Summary: lib components for the R-fst package.
Group: Libraries

%description lib
lib components for the R-fst package.


%prep
%setup -q -c -n fst

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571834172

%install
export SOURCE_DATE_EPOCH=1571834172
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fst
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fst
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fst
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fst || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fst/DESCRIPTION
/usr/lib64/R/library/fst/INDEX
/usr/lib64/R/library/fst/LICENSE
/usr/lib64/R/library/fst/Meta/Rd.rds
/usr/lib64/R/library/fst/Meta/features.rds
/usr/lib64/R/library/fst/Meta/hsearch.rds
/usr/lib64/R/library/fst/Meta/links.rds
/usr/lib64/R/library/fst/Meta/nsInfo.rds
/usr/lib64/R/library/fst/Meta/package.rds
/usr/lib64/R/library/fst/NAMESPACE
/usr/lib64/R/library/fst/R/fst
/usr/lib64/R/library/fst/R/fst.rdb
/usr/lib64/R/library/fst/R/fst.rdx
/usr/lib64/R/library/fst/help/AnIndex
/usr/lib64/R/library/fst/help/aliases.rds
/usr/lib64/R/library/fst/help/fst.rdb
/usr/lib64/R/library/fst/help/fst.rdx
/usr/lib64/R/library/fst/help/paths.rds
/usr/lib64/R/library/fst/html/00Index.html
/usr/lib64/R/library/fst/html/R.css
/usr/lib64/R/library/fst/tests/testthat.R
/usr/lib64/R/library/fst/tests/testthat/FactorStore/data1.fst
/usr/lib64/R/library/fst/tests/testthat/datasets/legacy.fst
/usr/lib64/R/library/fst/tests/testthat/datasets/legacy.rds
/usr/lib64/R/library/fst/tests/testthat/datasets/utf8.csv
/usr/lib64/R/library/fst/tests/testthat/helper_fstwrite.R
/usr/lib64/R/library/fst/tests/testthat/keyedTable.rds
/usr/lib64/R/library/fst/tests/testthat/test_access.R
/usr/lib64/R/library/fst/tests/testthat/test_bigvector.R
/usr/lib64/R/library/fst/tests/testthat/test_compress.R
/usr/lib64/R/library/fst/tests/testthat/test_date.R
/usr/lib64/R/library/fst/tests/testthat/test_encoding.R
/usr/lib64/R/library/fst/tests/testthat/test_factor.R
/usr/lib64/R/library/fst/tests/testthat/test_fst.R
/usr/lib64/R/library/fst/tests/testthat/test_fst_table.R
/usr/lib64/R/library/fst/tests/testthat/test_integer64.R
/usr/lib64/R/library/fst/tests/testthat/test_interface.R
/usr/lib64/R/library/fst/tests/testthat/test_keys.R
/usr/lib64/R/library/fst/tests/testthat/test_legacy.R
/usr/lib64/R/library/fst/tests/testthat/test_lintr.R
/usr/lib64/R/library/fst/tests/testthat/test_meta.R
/usr/lib64/R/library/fst/tests/testthat/test_nanotime.R
/usr/lib64/R/library/fst/tests/testthat/test_omp.R
/usr/lib64/R/library/fst/tests/testthat/test_rbind.R
/usr/lib64/R/library/fst/tests/testthat/test_roundtrip.R
/usr/lib64/R/library/fst/tests/testthat/test_time.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fst/libs/fst.so
/usr/lib64/R/library/fst/libs/fst.so.avx2
