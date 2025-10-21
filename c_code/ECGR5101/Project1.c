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
    char sensor_stream[] = "A1:23.5,45%|H8:30,92%|I9:21.0,35%|JA:5.8,55%|";
    Sensor sensors[MAX_SENSORS];
    int sensor_count = 0;
    int sensor_max = 0;
    float sensor_total = 0;
    char *sensor_maxId;

    // Parse the sensor_stream and populate sensors array
    const char delimiters[] = "|"; // Space as delimiter
    char *token;
    token = strtok(sensor_stream, delimiters);

    while (token != NULL)
    {
        sscanf(token, "%2[^:]:%f,%d%%", sensors[sensor_count].id, &sensors[sensor_count].temperature, &sensors[sensor_count].humidity);
        sensor_total += sensors[sensor_count].temperature;
        sensor_count++;

        token = strtok(NULL, delimiters); // Continue tokenizing
    }

    // Compute average temperature
    float sensor_avg = sensor_total / sensor_count;

    for (int j = 0; j < sensor_count; j++)
    {
        // Find sensor with max humidity
        if (sensors[j].humidity > sensor_max)
        {
            sensor_max = sensors[j].humidity;
            sensor_maxId = sensors[j].id;
        }
    }

    printf("\nParsed %d sensor readings\n", sensor_count);
    printf("Average temperature: %.1f C\n", sensor_avg);
    printf("Sensor with highest humidity: %s (%d%%)\n\n", sensor_maxId, sensor_max);

    return 0;
}