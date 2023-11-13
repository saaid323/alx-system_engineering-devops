## Issue summary
+ **Duration**: From 2pm to 2:40pm on November 11, 2023.
+ **Impact**: User could not access our web app.
+ **Root Cause**: Network Outage,  Disruptions in network connectivity.
## Timeline
+ **🕙10:00**: The issue was detected after receiving alert from datadog that our web app was down.
+ **🕙10:04**: Our first assumption was a server failure, but after investigation we found out that the problem was not the server.
+ **🕥10:25**: The incident escalated to security and network team.
+ **🕥10:40**: The web application was back up.
## Root Cause
The root cause was misconfiguration of the firewall rules.
## Resolution and recovery
The root cause was as misconfiguration of the firewall rules. It was causing the downtime.
The issues was resolves by rolling back. The problem wsa addresed and we successfully rolled back at 2:40 PM.
## Corrective and preventative measures
+ Provide training and  documentation.
+ Consider implementing automation tools for firewall management.
+ Learn from the misconfigurations and incidents.
