# SPDX-FileCopyrightText: 2024 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0
import pytest
from pytest_embedded import Dut
from pytest_embedded_idf.app import IdfApp


@pytest.mark.esp32c3
@pytest.mark.esp32s3
@pytest.mark.generic
def test_custom_bootloader_multiboot_example(app: IdfApp, dut: Dut) -> None:
    # Expect to see all three partitions in the list
    dut.expect_exact('default')
    dut.expect_exact('hello_world')
    dut.expect_exact('console')
    # Send "down arrow" signal to select the second image, which should be `hello_world`
    dut.write('\x1b[B')
    # Send Enter to validate and start the image
    dut.write('\n')
    # Make sure the example booted properly
    dut.expect('Hello world!')
