#! /usr/bin/env python3

import os
import shutil
import sys
import socket

def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required-old")

def check_disk_full(disk, min_gb, min_percent):
	"""Returns True if there isn't enough disk space, False otherwise."""
	du = shutil.disk_usage(disk)
	# Calculate the percentage of the free space
	percent_free = 100 * du.free / du.total
	# Calculate how many free gygabytes there are
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
		return True
	return False

def check_root_full():
	"""Returns True if the root partition is full, False otherwise."""
	return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
	"""Retunrns True if it fails to resolve Google's URL, False otherwise."""
	try:
		socket.gethostbyname("www.google.ca")
		return False
	except:
		return True

def main():
	checks=[
		(check_reboot, "Pending Reboot"),
		(check_root_full, "Root partition full"),
		(check_no_network, "No working network"),
	]

	everything_ok=True # Initialize flag
	for check, msg in checks: # Loop to print each msg
		if check():
			print(msg)
			everything_ok = False # Change flag when check is true
	if not everything_ok: # Test flag
		sys.exit(1)

	print("Everything looks fine.")
	sys.exit(0)

main()
