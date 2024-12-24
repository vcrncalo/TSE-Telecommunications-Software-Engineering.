from QAM_test import test_happy_path, test_sad_path

if __name__ == '__main__':
	print("Currently, only the happy path test will run, if you want to run the sad path test you must uncomment the lines of code which will run the sad path test function.")
	# Call the happy path test
	print("Running happy path test...")
	test_happy_path()

    # Call the sad path test
#print("Running sad path test...")
#test_sad_path()
