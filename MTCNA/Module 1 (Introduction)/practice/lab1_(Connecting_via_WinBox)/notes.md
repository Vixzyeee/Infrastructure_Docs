```bash
## What is WinBox?

WinBox is MikroTik’s native configuration utility used to manage RouterBOARD devices.
It provides a GUI-based interface that communicates directly with RouterOS, offering full access to system configuration, monitoring, and debugging features.  
WinBox supports both MAC-based Layer 2 connectivity and standard IP-based Layer 3 sessions, making it suitable for initial setup, recovery, and production-grade management workflows.

## Understanding Connection Methods

**MAC Address Login**  
Used when the router has no IP configuration, the IP is unknown, or the device becomes unreachable due to misconfiguration.
WinBox communicates over Layer 2, allowing direct access within the same broadcast domain regardless of IP settings.
This method is ideal for initial provisioning, recovery scenarios, and situations where L3 connectivity is not yet available.

**IP Address Login**  
The standard operational method once the router is properly configured.
IP-based access provides stable Layer 3 connectivity, supports remote management across different subnets, and aligns with production environments where routing, VLANs, and access control are enforced.
This approach is required for any scalable or remotely managed deployment.
