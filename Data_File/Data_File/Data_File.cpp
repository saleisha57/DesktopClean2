#include <iostream>
#include <stdlib.h>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
	srand(time(0));                                                                                               // Set program time to 0 to ensure that randomization happens.

	ofstream data_file;                                                                                           // Create an out file called data_file.
	data_file.open("data_file.txt");                                                                              // Open data_file.

	int PID, priority, arrival_time, C_burst, I_burst;                                                            // Declare 5 integers with process information.

	PID = 0;                                                                                                      // Set PID to 0.
	
	for (int i = 0; i < 1000; i++)                                                                                // Set a for loop that iterates 1000 times.
	{
		PID += 1;                                                                                                 // Increase PID by 1.
		priority = rand() % ((5 - 1) + 1) + 1;                                                                    // Randomly generate a number between 1 and 5 for the priority.
		arrival_time = rand() % 151;                                                                              // Randomly generate a number between 0 and 150 for the arrival time.
		C_burst = rand() % ((20 - 1) + 1) + 1;                                                                    // Randomly generate a number between 1 and 20 for the CPU Burst time.
		I_burst = rand() % ((20 - 1) + 1) + 1;                                                                    // Randomly generate a number between 1 and 20 for the I/O Burst time.

		data_file << PID << " " << arrival_time << " " << priority << " " << C_burst << " " << I_burst << "\n";   // Populate the out file.
	}

	data_file.close();                                                                                            // Close the out file.

	system("pause");                                                                                              // Pause to test the outputs.

	return 0;
}
