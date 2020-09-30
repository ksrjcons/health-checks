#!/usr/bin/env python3

# Change Log
# 2020-09-21: Add a comment line to see reflected in diff and Git
# 2020-09-22: Add a second comment line only to revert back later
# 2020-09-30: Add a dummy comment

import os
# 2020-09-21: The result will be False as there is reboot scheduled
# Dummy line added to test revert
def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

# Dummy commnent to uploaded file
print("The status of pending reboot is {}.".format(check_reboot()))
