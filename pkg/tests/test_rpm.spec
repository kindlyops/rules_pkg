Name: rules_pkg
Version: 0
Release: 1
Summary: Test data
URL: https://github.com/bazelbuild/rules_pkg
License: Apache License, v2.0

# Do not try to use magic to determine file types
%define __spec_install_post %{nil}
# Do not die becuse we give it more input files than are in the files section
%define _unpackaged_files_terminate_build 0

%description
This is a package description.

%prep

%build

%install
cp -r ./tests %{buildroot}/

%files
/tests/testdata/a.ar
/tests/testdata/a_ab.ar
/tests/testdata/a_b.ar
/tests/testdata/a_b_ab.ar
/tests/testdata/ab.ar
/tests/testdata/b.ar
/tests/testdata/config
