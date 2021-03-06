#!/usr/bin/env python
"""Fixture files for the pyhtslib.bam tests"""

import os
import py
import pytest

import pyhtslib.bam_internal as bam_internal
import pyhtslib.hts_internal as hts_internal

__author__ = 'Manuel Holtgrewe <manuel.holtgrewe@bihealth.de>'

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.yield_fixture
def header_only_sam(tmpdir):
    """Copy the header_only.sam file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'header_only.sam')
    dst = tmpdir.join('header_only.sam')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def header_only_sam_header(header_only_sam):
    hts_file = hts_internal._hts_open(
        str(header_only_sam).encode('utf-8'), 'r')
    hdr = bam_internal._sam_hdr_read(hts_file)
    yield hdr
    bam_internal._bam_hdr_destroy(hdr)
    hts_internal._hts_close(hts_file)


@pytest.yield_fixture
def header_only_sam_gz(tmpdir):
    """Copy the header_only.sam.gz file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'header_only.sam.gz')
    dst = tmpdir.join('header_only.sam.gz')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def header_only_sam_gz_header(header_only_sam_gz):
    hts_file = hts_internal._hts_open(
        str(header_only_sam_gz).encode('utf-8'), 'r')
    hdr = bam_internal._sam_hdr_read(hts_file)
    yield hdr
    bam_internal._bam_hdr_destroy(hdr)
    hts_internal._hts_close(hts_file)


@pytest.yield_fixture
def header_only_bam(tmpdir):
    """Copy the header_only.bam file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'header_only.bam')
    dst = tmpdir.join('header_only.bam')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def header_only_bai(tmpdir):
    """Copy the header_only.bam.bai file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'header_only.bam.bai')
    dst = tmpdir.join('header_only.bam.bai')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def six_records_sam(tmpdir):
    """Copy the six_records.sam file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'six_records.sam')
    dst = tmpdir.join('six_records.sam')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def six_records_sam_header(six_records_sam):
    hts_file = hts_internal._hts_open(
        str(six_records_sam).encode('utf-8'), 'r')
    hdr = bam_internal._sam_hdr_read(hts_file)
    yield hdr
    bam_internal._bam_hdr_destroy(hdr)
    hts_internal._hts_close(hts_file)


@pytest.yield_fixture
def six_records_sam_gz(tmpdir):
    """Copy the six_records.sam.gz file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'six_records.sam.gz')
    dst = tmpdir.join('six_records.sam.gz')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def six_records_sam_gz_header(six_records_sam_gz):
    hts_file = hts_internal._hts_open(
        str(six_records_sam_gz).encode('utf-8'), 'r')
    hdr = bam_internal._sam_hdr_read(hts_file)
    yield hdr
    bam_internal._bam_hdr_destroy(hdr)
    hts_internal._hts_close(hts_file)


@pytest.yield_fixture
def six_records_bam(tmpdir):
    """Copy the six_records.bam file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'six_records.bam')
    dst = tmpdir.join('six_records.bam')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def six_records_bai(tmpdir):
    """Copy the six_records.bam.bai file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'six_records.bam.bai')
    dst = tmpdir.join('six_records.bam.bai')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def two_hundred_sam(tmpdir):
    """Copy the two_hundred.sam file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'two_hundred.sam')
    dst = tmpdir.join('two_hundred.sam')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def two_hundred_sam_gz(tmpdir):
    """Copy the two_hundred.sam.gz file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'two_hundred.sam.gz')
    dst = tmpdir.join('two_hundred.sam.gz')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def two_hundred_tbi(tmpdir):
    """Copy the two_hundred.sam.gz.tbi file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'two_hundred.sam.gz.tbi')
    dst = tmpdir.join('two_hundred.sam.gz.tbi')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def two_hundred_bam(tmpdir):
    """Copy the two_hundred.bam file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'two_hundred.bam')
    dst = tmpdir.join('two_hundred.bam')
    src.copy(dst)
    yield dst
    dst.remove()


@pytest.yield_fixture
def two_hundred_bai(tmpdir):
    """Copy the two_hundred.bam.bai file to temporary directory."""
    src = py.path.local(os.path.dirname(__file__)).join(
        'files', 'two_hundred.bam.bai')
    dst = tmpdir.join('two_hundred.bam.bai')
    src.copy(dst)
    yield dst
    dst.remove()
