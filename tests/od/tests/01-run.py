#!/usr/bin/env python3

# Copyright (C) 2016 Freie Universität Berlin
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import os
import sys

sys.path.append(os.path.join(os.environ['RIOTBASE'], 'dist/tools/testrunner'))
import testrunner

def testfunc(child):
    # check if running with newlib
    print("ATTENTION: This script is currently not suitable for non-native platforms")

    # test data width vs. output width discrepency
    child.expect_exact(r'od(short_str, sizeof(short_str), OD_WIDTH_DEFAULT, 0)')
    child.expect_exact(r'000000000 000000041101')

    # Test different output width in default configuration
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, 0)')
    child.expect_exact(r'000000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'000000020 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 4, 0)')
    child.expect_exact(r'000000000 037730226377')
    child.expect_exact(r'000000004 014430661056')
    child.expect_exact(r'000000010 015031663145')
    child.expect_exact(r'000000014 015432665151')
    child.expect_exact(r'000000020 016033667155')
    child.expect_exact(r'000000024 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 3, 0)')
    child.expect_exact(r'000000000 037730226377')
    child.expect_exact(r'000000004 014430661056')
    child.expect_exact(r'000000010 015031663145')
    child.expect_exact(r'000000014 015432665151')
    child.expect_exact(r'000000020 016033667155')
    child.expect_exact(r'000000024 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 8, 0)')
    child.expect_exact(r'000000000 037730226377 014430661056')
    child.expect_exact(r'000000010 015031663145 015432665151')
    child.expect_exact(r'000000020 016033667155 000000000000')

    # Test different address formats in default configuration
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_OCTAL)')
    child.expect_exact(r'000000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'000000020 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_HEX)')
    child.expect_exact(r'000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'000010 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_DECIMAL)')
    child.expect_exact(r'0000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'0000016 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_NONE)')
    child.expect_exact(r' 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r' 016033667155 000000000000')

    # Test octal data format with different address formats
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_OCTAL)')
    child.expect_exact(r'000000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'000000020 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_OCTAL | OD_FLAGS_BYTES_OCTAL)')
    child.expect_exact(r'000000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'000000020 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_HEX | OD_FLAGS_BYTES_OCTAL)')
    child.expect_exact(r'000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'000010 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_DECIMAL | OD_FLAGS_BYTES_OCTAL)')
    child.expect_exact(r'0000000 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r'0000016 016033667155 000000000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_ADDRESS_NONE | OD_FLAGS_BYTES_OCTAL)')
    child.expect_exact(r' 037730226377 014430661056 015031663145 015432665151')
    child.expect_exact(r' 016033667155 000000000000')

    # Test different data formats
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_CHAR)')
    child.expect_exact(r'000000000  377    ,    a  377    .    b    c    d    e    f    g    h    i    j    k    l')
    child.expect_exact(r'000000020    m    n    o    p   \0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT)')
    child.expect_exact(r'000000000    -10408705   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL)')
    child.expect_exact(r'000000000    -10408705   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT)')
    child.expect_exact(r'000000000   4284558591   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX)')
    child.expect_exact(r'000000000 ff612cff 6463622e 68676665 6c6b6a69')
    child.expect_exact(r'000000020 706f6e6d 00000000')

    # Test octal byte-wise output with different output lengths
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000 377 054 141 377 056 142 143 144 145 146 147 150 151 152 153 154')
    child.expect_exact(r'000000020 155 156 157 160 000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 4, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000 377 054 141 377')
    child.expect_exact(r'000000004 056 142 143 144')
    child.expect_exact(r'000000010 145 146 147 150')
    child.expect_exact(r'000000014 151 152 153 154')
    child.expect_exact(r'000000020 155 156 157 160')
    child.expect_exact(r'000000024 000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 3, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000 377 054 141')
    child.expect_exact(r'000000003 377 056 142')
    child.expect_exact(r'000000006 143 144 145')
    child.expect_exact(r'000000011 146 147 150')
    child.expect_exact(r'000000014 151 152 153')
    child.expect_exact(r'000000017 154 155 156')
    child.expect_exact(r'000000022 157 160 000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 8, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000 377 054 141 377 056 142 143 144')
    child.expect_exact(r'000000010 145 146 147 150 151 152 153 154')
    child.expect_exact(r'000000020 155 156 157 160 000')

    # Test different data formats with byte-wise output
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_CHAR | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000  377    ,    a  377    .    b    c    d    e    f    g    h    i    j    k    l')
    child.expect_exact(r'000000020    m    n    o    p   \0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000   -1   44   97   -1   46   98   99  100  101  102  103  104  105  106  107  108')
    child.expect_exact(r'000000020  109  110  111  112    0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000   -1   44   97   -1   46   98   99  100  101  102  103  104  105  106  107  108')
    child.expect_exact(r'000000020  109  110  111  112    0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000 255  44  97 255  46  98  99 100 101 102 103 104 105 106 107 108')
    child.expect_exact(r'000000020 109 110 111 112   0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_1)')
    child.expect_exact(r'000000000 ff 2c 61 ff 2e 62 63 64 65 66 67 68 69 6a 6b 6c')
    child.expect_exact(r'000000020 6d 6e 6f 70 00')

    # Test octal 2-byte-wise output with different output lengths
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000 026377 177541 061056 062143 063145 064147 065151 066153')
    child.expect_exact(r'000000020 067155 070157 000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 4, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000 026377 177541')
    child.expect_exact(r'000000004 061056 062143')
    child.expect_exact(r'000000010 063145 064147')
    child.expect_exact(r'000000014 065151 066153')
    child.expect_exact(r'000000020 067155 070157')
    child.expect_exact(r'000000024 000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 3, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000 026377')
    child.expect_exact(r'000000002 177541')
    child.expect_exact(r'000000004 061056')
    child.expect_exact(r'000000006 062143')
    child.expect_exact(r'000000010 063145')
    child.expect_exact(r'000000012 064147')
    child.expect_exact(r'000000014 065151')
    child.expect_exact(r'000000016 066153')
    child.expect_exact(r'000000020 067155')
    child.expect_exact(r'000000022 070157')
    child.expect_exact(r'000000024 000000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 8, OD_FLAGS_BYTES_OCTAL | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000 026377 177541 061056 062143')
    child.expect_exact(r'000000010 063145 064147 065151 066153')
    child.expect_exact(r'000000020 067155 070157 000000')

    # Test 2-byte-char output (should just return normal char output)
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_CHAR | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  377    ,    a  377    .    b    c    d    e    f    g    h    i    j    k    l')
    child.expect_exact(r'000000020    m    n    o    p   \0')

    # Test 2-byte-int output with different output widths
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  11519   -159  25134  25699  26213  26727  27241  27755')
    child.expect_exact(r'000000020  28269  28783      0')
    child.expect_exact(r'od(long_str, sizeof(long_str), 5, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  11519   -159')
    child.expect_exact(r'000000004  25134  25699')
    child.expect_exact(r'000000010  26213  26727')
    child.expect_exact(r'000000014  27241  27755')
    child.expect_exact(r'000000020  28269  28783')
    child.expect_exact(r'000000024      0')

    # Test 2-byte-decimal output with different output widths
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  11519   -159  25134  25699  26213  26727  27241  27755')
    child.expect_exact(r'000000020  28269  28783      0')
    child.expect_exact(r'od(long_str, sizeof(long_str), 5, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  11519   -159')
    child.expect_exact(r'000000004  25134  25699')
    child.expect_exact(r'000000010  26213  26727')
    child.expect_exact(r'000000014  27241  27755')
    child.expect_exact(r'000000020  28269  28783')
    child.expect_exact(r'000000024      0')

    # Test 2-byte-unsigned-int output with different output widths
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  11519  65377  25134  25699  26213  26727  27241  27755')
    child.expect_exact(r'000000020  28269  28783      0')
    child.expect_exact(r'od(long_str, sizeof(long_str), 5, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000  11519  65377')
    child.expect_exact(r'000000004  25134  25699')
    child.expect_exact(r'000000010  26213  26727')
    child.expect_exact(r'000000014  27241  27755')
    child.expect_exact(r'000000020  28269  28783')
    child.expect_exact(r'000000024      0')

    # Test 2-byte-hex output with different output widths
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000 2cff ff61 622e 6463 6665 6867 6a69 6c6b')
    child.expect_exact(r'000000020 6e6d 706f 0000')
    child.expect_exact(r'od(long_str, sizeof(long_str), 5, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_2)')
    child.expect_exact(r'000000000 2cff ff61')
    child.expect_exact(r'000000004 622e 6463')
    child.expect_exact(r'000000010 6665 6867')
    child.expect_exact(r'000000014 6a69 6c6b')
    child.expect_exact(r'000000020 6e6d 706f')
    child.expect_exact(r'000000024 0000')

    # Test different 4-byte-wise byte formats
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_4)')
    child.expect_exact(r'000000000    -10408705   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_4)')
    child.expect_exact(r'000000000    -10408705   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_4)')
    child.expect_exact(r'000000000   4284558591   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_4)')
    child.expect_exact(r'000000000 ff612cff 6463622e 68676665 6c6b6a69')
    child.expect_exact(r'000000020 706f6e6d 00000000')

    # Test different 8-byte-wise byte formats
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_8)')
    child.expect_exact(r'000000000      7233733380479724799      7812454979559974501')
    child.expect_exact(r'000000020               1886350957')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_8)')
    child.expect_exact(r'000000000      7233733380479724799      7812454979559974501')
    child.expect_exact(r'000000020               1886350957')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_8)')
    child.expect_exact(r'000000000      7233733380479724799      7812454979559974501')
    child.expect_exact(r'000000020               1886350957')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_8)')
    child.expect_exact(r'000000000 6463622eff612cff 6c6b6a6968676665')
    child.expect_exact(r'000000020 00000000706f6e6d')

    # Test different char-wise byte formats
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_CHAR)')
    child.expect_exact(r'000000000   -1   44   97   -1   46   98   99  100  101  102  103  104  105  106  107  108')
    child.expect_exact(r'000000020  109  110  111  112    0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_CHAR)')
    child.expect_exact(r'000000000   -1   44   97   -1   46   98   99  100  101  102  103  104  105  106  107  108')
    child.expect_exact(r'000000020  109  110  111  112    0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_CHAR)')
    child.expect_exact(r'000000000 255  44  97 255  46  98  99 100 101 102 103 104 105 106 107 108')
    child.expect_exact(r'000000020 109 110 111 112   0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_CHAR)')
    child.expect_exact(r'000000000 ff 2c 61 ff 2e 62 63 64 65 66 67 68 69 6a 6b 6c')
    child.expect_exact(r'000000020 6d 6e 6f 70 00')

    # Test different short-wise byte formats
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_SHORT)')
    child.expect_exact(r'000000000  11519   -159  25134  25699  26213  26727  27241  27755')
    child.expect_exact(r'000000020  28269  28783      0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_SHORT)')
    child.expect_exact(r'000000000  11519   -159  25134  25699  26213  26727  27241  27755')
    child.expect_exact(r'000000020  28269  28783      0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_SHORT)')
    child.expect_exact(r'000000000  11519  65377  25134  25699  26213  26727  27241  27755')
    child.expect_exact(r'000000020  28269  28783      0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_SHORT)')
    child.expect_exact(r'000000000 2cff ff61 622e 6463 6665 6867 6a69 6c6b')
    child.expect_exact(r'000000020 6e6d 706f 0000')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_INT | OD_FLAGS_LENGTH_LONG)')
    child.expect_exact(r'000000000    -10408705   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_DECIMAL | OD_FLAGS_LENGTH_LONG)')
    child.expect_exact(r'000000000    -10408705   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_UINT | OD_FLAGS_LENGTH_LONG)')
    child.expect_exact(r'000000000   4284558591   1684234798   1751606885   1818978921')
    child.expect_exact(r'000000020   1886350957            0')
    child.expect_exact(r'od(long_str, sizeof(long_str), OD_WIDTH_DEFAULT, OD_FLAGS_BYTES_HEX | OD_FLAGS_LENGTH_LONG)')
    child.expect_exact(r'000000000 ff612cff 6463622e 68676665 6c6b6a69')
    child.expect_exact(r'000000020 706f6e6d 00000000')

    print("All tests successful")

if __name__ == "__main__":
    sys.exit(testrunner.run(testfunc, timeout=1, echo=False))
