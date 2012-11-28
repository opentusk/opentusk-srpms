#
# Build mock and local RPM versions of tools
#

# Assure that sorting is case sensitive
LANG=C

#MOCKS+=rpmforge-extras-6-i386
MOCKS+=rpmforge-extras-5-i386
#MOCKS+=rpmforge-extras-4-i386

MOCKS+=rpmforge-extras-6-x86_64
MOCKS+=rpmforge-extras-5-x86_64
#MOCKS+=rpmforge-extras-4-x86_64

# Recent changes in mock-1.1.28 demand full SPEC file path
SPEC := `ls *.spec | head -1`
PKGNAME := `ls *.spec | head -1 | sed 's/.spec$$//g'`

all:: verifyspec $(MOCKS)

# Oddness to get deduced .spec file verified
verifyspec:: FORCE
	@if [ ! -e $(SPEC) ]; then \
	    echo Error: SPEC file $(SPEC) not found, exiting; \
	    exit 1; \
	fi

srpm:: verifyspec FORCE
	@echo "Building SRPM with $(SPEC)"
	rm -f $(PKGNAME)*.src.rpm
	rpmbuild --define '_sourcedir $(PWD)' \
		--define '_srcrpmdir $(PWD)' \
		-bs $(PWD)/$(SPEC) --nodeps

build:: srpm FORCE
	rpmbuild --rebuild `ls *.src.rpm | grep -v ^rpmforge-extras-`

$(MOCKS):: verifyspec FORCE
	@echo "Building $@ RPMS with $(SPEC)"
	@rm -rf $@
	/usr/bin/mock -q -r $@ \
		--resultdir=$(PWD)/$@ \
		--buildsrpm \
		--sources=$(PWD) \
		--spec=$(PWD)/$(SPEC)
	@echo "Storing $@/*.src.rpm in $@.rpm"
	/bin/mv $@/*.src.rpm $@.src.rpm
	@echo "Actally building RPMS in $@"
	@rm -rf $@
	/usr/bin/mock -q -r $@ \
	     --resultdir=$(PWD)/$@ \
	     $(PWD)/$@.src.rpm

mock:: $(MOCKS)

clean::
	rm -rf $(MOCKS)

realclean distclean:: clean
	rm -f *.src.rpm

FORCE:
