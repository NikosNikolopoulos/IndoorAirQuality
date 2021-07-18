# Visualizing Indoor Air Quality 

- [x] Plotting IAQ data obtained from sample dataset generated by 
[Honeywell Indoor Air Quality Detector](https://ifworlddesignguide.com/entry/234934-honeywell-indoor-air-quality-detector#:~:text=The%20Honeywell%20IAQ%20tracks%20and,displaying%20temperature%20and%20humidity%20levels.).
- [x] Measurements: 
  - PM2.5 ~ [μg/m3]
  - Temperature ~ [°C]
  - Humidity ~ [%]
- [x] Dividing data points depending on the health level of the corresponding IAQ index. For this process the following table was utilized. 
  
    |     PM2.5     |    AQI      |            Health Level         |
    |---------------|:-----------:|--------------------------------:|
    |   0.0 ~ 15.4  |    0 ~ 50   |                Good             |
    |  15.5 ~ 40.4  |   51 ~ 100  |            Moderate             |
    |  40.5 ~ 65.4  |   101 ~ 150 |  Unhealthy for sensitive groups |
    |  65.5 ~ 150.4 |   151 ~ 200 |  Unhealthy                      |
    | 150.5 ~ 250.4 |   201 ~ 300 |  Very unhealthy                 |
    | 250.5 ~ 350.4 |   301 ~ 400 |  Hazardous                      |
    | 350.5 ~ 500.4 |   401 ~ 500 |  Hazardous                      |

## References
[1] https://github.com/SophonAlpha/visualise-IAQ-data

[2] https://ieeexplore.ieee.org/document/6907986