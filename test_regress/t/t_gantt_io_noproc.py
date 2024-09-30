#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('dist')

test.run(cmd=[
    "cd " + test.obj_dir + " && " + os.environ["VERILATOR_ROOT"] + "/bin/verilator_gantt" +
    " --no-vcd", test.t_dir + "/" + test.name + ".dat > gantt.log"
],
         check_finished=False)

test.files_identical(test.obj_dir + "/gantt.log", test.golden_filename)

test.passes()
