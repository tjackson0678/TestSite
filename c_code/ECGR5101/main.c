///////////////////////////////////////
// Terrence Jackson
// ECGR 5101 - Adv Embeded Systems
// Fall 2025
// Project 1
////////////////////////////////////

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SENSORS 10

typedef struct
{
    char id[3]; // 2 chars + null terminator
    float temperature;
    int humidity;
} Sensor;

int main()
{
    char sensor_stream[] = "A1:23.5,45%|B2:-5.2,60%|C3:18.0,89%|D4:14,33%|E5:50,75%|F6:7,45%|G7:15,55%|H8:30,92%|I9:21.0,35%|";
    Sensor sensors[MAX_SENSORS];
    int sensor_count = 0;
    int sensor_max = 0;
    float sensor_total = 0;
    char *sensor_maxId;

    // Parse the sensor_stream and populate sensors array
    const char delimiters[] = "|"; // Space as delimiter
    char *token;
    token = strtok(sensor_stream, delimiters);

    sscanf(token, "%2[^:]:%f,%d%%", sensors[sensor_count].id, &sensors[sensor_count].temperature, &sensors[sensor_count].humidity);
    sensor_max = sensors[0].humidity;
    sensor_maxId = sensors[0].id;

    while (token != NULL)
    {
        sensor_count++;
        sscanf(token, "%2[^:]:%f,%d%%", sensors[sensor_count].id, &sensors[sensor_count].temperature, &sensors[sensor_count].humidity);
        sensor_total += sensors[sensor_count].temperature;

        // Find sensor with max humidity
        if (sensors[sensor_count].humidity > sensor_max)
        {
            sensor_max = sensors[sensor_count].humidity;
            sensor_maxId = sensors[sensor_count].id;
        }
        token = strtok(NULL, delimiters); // Continue tokenizing
    }

    // Compute average temperature
    float sensor_avg = sensor_total / sensor_count;

    printf("\nParsed %d sensor readings\n", sensor_count);
    printf("Average temperature: %.1f C\n", sensor_avg);
    printf("Sensor with highest humidity: %s (%d%%)\n\n", sensor_maxId, sensor_max);

    return 0;
}
